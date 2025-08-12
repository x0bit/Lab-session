import pandas as pd

data = pd.Series([300, 1200, 17400, 100])
filtered = data[data > 200]
print(filtered)
