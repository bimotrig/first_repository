from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_score
import numpy as np

# Load the digits dataset
digits = datasets.load_digits()

# Initialize the SVM classifier with a specified gamma value
clf = svm.SVC(gamma=0.001)

# Perform 5-fold cross-validation
accuracies = cross_val_score(clf, digits.data, digits.target, cv=5)

# Print the cross-validation accuracies
print(accuracies)
print("정확도(평균) = %0.3f%%, 표준편차 = %0.3f" % (accuracies.mean() * 100, accuracies.std()))