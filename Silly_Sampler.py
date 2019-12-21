import os
from os.path import isfile, join
#import scipy.io.wavfile as waves    #requires install; does not handle 24bit audio. 8, 16, 32 only.
import numpy as np                  #requires install
import mido as md                   #requires install
import random
import librosa                      #requires install
import soundfile as sf              #requires install 

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

    for track in score_file.tracks:
        print('Processing ' + track.name + '...')

        output_buffer = np.zeros((int(score_file.length * fs),))
        buffer_modified = False
        tick = 0

        sample_dict = {}

        num_events = len(track)
        print(num_events)
        i = 0
        while i < num_events:
            if i % 32 == 0:
                print(str(100*i / num_events)+'%')
            tick += track[i].time

            if track[i].type == 'note_on':
                if not track[i].note in sample_dict:
                    #choose a sample
                    if not all_samples_names:
                        all_samples_names = used_samples.copy()
                        used_samples = []

                    #sample_dict[track[i].note] = random.choice(all_samples_names)
                    #all_samples_names.remove(sample_dict[track[i].note])
                    #used_samples.append(sample_dict[track[i].note])
                    chosen_sample_name = random.choice(all_samples_names)

                    #load the sample
                    sample_data, _ = librosa.load(join(cwd_path, sample_directory, chosen_sample_name))
                    MIDI_note = get_MIDI_note(sample_data, fs)
                    sample_dict[track[i].note] = librosa.effects.pitch_shift(sample_data, fs, track[i].note - MIDI_note)

                #load the sample
                #sample_name = sample_dict[track[i].note]
                #_, sample_data = waves.read(join(cwd_path, sample_directory, sample_name))
                #sample_data, _ = librosa.load(join(cwd_path, sample_directory, sample_name))
                
                #write the sample to buffer
                start_sample = int(md.tick2second(tick, score_file.ticks_per_beat, tempo*fs))
                for j in range(len(sample_data)):
                    if start_sample+j >= len(output_buffer):
                        break
                    val = gain * track[i].velocity/127 * sample_dict[track[i].note][j]
                    
                    """if track.name == 'Main':
                        print('v' + str(track[i].velocity))
                        print('sd' + str(sample_data[j]))
                        print(j)
                        print(val)"""
                    
                    if val != 0:
                        buffer_modified = True
                    output_buffer[start_sample+j] += val
            i += 1         
        
        if buffer_modified:
            print('Writing ' + track.name + ' to file')
            #waves.write(join(cwd_path, 'output', track.name + '.wav'), fs, output_buffer)
            sf.write(join(cwd_path, 'Output', track.name + '.wav'), output_buffer, fs)

    """
    # wav tutorial
    all_files = [f for f in os.listdir(samples_path) if isfile(join(samples_path, f))]

    for f in all_files:
        fs, data = waves.read(join(cwd_path, sample_directory, f))
        new_data = np.zeros((2, len(data)), dtype=type(data[0]))

        for i in range(len(data)):
            new_data[0][i] = data[i]
            new_data[1][i] = data[i]

        if '440' in f:
            waves.write(join(cwd_path, sample_directory, 'test.wav'), 44100, new_data)

    op = waves.read(join(cwd_path, sample_directory, 'test.wav'))
    print(op)"""


