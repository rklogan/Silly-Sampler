import os
from os.path import isfile, join
import scipy.io.wavfile as waves    #does not handle 24bit audio. 8, 16, 32 only.
import numpy as np
import mido as md
import random

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

        output_buffer = np.zeros((int(score_file.length * fs),), dtype=np.int16)
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

                    sample_dict[track[i].note] = random.choice(all_samples_names)
                    all_samples_names.remove(sample_dict[track[i].note])
                    used_samples.append(sample_dict[track[i].note])
                
                #load the sample
                sample_name = sample_dict[track[i].note]
                _, sample_data = waves.read(join(cwd_path, sample_directory, sample_name))

                #write the sample to buffer
                start_sample = int(md.tick2second(tick, score_file.ticks_per_beat, tempo*fs))
                for j in range(len(sample_data)):
                    if start_sample+j >= len(output_buffer):
                        break
                    val = track[i].velocity/127 * sample_data[j]
                    
                    """if track.name == 'Main':
                        print('v' + str(track[i].velocity))
                        print('sd' + str(sample_data[j]))
                        print(j)
                        print(val)"""
                    
                    if val != 0:
                        buffer_modified = True
                    output_buffer[start_sample+j] += np.int16(gain * val)
            i += 1         
        
        if buffer_modified:
            print('Writing ' + track.name + ' to file')
            waves.write(join(cwd_path, 'output', track.name + '.wav'), fs, output_buffer)


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


