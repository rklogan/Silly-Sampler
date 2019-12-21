# Silly-Sequencer
Silly Sequencer assigns a random sample to each note of each channel of a MIDI file and output the resulting audio file. The samples are pitch shifted to the note specified in the MIDI file. Silly Sequencer is written in Python and is cross-platform.

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

TODO



--- 

## Built With

* [LibROSA](https://librosa.github.io/librosa/) - Used for audio analysis
* [Mido](https://mido.readthedocs.io/en/latest/) - Used to parse MIDI
* [NumPy](https://numpy.org/) - Required for other dependencies
* [SoundFile](https://pysoundfile.readthedocs.io/en/latest/) - Used for writing audio files

---

## Example Samples Source
The provided test tones were generated using audiocheck.net's ['Sine Tone Generator'](https://www.audiocheck.net/audiofrequencysignalgenerator_sinetone.php).  
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

## License
Copyright <2019> <Ryan Logan>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.