import numpy as np
import pandas as pd

np_ary = np.array([10,20,30,40,50])
print("NumPy array :\n", np_ary)

new_series = pd.Series(np_ary)
print("Converted Pandas Series:\n" , new_series)
