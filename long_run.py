from getdata import getSplitData
from getlabels import instrumentsToLabels
from featurize import mfcc_averages
from sklearn.multiclass import OneVsOneClassifier
from perceptron import *
import numpy as np
import sys
#generate data

for x in range(6):
    for y in range(2,19):
        splitData = getSplitData(y)
        labels = instrumentsToLabels(splitData)
        features = mfcc_averages(splitData)
        if x == 1:
            print "svm", y
            p = svm(features, labels)
        elif x == 2:
            print "randomforest", y
            for z in range(5):
                p = randomforest(features, labels)
        elif x ==3:
            print "bayes", y
            p = bayes(features, labels)
        elif x == 4:
            print "neuralnet", y
            for z in range(5):
                p = neuralNet(features, labels)
        elif x == 5:
            print "knn", y
            p = knn(features, labels)
        else:
            print "perceptron", y
            for z in range(5):
                p = perceptron(features, labels)
