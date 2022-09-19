import numpy as np
import pandas as pd
dict1={
    'fname':['Ishan','Vedant','Ishan','Dhruvi','Vishal','Aniket'],
    'mname':['Dushyant','Amit','Piyush','Rahul','Kashyap','Ashish'],
    'lname':['Pathak','Shah','Patel','Mehta','Bagga',np.NaN]
}
df=pd.DataFrame(dict1)
a=df.fillna(0)
print(a)
print('\n')
b=df['lname'].fillna(0)
print(b)