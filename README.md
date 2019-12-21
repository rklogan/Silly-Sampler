# Silly-Sequencer
Silly Sequencer assigns a random sample to each note of each channel of a MIDI file and outputs the resulting audio file. The samples are pitch shifted to the note specified in the MIDI file. Silly Sequencer is written in Python and is cross-platform.

---

## Why do this?
Because we can. (And for fun)

---

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites
#### Python 3.x
Installation instructions can be found [here](https://docs.python.org/3/using/index.html)

#### pip
While pip is not strictly required to run this project, the installation instructions contained here will use it. References to the dependency's developer's instructions will be included if you do not wish to install pip. Installation instructions can be found [here](https://pip.pypa.io/en/stable/installing/)

#### NumPy
NumPy can be installed using pip as follows:
```bash
pip install numpy
```
Otherwise, consult [this link](https://docs.scipy.org/doc/numpy/user/install.html) for further instructions.

#### Mido
Mido is a library for working with MIDI messages and ports. It can be installed with pip as follows:
```bash
pip install Mido
```
Otherwise, you can consult the [Mido documentation](https://mido.readthedocs.io/en/latest/index.html)

#### LibROSA
LibROSA is a python package for music and audio analysis. It can be installed with pip as follows:
```bash
pip install librosa
```
Alternative installation instructions can be found [here](https://librosa.github.io/librosa/install.html)

#### SoundFile
SoundFile can read and write sound files. It can be installed with pip as follows:
```bash
pip install PySoundFile
```
On Linux, you will additionally need to install libsndfile. Depending on your package manager this can be done with:
```bash
sudo apt-get install libsndfile1
```
You can consult the [SoundFile documentation](https://pysoundfile.readthedocs.io/en/latest/#installation) for further information.

### Installing
Once the prerequisites are intalled, no further installation is required.

---

## Usage

### Provided Example
To run the provided example simply run the following in the top level directory of the repository:
```bash
python Silly_Sequencer.py
```
or
```bash
python3 Silly_Sequencer.py
```
depending on your alias configuration.  
  
This will run Silly Sequencer with it's default parameters. It may take a minute for Silly Sequencer to complete it's execution, but will provide updates on the terminal as it progresses. Upon completion an audio file will be created for each track that was used in the MIDI example. In this case, it will generate three audio files that, when played together, will play the first 45 seconds of Queen's Bohemian Rhapsody.

### General Usage

```bash
python Silly_Sequencer.py [sample_directory] [score] [output_directory] [gain] [verbose]
```
* **sample_directory**: The relative path to the directory containing the samples. To recreate the example, a value of 'Samples' (without quotation marks) could be used.
* **score**: The relative path to the MIDI file that is to be processed. To recreate the example, a value of 'score.mid' (without quotation marks) could be used.
* **output_directory**: The relative path to the directory to which the output audio should be written. Should the directory not exist, it will be created. Should it already contain audio files that match the track names of the MIDI file being process they will be **OVERWRITTEN**. To recreate the example, a value of 'Output' (without quotation marks) could be provided.
* **gain**: This is the gain factor applied to all the samples. By default it is 0.2. Depending on the MIDI file being processed, and the number of samples that are playing simultaneously this may need to be adjusted to avoid clipping.
* **verbose**: If a value of 'f', 'F', or 'False' is provided in this position, Silly Sequencer will only update the console if an error has occured. That is to say, it will not report it's progress on the terminal.  

All parameters listed above are positional and must be provided in the order presented above. Should the user wish to use later parameters without using earlier ones a value of 'None' can be passed to indicate to Silly Sequencer that the parameter should be ignored. For example:
```bash
python Silly_Sequencer.py None None new_output_directory
```
would use the default parameters for sample_directory, score, gain and verbose, but would instead write the output values to new_output_directory.

### General Notes
* Silly Sequencer produces rather chaotic music. Sample choice greatly effects the musicality of the output. For instance, in the provided example the gunshot sound effects are not noticeably effected by the pitch shifting and result, for the most part, in destroying the melodic structure (however amusing it might be).
* Silly Sequencer will automatically select the sample rate for the audio files to be the same as the sample rate of the sample whose file name is first lexicographically. As such, all samples should have the same sample rate to avoid erroneous behaviour.
* Silly Sequencer will work with mono and stereo samples. It has not been tested with samples that have more than two channels.
* If the Samples directory provided does not exist, the program will fail. Furthermore if the Samples directory is empty the program will also fail. Finally, the samples directory must contain **EXCLUSIVELY** audio files. The presence of any other type of file will cause failure. As per the limitations of the dependency _SoundFile,_ Silly Sequencer fully supports WAV, FLAC and MAT files and has limited support for OGG files. See the [SoundFile documentation](https://pysoundfile.readthedocs.io/en/latest/#read-write-functions) for more details.
* This version of Silly Sequencer does not acknowledge _Note Off_ events, nor does it respond to _Note On_ events with a velocity of 0 (which both usually indicate that the note should stop playing). When Silly Sequencer recieves a _Note On_ event with non-zero velocity, it will play the entire sample, stopping only if the end point of the song has been reached.
* There are a few scenarion where writing the audio files can fail:  
  * The files are already in use by another program. This could arise if the user was trying to overwrite the output of a previous run of Silly Sequencer after having imported them into their DAW.
  * Silly Sequencer does not have write access to the specified directory.  
  
  In both of these cases, Silly Sequencer will try to perform the write every 30 seconds until it is either successful or the user terminates the process with 'ctrl+c'. This allows the user to rectify the situation without having to restart the processing.

---

## Built With

* [LibROSA](https://librosa.github.io/librosa/) - Used for audio analysis
* [Mido](https://mido.readthedocs.io/en/latest/) - Used to parse MIDI
* [NumPy](https://numpy.org/) - Required for other dependencies
* [SoundFile](https://pysoundfile.readthedocs.io/en/latest/) - Used for writing audio files

---

## Example Samples Source
The provided test tones were generated using audiocheck's ['Sine Tone Generator'](https://www.audiocheck.net/audiofrequencysignalgenerator_sinetone.php).  
The MIDI file used in the example is a cropped version of the file found [here](https://bitmidi.com/queen-bohemian-rhapsody-mid).

Listed below is the source for the samples used in the example:  
* [Air_Wrench_Short-Lightning_McQue-2139303794.wav](http://soundbible.com/1975-Air-Wrench-Short.html) - **Lightning McQue**
* [Cow_Moo-Mike_Koenig-42670858.wav](http://soundbible.com/1778-Cow-Moo.html) - **Mike Koenig**
* [fire_bow_sound-mike-koenig.wav](http://soundbible.com/2108-Shoot-Arrow.html) - **Mike Koenig**
* [Guillotine-SoundBible.com-1694495814.wav](http://soundbible.com/1532-Guillotine.html) - **Mike Koenig**
* [Kid_Laugh-Mike_Koenig-1673908713.wav](http://soundbible.com/2026-Kid-Laugh.html) - **Mike Koenig**
* [M16 Short Burst-SoundBible.com-1461274012](http://soundbible.com/1374-M16-Short-Burst.html) - **snottyboi**
* [male_cough-Mike_Koenig-144979711.wav](http://soundbible.com/1864-Male-Cough.html) - **Mike Koenig**
* [MP5_SMG-GunGuru-703432894.wav](http://soundbible.com/2091-MP5-SMG-9mm.html) - **GunGuru**
* [neck_snap-Vladimir-719669812.wav](http://soundbible.com/1953-Neck-Snap.html) - **Vladimir**
* [Pew_Pew-DKnight556-1379997159.wav](http://soundbible.com/1949-Pew-Pew.html) - **DKnight556**
* [Short-Dial-Tone-SoundBible.com-1911037576.wav](http://soundbible.com/1118-Short-Dial-Tone.html) - **Mike Koenig**
* [short_male_burp-Mike_Koenig-832127430.wav](http://soundbible.com/1867-Short-Male-Burp.html) - **Mike Koenig**
* [Train_Honk_Horn_Clear-Mike_Koenig-1632487478.wav](http://soundbible.com/1696-Train-Honk-Horn-Clear.html) - **Mike Koenig**

---

## Authors

* **Ryan Logan** - *Development* [Silly Sequencer](https://github.com/rklogan/Silly-Sampler)

---

## MIT License
Copyright <2019> <Ryan Logan>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
