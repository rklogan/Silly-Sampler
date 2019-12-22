# MIT License
# Copyright <2019> <Ryan Logan>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this 
# software and associated documentation files (the "Software"), to deal in the Software 
# without restriction, including without limitation the rights to use, copy, modify, merge, 
# publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons 
# to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or 
# substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.

import os
from os.path import isfile, join
import numpy as np                  #requires install
import mido as md                   #requires install
import random
import librosa                      #requires install
import soundfile as sf              #requires install 
import sys
import time

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
    output_directory = 'Output'
    fs = 22050                  
    gain = 0.2

    if len(sys.argv) > 1:
        if sys.argv[1] != 'None':
            sample_directory = sys.argv[1]
    if len(sys.argv) > 2:
        if sys.argv[2] != 'None':
            score_name = sys.argv[2]
    if len(sys.argv) > 3:
        if sys.argv[3] != 'None':
            output_directory = sys.argv[3]
    if len(sys.argv) > 4:
        if sys.argv[4] != 'None':
            gain = float(sys.argv[4])
    if len(sys.argv) > 5:
        if sys.argv[5][0] == 'f' or sys.argv[5][0] == 'F':
            VERBOSE = False

    cwd_path = os.getcwd()
    samples_path = join(cwd_path, sample_directory)
    score_path = join(cwd_path, score_name)
    output_path = join(cwd_path, output_directory)

    #check if the source exists
    if not os.path.exists(samples_path) or os.path.isfile(samples_path) :
        print('The directory ' + samples_path + ' does not exist.')
        print('Aborting...')
        sys.exit(1)

    #check if the destination exists, if not create it
    if os.path.isfile(output_path):
        print('The specified output directory, ' + output_path + ' is already a file.')
        print('Aborting...')
        sys.exit(1)
    elif not os.path.exists(output_path):
        os.mkdir(output_path)


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

    #update the sample rate
    _, fs = librosa.load(join(cwd_path, sample_directory, all_samples_names[0]), sr=None)

    #process each track in the MIDI file
    name = 0
    for track in score_file.tracks:
        if track.name == '' or track.name == None:
            track.name = 'Track ' + str(name)
            name += 1
        if VERBOSE: print('Processing ' + track.name + '...')

        output_buffer = np.zeros((int(score_file.length * fs),))
        buffer_modified = False         #avoids writing empty audio files
        tick = 0                        #tick in MIDI clock

        sample_dict = {}                #will store pitched samples
        num_events = len(track)
        
        i = 0
        while i < num_events:
            if VERBOSE and i % 32 == 0 and i != 0:
                print(str(i) + ' of ' + str(num_events) + ' events processed for track: ' + track.name + '\t\t\t\t' + str(int(100*i/num_events)) + '%')
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
            write_successful = False
            while not write_successful:
                try:
                    sf.write(join(output_path, track.name + '.wav'), output_buffer, fs)
                    write_successful = True
                    if VERBOSE: print('Write Successful')
                except:
                    print('Silly Sequencer cannot access file: ' + output_path)
                    print('This may be caused because the file is in use, Silly Sequencer does not have the correct permission to create the file or because the track\'s name in not a valid filename.')
                    print('If the issue was caused by a permission or use problem, press enter once the problem has been resolved to resume execution.')
                    print('If the tracks\'s name is not a valid filename, please enter a new name below and then press enter.')
                    print('Press ctrl+c to abort execution.')
                    ip = input()
                    if ip != '':
                        track.name = ip 