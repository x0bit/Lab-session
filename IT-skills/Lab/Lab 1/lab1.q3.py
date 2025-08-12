import pandas as pd

name = input("Enter your name: ")
series_name = pd.Series(list(name))

print(series_name)
