"""
Get a list of the data files for each instrument.

Each datapoint will be a dictionary that has keys for at least "instrument" and some basic info like samplerate and a signal derived from its frames:
{
    instrument:  string,
    signal:      [int],
    samplerate:  int,
    samplewidth: int,
    nframes:     int,
    sigstr:      string,
    path:        string
}

getSplitData returns a dict that looks like this:
{
    train: [datapoints],
    test:  [datapoints]
}

getAllData returns a list of datapoint dicts following the shape above.
"""
import aifc
import struct
import glob
import random
import numpy as np
from sklearn.preprocessing import StandardScaler

INSTRUMENTS = ["AltoFlute", "Basoon", "BassClarinet", "BassFlute", "BassG", "BassTrombone", "BbClarinet", "CelloG", "EbClarinet", "flute", "Horn", "oboe", "saxaphone", "SopSax", "TenorTrombone", "trumpet", "Tuba", "ViolaG", "ViolinG"]
INSTRUMENT_CATEGORIES = {
    "woodwind": ["BbClarinet", "BassClarinet", "BassFlute", "AltoFlute", "flute", "Basoon", "EbClarinet", "oboe"],
    "brass": ["trumpet", "BassTrombone", "Horn", "saxaphone", "SopSax", "TenorTrombome", "Tuba"],
    "strings": ["CelloG", "ViolaG", "ViolinG", "BassG"]
}
# These should add up to 1.0
TRAIN_PERCENT = 0.80
TEST_PERCENT = 0.20

def getSplitData(num=None):
    # Split up all of the data into train and test portions
    d = getAllData(num)

    random.seed(0)
    random.shuffle(d)

    train_cutoff = int(len(d) * TRAIN_PERCENT)
    splitData = {
        "train": d[:train_cutoff],
        "test": d[train_cutoff:]
    }
    return splitData

def getAllData(num=None):
    # Return all datapoints as dicts in a single list
    data = []
    instruments = INSTRUMENTS
    random.shuffle(instruments)
    if num:
        instruments = instruments[:num]
    print instruments
    for instrument in instruments:
        for fpath in getPathsByInstrument(instrument):
            audio = aifc.open(fpath)

            datapoint = {
                "instrument":  instrument,
                "path":        fpath,
                "nframes":     audio.getnframes(),
                "samplewidth": audio.getsampwidth(),
                "samplerate":  audio.getframerate()
            }

            datapoint["sigstr"] = audio.readframes(datapoint["nframes"])
            datapoint["signal"] = getSignalArray(datapoint)
            datapoint["instrument_category"] = instrumentToCategory(instrument)

            data.append(datapoint)
            audio.close()
    return data

def getPathsByInstrument(instrument):
    return glob.glob('data/' + instrument + '/*.aif')

def instrumentToCategory(instrument):
    for k in INSTRUMENT_CATEGORIES:
        if instrument in INSTRUMENT_CATEGORIES[k]:
            return k
    print "Unexpected instrument category encountered!"
    return "unknown category"

def getSignalArray(datapoint):
    # from https://www.kaggle.com/c/whale-detection-challenge/discussion/3794
    return np.fromstring(datapoint["sigstr"], np.short).byteswap()

if __name__ == "__main__":
    allData = getAllData()
    splitData = getSplitData()
