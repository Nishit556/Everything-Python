import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
df = pd.DataFrame( {'Day': [1, 2, 3, 4, 5, 6],
           'Visitors': [1000, 700, 6000, 1000, 400, 350],
           'Bounce Rate': [100, 20, 30, 40, 50, 0]
           })
df.set_index('Day', inplace= True)
df = df.rename(columns={'Visitors':'Users'})
print(df)
df.plot()
plt.show()
