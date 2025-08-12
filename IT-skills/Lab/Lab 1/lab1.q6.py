import pandas as pd

data = pd.Series([25000,12000,8000,5000] , index=['A' ,'B' ,'C' ,'D'])

print("\nBefore:")
print(data)

data.loc['D'] = 7000

print("\nAfter:")
print(data)
