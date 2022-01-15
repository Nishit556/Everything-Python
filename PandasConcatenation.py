import pandas as pd
#Concatenation

a = pd.DataFrame({'Int rate': [2, 3, 2, 2], 'USA GDP(thousands)': [50, 55, 65, 55,]}, index = [2001, 2002, 2003, 2004])
b = pd.DataFrame({'Int rate': [2, 3, 2, 2], 'USA GDP(thousands)': [50, 55, 65, 55,]}, index = [2005, 2006, 2007, 2008])
c = pd.concat([a, b])
print(c)