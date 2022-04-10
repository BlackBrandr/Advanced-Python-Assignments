from sklearn import datasets
from sklearn import model_selection
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt


boston = datasets.load_boston()
BOSTON_DATA = boston.data
BOSTON_TARGET = boston.target

BOSTON_DATA_test,BOSTON_DATA_train,BOSTON_TARGET_test,BOSTON_TARGET_train= model_selection.train_test_split(BOSTON_DATA,BOSTON_TARGET,random_state = 0)

# FITTING BOSTON DATASET
clf = Ridge(alpha=0.0001)
clf.fit(BOSTON_DATA_train, BOSTON_TARGET_train)
Ridge(alpha=0.0001, copy_X=True, fit_intercept=True, max_iter=None, normalize=False, random_state=None, solver="auto", tol=0,)

# TESTING VALUES PREDICTION
BOSTON_TARGET_pred = clf.predict(BOSTON_DATA_test)
print("TEST SCORE :", clf.score(BOSTON_DATA_test, BOSTON_TARGET_test))

# PLOTTING GRAPH
plt.scatter(BOSTON_TARGET_test,BOSTON_TARGET_pred)
plt.show()

# ADDING POLYNOMIAL PART
poly = PolynomialFeatures(2)
poly.fit(BOSTON_DATA_train)
BOSTON_DATA_train = poly.transform(BOSTON_DATA_train)
BOSTON_DATA_test = poly.transform(BOSTON_DATA_test)

clf1 = Ridge(alpha=100000)
clf1.fit(BOSTON_DATA_train, BOSTON_TARGET_train)
Ridge(alpha=100000, copy_X=True, fit_intercept=True, max_iter=None, normalize=False, random_state=None, solver="auto", tol=0)

# TEST VALUES PREDICTIONS
BOSTON_DATA_test.shape
BOSTON_TARGET_pred1 = clf1.predict(BOSTON_DATA_test)
print("TEST SCORE 2 :", clf1.score(BOSTON_DATA_test,BOSTON_TARGET_test))

# PLOTTING GRAPH
plt.scatter(BOSTON_TARGET_test, BOSTON_TARGET_pred1)
plt.show()



