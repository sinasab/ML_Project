"""
Get a list of the data files for each instrument.

Each datapoint will be a dictionary that has keys for at least "instrument" and some kind of derived features.

Logic for converting aif frames to signal array from https://www.kaggle.com/c/whale-detection-challenge/discussion/3794
"""
import aifc
import struct
import glob
import numpy as np
from python_speech_features import mfcc

INSTRUMENTS = ["flute", "trumpet"]

def getAllData():
    data = []
    for instrument in INSTRUMENTS:
        for fpath in getPathsByInstrument(instrument):
            audio = aifc.open(fpath)

            datapoint = {
                "instrument":  instrument,
                "nframes":     audio.getnframes(),
                "samplewidth": audio.getsampwidth(),
                "samplerate":  audio.getframerate()
            }

            datapoint["sigstr"] = audio.readframes(datapoint["nframes"])
            datapoint["signal"] = np.fromstring(datapoint["sigstr"], np.short).byteswap()
            datapoint["mfcc_features"] = getMFCCFeatures(datapoint)

            data.append(datapoint)
            audio.close()
    return data

def getMFCCFeatures(datapoint):
    return mfcc(
        signal=datapoint["signal"],
        samplerate=datapoint["samplerate"]
    )

def getPathsByInstrument(instrument):
    return glob.glob('data/' + instrument + '/*.aif')
