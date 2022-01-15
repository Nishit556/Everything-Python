import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv('College_Data', index_col=0)
#print(df.head())
#sns.scatterplot(x='Grad.Rate', y='Room.Board', data=df,hue='Private')
#sns.set_style('whitegrid')
#sns.lmplot(x='Outstate',y='F.Undergrad',data=df, hue='Private',
#           palette='coolwarm',height=6,aspect=1,fit_reg=False)
#sns.set_style('darkgrid')
#g = sns.FacetGrid(df,hue="Private",palette='coolwarm',size=6,aspect=2)
#g = g.map(plt.hist,'Outstate',bins=20,alpha=0.7)
#g = sns.FacetGrid(df,hue="Private",palette='coolwarm',size=6,aspect=2)
#g = g.map(plt.hist,'Grad.Rate',bins=20,alpha=0.7)
print(df[df['Grad.Rate'] > 100])
df['Grad.Rate']['Cazenovia College'] = 100
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2)
kmeans.fit(df.drop('Private',axis=1))
def converter(cluster):
    if cluster=='Yes':
        return 1
    else:
        return 0
df['Cluster'] = df['Private'].apply(converter)
from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(df['Cluster'],kmeans.labels_))
print(classification_report(df['Cluster'],kmeans.labels_))
#plt.show()