![Alt text](UIowaLogo.png?raw=True)

# CSE 5523 Final Project

## Data

This project classifies instruments based on recordings made by the wonderful people at the University of Iowa.
The main goal of this project is to compare the performance different learning algorithms and models on the same dataset.

Each instrument has a set of `.aif` files associated with it. For example in `data/trumpet` there are files named `Trumpet.vib.ff.<pitch><octave>.stereo.aif` where the pitch is from a set of music notes and the octave is a number in [3-6].

### Features

In order to convert the data to a form that one of our algorithms can understand, we used an open source library called [python speech features](https://github.com/jameslyons/python_speech_features).
In a nutshell, this library takes an N*1 array representing an audio signal and a sample rate. It returns
an array of feature vectors calculated from the audio signal. The library is creating MFCC (Mel-frequency cepstral coefficients) vectors, which is a fancy way of saying it's creating the representation of the short-term power spectrum of a sound. This project will learn those features
to classify which instruments produces the sounds.

## Team

- [Rafah Asadi](https://github.com/cse3019)
- [Cameron Long](https://github.com/phirefly9)
- [Sina Sabet](https://github.com/sinasabet18)
- [Alex Tareshawty](https://github.com/atareshawty)
