import pandas as pd

xyz_web = {'Day': [1, 2, 3, 4, 5, 6],
           'Visitors': [1000, 700, 6000, 1000, 400, 350],
           'Bounce Rate': [100, 20, 30, 40, 50, 0]
           }
df = pd.DataFrame(xyz_web)
print(df)
print("------------------------------------------------")
s = pd.Series(xyz_web)
print(s)
print("------------------------------------------------")
#slicing
print(df.head(3))
print(df.tail(3))
print("------------------------------------------------")
