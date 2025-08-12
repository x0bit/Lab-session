import pandas as pd

s1 = pd.Series([1,3,5,7,9])
s2 = pd.Series([2,4,6,8,10])

sum = s1+s2
print("\nsum of 2 series")
print(sum)

sub = s1 - s2
print("\nsubscration of 2 series")
print(sub)

multi = s1*s2
print("\nMiltipliction of 2 series")
print(multi)

div = s1*s2
print("\nivistion of 2 series")
print(div)
