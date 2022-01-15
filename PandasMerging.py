import pandas as pd
#Merging

a = pd.DataFrame({'HPI': [80, 85, 88, 85], 'Int rate': [2, 3, 2, 2], 'USA GDP(thousands)': [50, 55, 65, 55,]}, index = [2001, 2002, 2003, 2004])
b = pd.DataFrame({'HPI': [80, 85, 88, 85], 'Int rate': [2, 3, 2, 2], 'USA GDP(thousands)': [50, 55, 65, 55,]}, index = [2005, 2006, 2007, 2008])
m = pd.merge(a, b, on = 'HPI')
print(m)