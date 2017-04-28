from sklearn.multiclass import OneVsOneClassifier
import numpy as np
import sys

def perceptron(features, labels):
    from sklearn.linear_model import Perceptron
    p = Perceptron(
        n_iter=200,
        # verbose=True,
        n_jobs=-1, # parallelize
        shuffle=True,
        random_state=0
    )
    p.fit(features["train"], labels["train"])
    print p.score(features["test"], labels["test"])
    return p

def knn(features, labels):
    from sklearn.neighbors import KNeighborsClassifier
    p = KNeighborsClassifier(3)
    p.fit(features["train"], labels["train"])
    print p.score(features["test"], labels["test"])
    return p

def neuralNet(features, labels):
    from sklearn.neural_network import MLPClassifier
    p = MLPClassifier(max_iter=1000, solver='lbfgs', hidden_layer_sizes=(100))
    p.fit(features["train"], labels["train"])
    print p.score(features["test"], labels["test"])
    return p

def bayes(features, labels):
    from sklearn.naive_bayes import GaussianNB
    p = OneVsOneClassifier(GaussianNB())
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
    from getlabels import instrumentsToLabels, categoryToLabels
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
        elif classifier ==3:
            p = bayes(features, labels)
        elif classifier == 4:
            p = neuralNet(features, labels)
        elif classifier == 5:
            p = knn(features, labels)        
        else:
            p = perceptron(features, labels)
    else:
        p = perceptron(features, labels)
