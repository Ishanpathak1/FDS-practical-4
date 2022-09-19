import numpy as np
import pandas as pd
dict1={
    'fname':['Ishan','Vedant','Ishan','Dhruvi','Vishal'],
    'mname':['Dushyant','Amit','Piyush','Rahul','Kashyap'],
    'lname':['Pathak','Shah','Patel','Mehta','Bagga']
}
df=pd.DataFrame(dict1)
a=df.drop_duplicates()
print(a)
print('\n')
b=df.drop_duplicates(subset=['fname'])
print(b)