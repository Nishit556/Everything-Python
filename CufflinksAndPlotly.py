import cufflinks as cf
import pandas as pd
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import chart_studio
#import chart_studio
init_notebook_mode(connected= True)
cf.go_online()
#df
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df.head()
print(df)
df2 = pd.DataFrame({'Category':['A', 'B', 'C'], 'values': [32, 43, 50]})
print(df2)
df.plot()
