from __future__ import print_function
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# LOADING MNIST DATASET
MNIST = datasets.load_digits()

# CONSTRUCT TRAINING AND TESTING SPLIT (%25)
(trainData,testData, trainLabels, testLabels) = train_test_split(np.array(MNIST.data), MNIST.target, test_size=0.25, random_state=42)

# TESTING (%10)
(trainData,valData , trainLabels, valLabels) = train_test_split(trainData,trainLabels,test_size=0.1, random_state=84)

# SIZE OF SPLITS
print("POINTS OF TRAINING DATA: {}".format(len(trainLabels)))
print("POINTS OF VALIDATION DATA: {}".format(len(valLabels)))
print("PINTS OD TESTING DATA: {}".format(len(testLabels)))

# INITIALIZE VALUES OF K
KEY_VALUES = range(1, 30, 2)
ACC = []

# STARTING LOOP
for k in range(1, 30, 2):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(trainData,trainLabels)

# CALCULATION AND UPDATING LIST OF ACC
    score = model.score(valData,valLabels)
    print("k=%d, accuracy=%.2f%%" % (k, score * 100))
    ACC.append(score)

# FINDING THE LARGEST ACC
i = int(np.argmax(ACC))
print("k=%d achieved highest accuracy of %.2f%% on validation data" % (KEY_VALUES[i],ACC[i] * 100))