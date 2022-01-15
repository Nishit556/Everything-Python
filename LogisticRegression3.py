from jedi.api.refactoring import inline
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pandas as pd
suv_data = pd.read_csv('suv_data.csv')
print(suv_data.head())
X= suv_data.iloc[:,[2,3]].values
y=suv_data.iloc[:,4].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
sc= StandardScaler()
X_train= sc.fit_transform(X_train)
X_test= sc.transform(X_test)
classifier= LogisticRegression(random_state=0) 
classifier.fit(X_train,y_train)
predictions= classifier.predict(X_test)
print(predictions)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(accuracy_score(y_test, predictions)*100,"%")

#plt.show()
#print(ad_data.describe())
#print(ad_data.info())
#ad_data['Age'].plot.hist(bins=30)
#plt.show()
#sns.jointplot(x="Age", y='Area Income', data=ad_data)
#sns.jointplot(x="Age", y='Daily Time Spent on Site', data=ad_data, kind='kde')
#sns.jointplot(x="Daily Time Spent on Site", y='Daily Internet Usage', data=ad_data)
#sns.pairplot(ad_data,hue='Clicked on Ad')