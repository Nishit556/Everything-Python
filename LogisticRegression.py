#Train a logistic regression classifier to predict whether a flower is iris verginica or not
from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
iris = datasets.load_iris()
X=iris["data"][:,3:]
y=(iris["target"]==2).astype(int)
#print(X)
#print(y)
#Train a logistic regression classifier
clf = LogisticRegression()
clf.fit(X,y)
example = clf.predict(([[2.6]]))
print(example)
#using matplotlib to plot the visualization
X_new = np.linspace(0,3,1000).reshape(-1,1)
#print(X_new)
y_prob = clf.predict_proba(X_new)
print(y_prob)
plt.plot(X_new, y_prob[:,1], "b-", label= "virginica")
plt.show()

#print(list(iris.keys()))
#print(iris['data'])
#print(iris['target'])
#print(iris['DESCR'])