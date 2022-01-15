from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
cancer = load_breast_cancer()
#print(cancer.keys())
#print(cancer['DESCR'])
df_feat= pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
print(df_feat.head())
print(cancer['target'])
X=df_feat
y=cancer['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#sc= StandardScaler()
#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)
model = SVC()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(predictions)
print(confusion_matrix(y_test, predictions))
print("\n")
print(classification_report(y_test, predictions))
print(accuracy_score(y_test, predictions)*100,"%")
