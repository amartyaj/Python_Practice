#!/usr/bin/env python3

import pandas as pd

data = {'col1' : [1, 2, 3], 'col2' : [1, 2, 5], 'col3' : [1, 2, 6], 'col4' : [1, 2, 2], 'col5' : ['row1', 'row2', 'row3']}
df = pd.DataFrame(data)

Q1 = 0
Q3 = 0
outlier_columns = []

# print(df)

for column in df.columns:
    # print(column)
    if df[column].dtype != 'object':
        Q1 = df[column].quantile(.25)
        Q3 = df[column].quantile(.75)
        IQR = Q3 - Q1
        upper_bound = Q3 + (1.5 * IQR)
        lower_bound = Q1 - (1.5 * IQR)
        total_rows = len(df)
        rows_outside_bounds = len(df[column][(df[column] < lower_bound) | (df[column] > upper_bound)])
        percent_outside_bounds = (rows_outside_bounds / total_rows) * 100
        if percent_outside_bounds > 11:
            outlier_columns.append(column)
    # print(f"{Q1} : {Q3} : {IQR} : {lower_bound} : {upper_bound}")

df.drop(outlier_columns, axis=1, inplace=True)    
print(df)
# df = pd.read_csv('data.txt')

