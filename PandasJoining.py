import pandas as pd
#Joining

a = pd.DataFrame({'Int rate': [2, 3, 2, 2], 'USA GDP(thousands)': [50, 55, 65, 55,]},
                 index = [2001, 2002, 2003, 2004])
b = pd.DataFrame({'Low Tier HPI': [80, 85, 88, 85], 'Unemployment(%)': [1, 3, 4, 5]},
                 index = [2001, 2002, 2003, 2004])
joined = a.join(b)
print(joined)
