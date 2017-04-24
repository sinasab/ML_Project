"""
Our different featurizer functions. These functions will create features for different splits of data, returning a dict of all of the features.

Input to a featurizer should look like this:
{
    train: [datapoints],
    test:  [datapoints]
}

Output of a featurizer should look like this:
{
    train: [featurevectors],
    test: [featurevectors]
}

Since different audiofiles can be of different length, and the parameters are calculated over small windows, each datapoint will have different number of feature vectors. Possible ways to deal with this are to flatten the list of feature vectors by just taking the average or sum.
"""
import numpy as np
from python_speech_features import mfcc

def mfcc_averages(splitData):
    feats = mfcc_features(splitData)
    avg_feats = {
        "train": [np.average(f, axis=0) for f in feats["train"]],
        "test":  [np.average(f, axis=0) for f in feats["test"]]
    }
    return avg_feats

def mfcc_sums(splitData):
    feats = mfcc_features(splitData)
    sum_feats = {
        "train": [np.sum(f, axis=0) for f in feats["train"]],
        "test": [np.sum(f, axis=0) for f in feats["test"]]
    }
    return sum_feats

def mfcc_features(splitData):
    # input should look like {train: [datapoints], test: [datapoints]}
    features = {}
    for k in splitData:
        features[k] = []
        for dp in splitData[k]:
            feats = getOneMFCCFeatures(dp)
            features[k].append(feats)
    return features

def getOneMFCCFeatures(datapoint):
    # TODO I'm not sure if I should be messing with the winlen and winstep params for this, see https://github.com/jameslyons/python_speech_features#mfcc-features
    return mfcc(
        signal=datapoint["signal"],
        samplerate=datapoint["samplerate"]
    )
