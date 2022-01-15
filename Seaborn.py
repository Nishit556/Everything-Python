import seaborn as sns
#import pandas as pd
#import matplotlib.pyplot as plt

a = sns.load_dataset("flights")
#df = pd.DataFrame(a)
#df.set_index('year', inplace=True)
#print(df)
#df.plot()
#plt.show()
sns.relplot(x= "passengers", y="month",hue='year', data=a)

