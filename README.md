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

TODO

---

## Example Samples Source

TODO

---

## Authors

* **Ryan Logan** - *Development* [Silly Sequencer](https://github.com/rklogan/Silly-Sampler)

---

## License
Copyright <2019> <Ryan Logan>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.