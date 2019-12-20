#https://github.com/vishnubob/python-midi

import os
from os.path import isfile, join
import scipy.io.wavfile as waves    #does not handle 24bit audio. 8, 16, 32 only.
import numpy as np
import mido as md

sample_directory = 'Samples'
score_name = 'score.mid'

cwd_path = os.getcwd()
samples_path = join(cwd_path, sample_directory)
score_path = join(cwd_path, score_name)

score_file = md.MidiFile(score_path, clip=True)

#microseconds/beat
tempo = 0
for _, track in enumerate(score_file.tracks):
        for msg in track:
            if msg.is_meta:
                try:
                    tempo = msg.tempo
                    break
                except:
                    pass
        if tempo != 0:
            break

print('Length: ' + str(score_file.length))
print('tempo: ' + str(tempo))


#md.tick2second(92160, score_file.ticks_per_beat, score_file.tempo)


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


