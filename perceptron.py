from sklearn.linear_model import Perceptron
import numpy as np

def perceptron(features, labels):
    p = Perceptron(
        n_iter=200,
        # verbose=True,
        # n_jobs=-1, # parallelize
        shuffle=True,
        random_state=0
    )
    p.fit(features["train"], labels["train"])
    print(p.score(features["test"], labels["test"]))
    return p

if __name__ == "__main__":
    from getdata import getSplitData
    from getlabels import instrumentsToLabels
    from featurize import mfcc_averages

    splitData = getSplitData()

    labels = instrumentsToLabels(splitData)
    features = mfcc_averages(splitData)
    p = perceptron(features, labels)
