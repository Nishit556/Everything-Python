import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
loans=pd.read_csv('loan_data.csv')
print(loans.head())
# plt.figure(figsize=(10,6))
# loans[loans['credit.policy']==1]['fico'].hist(bins=35,color='blue',label='Credit Policy=1', alpha=0.6)
# loans[loans['credit.policy']==0]['fico'].hist(bins=35,color='red',label='Credit Policy=0', alpha=0.6)
# plt.legend()
# plt.xlabel('Fico Score')
# #####
# plt.figure(figsize=(10,6))
# loans[loans['not.fully.paid']==1]['fico'].hist(bins=35,color='blue',label='not.fully.paid=1', alpha=0.6)
# loans[loans['not.fully.paid']==0]['fico'].hist(bins=35,color='red',label='not.fully.paid=0', alpha=0.6)
# plt.legend()
# plt.xlabel('Fico Score')
# ###
# plt.figure(figsize=(11,7))
# sns.countplot(x='purpose', hue='not.fully.paid',data=loans,palette='Set1')
# ###
# plt.figure(figsize=(11,7))
# sns.jointplot(x='fico', y='int.rate', data=loans, color='purple')
# ###
# plt.figure(figsize=(11,7))
# sns.lmplot(x='fico', y='int.rate', data=loans,hue='credit.policy', col='not.fully.paid',palette='Set2')
# plt.show()
###
cat_feats= ['purpose']
final_data=pd.get_dummies(loans,columns=['purpose'],drop_first=True)
print(final_data.head())



X=final_data.drop('not.fully.paid', axis=1)
y=final_data['not.fully.paid']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
sc= StandardScaler()
X_train= sc.fit_transform(X_train)
X_test= sc.transform(X_test)
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
