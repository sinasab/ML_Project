from sklearn.multiclass import OneVsOneClassifier
import numpy as np
import sys

def perceptron(features, labels):
    from sklearn.linear_model import Perceptron
    p = OneVsOneClassifier(Perceptron(
        n_iter=200,
        # verbose=True,
        # n_jobs=-1, # parallelize
        shuffle=True,
        random_state=0
    ))
    p.fit(features["train"], labels["train"])
    print p.score(features["test"], labels["test"])
    return p

def svm(features, labels):
    from sklearn.svm import SVC
    p = OneVsOneClassifier(SVC(kernel='poly'))
    p.fit(features["train"], labels["train"])
    print p.score(features["test"], labels["test"])
    return p

def randomforest(features, labels):
    from sklearn.ensemble import RandomForestClassifier
    p = RandomForestClassifier(n_estimators=20)
    p.fit(features["train"], labels["train"])
    print p.score(features["test"], labels["test"])
    return p

if __name__ == "__main__":
    from getdata import getSplitData
    from getlabels import instrumentsToLabels
    from featurize import mfcc_averages
    splitData = getSplitData()
    labels = instrumentsToLabels(splitData)
    features = mfcc_averages(splitData)
    if len(sys.argv) == 2:
        classifier = int(sys.argv[1])
        if classifier == 1:
            p = svm(features, labels)
        elif classifier == 2:
            p = randomforest(features, labels)          
        else:
            p = perceptron(features, labels)
    else:
        p = perceptron(features, labels)
