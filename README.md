![Alt text](UIowaLogo.png?raw=True)

# CSE 5523 Final Project

Full writeup available at https://github.com/sinasabet81/ML_Project/blob/master/ML%20Report.pdf

## Data

This project classifies instruments based on recordings made by the wonderful people at the University of Iowa.
The main goal of this project is to compare the performance different learning algorithms and models on the same dataset.

Each instrument has a set of `.aif` files associated with it. For example in `data/trumpet` there are files named `Trumpet.vib.ff.<pitch><octave>.stereo.aif` where the pitch is from a set of music notes and the octave is a number in [3-6].

### Features

In order to convert the data to a form that one of our algorithms can understand, we used an open source library called [python speech features](https://github.com/jameslyons/python_speech_features).
In a nutshell, this library takes an N*1 array representing an audio signal and a sample rate. It returns
an array of feature vectors calculated from the audio signal. The library is creating MFCC (Mel-frequency cepstral coefficients) vectors, which is a fancy way of saying it's creating the representation of the short-term power spectrum of a sound. This project will learn those features
to classify which instruments produces the sounds.
However, each audio file creates an array of feature vectors as a coefficient vector is created for every sample of the signal.
Because each file is of different length, each file produces a different sized coefficient matrix. Our solution to this
is to average the coefficients produced for each audio file. That way each audio file is one datapoint

## Algorithms

In the file `algorithms.py`, you'll find each of the algorithms used to learn our audio data. The file `long_run.py`
shows the script run to get the data used for the results found in the paper.

## To Run

To collect the data and see the algorithms produce results:

- Download the data from [University of Iowa's site](http://theremin.music.uiowa.edu/MIS.html)
- Install the following packages:
  - [Numpy/Scipy](https://www.scipy.org/)
  - [sklearn](http://scikit-learn.org/)
  - [python_speach_features](https://github.com/jameslyons/python_speech_features)
  
- Make sure the data is in this structure:

      ```
      +-- data/
      |   +-- trumpet/
      |   |   +-- Trumpet.vib.ff.A3.aif
      |   +-- brass/
      |   |   +-- Trumpet.vib.ff.A3.aif
      |   |   +-- ... (other brass instrument files)
      |   +-- strings/
      |   +-- woodwinds/
      +-- _site
      +-- index.html
      ```

      Where under each instrument directory is a flat structure of all the audio files.

      The brass instruments are:
      - Trumpet
      - Horn
      - Tenor Trombone
      - Bass Trombone
      - Tuba

      Woodwinds are:
      - Alto Flute
      - Alto Saxophone
      - Bass Clarinet
      - Bassoon
      - B flat Clarinet
      - E flat Clarinet
      - Oboe
      - Soprano Saxophone

      Strings are:
      - Bass
      - Cello
      - Viola
      - Violin

- After the data is correct, run `python long_run.py` and the data will print to the console

## Team

- [Rafah Asadi](https://github.com/cse3019)
- [Cameron Long](https://github.com/phirefly9)
- [Sina Sabet](https://github.com/sinasabet81)
- [Alex Tareshawty](https://github.com/atareshawty)
