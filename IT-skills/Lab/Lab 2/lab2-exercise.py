# this is the re-testing of lab-02 exercise 
# slide 3-4

#Q1

import pandas as pd
import numpy as np

data = {
    'x':[10,20,30,40,50],
    'y':[19,29,39,49,59],
    'z':[90,90,90,90,90]
}

df = pd.DataFrame(data)
# print(df)

#q2
score_broad = {
    'name' : ['vraj','harsh','jatin','meet','mehul','umang','harshil','karan'],
    'score' : [12,5,2,np.nan,4,5,6,8],
    'attempts' : [1,22,1,1,31,4,6,1],
    'qualify':['yes','no','yes','no','yes','no','yes','no']

}
labels =['a','b','c','d','e','f','g','h']

df2 = pd.DataFrame(score_broad , index=labels)
# print(df2)

#q3
# print(df2.head(3))

#q4
print("\n")
# print(df2[['name','score']])

#q5
# print(df2.loc[['a','b','c'],['name','score']])


#q6
# print(df2[df2['attempts'] > 2])

#q7
# print(f"Rows : {df2.shape[0]}\nColumns: {df2.shape[1]}")

#q8
# print(df2[df2['score'].isna()])

#q9 change name
# chnageName = df2.loc[df2['name'] == 'harsh' ,'name'] = 'callPagalu'
# print(chnageName)
# print(df2)

#q10
# df2['Grade'] = ['A', 'C', 'B', 'B', 'C', 'A', 'B', 'C']
# print(df2)

# #q11
# clm_list = list(df2.columns)
# print(clm_list)

#q12
# print(df2.index)
# nameAsIndex = df2.set_index('name')
# print(nameAsIndex)

#q13
# df2_int_index = df2.copy()
# df2_int_index.index = pd.Index([np.int64(i) for i in range(len(df2))])
# print(df2_int_index.index)

# # Using floating-point numbers as index
# df2_float_index = df2.copy()
# df2_float_index.index = pd.Index([float(i) + 0.5 for i in range(len(df2))])
# print(df2_float_index.index)

#q14

# names = df2['name']

# print(names.str.upper())
# print(names.str.lower())
# print(names.str.len())

#q15
# series = pd.Series(['  hello ', ' world  ', ' pandas ', ' data  '])

# print(series.str.strip()) 
# print(series.str.lstrip()) 
# print(series.str.rstrip()) 

#q16
# rdf1 = df2.head(5)
# rdf2 = df2.tail(5)
# joined_df = pd.concat([rdf1, rdf2], axis=0)
# print(joined_df)

#q17
# new_data = [
#     {'name': 'Samantha', 'score': 15, 'attempts': 1, 'qualify': 'yes', 'grade': 'B'},
#     {'name': 'George', 'score': 7, 'attempts': 2, 'qualify': 'no', 'grade': 'D'}
# ]

# df_appended = df2._append(new_data, ignore_index=True)
# print(df_appended)

#q18
# df_left = df2[['name', 'score']]
# df_right = pd.DataFrame({'name': ['vraj', 'harsh','jatin','meet'], 'age': [23, 25, 22, 30]})

# joined_inner = pd.merge(df_left, df_right, on='name', how='inner')
# print(joined_inner)
# print(df2)