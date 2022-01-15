import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
df=pd.read_csv('kyphosis.csv')
print(df.head())
#sns.pairplot(df, hue='Kyphosis')
#plt.show()
X=df.drop('Kyphosis', axis=1)
y=df['Kyphosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)
predictions = dtree.predict(X_test)
print(predictions)
print(classification_report(y_test, predictions))
print("\n")
print(confusion_matrix(y_test, predictions))
print(accuracy_score(y_test, predictions)*100,"%")
print("\n")
print("\n")
print("\n")
rfc= RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)
rfc_pred= rfc.predict(X_test)
print(classification_report(y_test, rfc_pred))
print("\n")
print(confusion_matrix(y_test, rfc_pred))
print(accuracy_score(y_test, rfc_pred)*100,"%")
