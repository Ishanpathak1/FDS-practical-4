import numpy as np
import pandas as pd
dict1={
    'name':['Ishan','Vedant','Dhara','Dhruvi','Vishal'],
    'sales':[10000,20000,20500,15000,14000],
    'quarter':[2,4,4,3,1],
    'country':['India','USA','Canada','Australia','Srilanka']
}
df = pd.DataFrame(dict1, columns= ['name','sales','quarter','country'] )
print (df)


pivot = df.pivot_table(index=['name'], values=['sales'], aggfunc='sum') 
print(pivot)
print("\n")
pivot1 = df.pivot_table(index=['country'], values=['sales'], aggfunc='sum')
print (pivot1)
print("\n")
pivot2 = df.pivot_table(index=['name','country'], values=['sales'], aggfunc= 'sum')
print (pivot2)
print("\n")
pivot3 = df.pivot_table(index=['country'], values=['sales'], aggfunc='max')
print (pivot3)
print("\n")
pivot4 = df.pivot_table(index=['country'], values=['sales'], aggfunc={'median','mean','min'})
print (pivot4)