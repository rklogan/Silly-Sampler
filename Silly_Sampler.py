import os
from os.path import isfile, join
import scipy.io.wavfile as waves

sample_directory = 'Samples'

cwd_path = os.getcwd()
samples_path = os.path.join(cwd_path, sample_directory)

all_files = [f for f in os.listdir(samples_path) if isfile(join(samples_path, f))]

for f in all_files:
    fs, data = waves.read(join(cwd_path, sample_directory, f))
    print('fs: ' + str(fs))
    print(data)

