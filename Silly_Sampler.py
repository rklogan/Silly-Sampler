import os
from os.path import isfile, join
import numpy as np                  #requires install
import mido as md                   #requires install
import random
import librosa                      #requires install
import soundfile as sf              #requires install 
import sys

VERBOSE = True

def get_MIDI_note(sample_data, fs):
    pitches, magnitudes = librosa.core.piptrack(y=sample_data, sr=fs)

    max_mag = -1.0
    max_bin = -1
    max_frame = -1

    for i in range(len(magnitudes)):
        for j in range(len(magnitudes[i])):
            if magnitudes[i][j] > max_mag:
                max_mag = magnitudes[i][j]
                max_bin = i
                max_frame = j

    return librosa.hz_to_midi(pitches[max_bin][max_frame])

if __name__ == "__main__":
    sample_directory = 'Samples'
    score_name = 'score.mid'
    fs = 44100
    gain = 0.1

    if len(sys.argv) > 1:
        if sys.argv[1] != 'None':
            sample_directory = sys.argv[1]
    if len(sys.argv) > 2:
        if sys.argv[2] != 'None':
            score_name = sys.argv[2]
    if len(sys.argv) > 3:
        if sys.argv[3] != 'None':
            gain = float(sys.argv[3])
    if len(sys.argv) > 4:
        if sys.argv[4][0] == 'f' or sys.argv[4][0] == 'F':
            VERBOSE = False

    cwd_path = os.getcwd()
    samples_path = join(cwd_path, sample_directory)
    score_path = join(cwd_path, score_name)

    score_file = md.MidiFile(score_path, clip=True)

    #microseconds/beat
    tempo = 0

    #extract the tempo from the midi file
    for track in score_file.tracks:
            for msg in track:
                if msg.is_meta:
                    try:
                        tempo = msg.tempo
                        break
                    except:
                        pass
            if tempo != 0:
                break

    #load the names of the samples
    all_samples_names = [f for f in os.listdir(samples_path) if isfile(join(samples_path, f))]
    used_samples = []

    #process each track in the MIDI file
    for track in score_file.tracks:
        if VERBOSE: print('Processing ' + track.name + '...')

        output_buffer = np.zeros((int(score_file.length * fs),))
        buffer_modified = False         #avoids writing empty audio files
        tick = 0                        #tick in MIDI clock

        sample_dict = {}                #will store pitched samples
        num_events = len(track)
        
        i = 0
        while i < num_events:
            if VERBOSE and i % 32 == 0 and i != 0:
                print(str(i) + ' of ' + str(num_events) + ' processed for track: ' + track.name + '\t\t\t\t' + str(int(100*i/num_events)) + '%')
            tick += track[i].time

            if track[i].type == 'note_on':
                if not track[i].note in sample_dict:
                    #choose a sample
                    if not all_samples_names:
                        all_samples_names = used_samples.copy()
                        used_samples = []

                    chosen_sample_name = random.choice(all_samples_names)
                    all_samples_names.remove(chosen_sample_name)
                    used_samples.append(chosen_sample_name)

                    #load the sample
                    sample_data, _ = librosa.load(join(cwd_path, sample_directory, chosen_sample_name))
                    MIDI_note = get_MIDI_note(sample_data, fs)
                    sample_dict[track[i].note] = librosa.effects.pitch_shift(sample_data, fs, track[i].note - MIDI_note)

                #write the sample to buffer
                start_sample = int(md.tick2second(tick, score_file.ticks_per_beat, tempo*fs))
                j = 0
                for j in range(len(sample_dict[track[i].note])):
                    if start_sample+j >= len(output_buffer):
                        break
                    
                    val = gain * track[i].velocity/127 * sample_dict[track[i].note][j]
                    
                    if val != 0:
                        buffer_modified = True
                    output_buffer[start_sample+j] += val
            i += 1         
        
        #write buffer to file
        if buffer_modified:
            if VERBOSE: 
                print('Finished processing track: ' + track.name)
                print('Writing ' + track.name + ' to file')
            sf.write(join(cwd_path, 'Output', track.name + '.wav'), output_buffer, fs)
