#sorting of the data in the given data frame
import numpy as np
import pandas as pd
dict1={
    'rollno':[42,50,32,28,18],
    'fname':['Ishan','Vedant','Dhara','Dhruvi','Vishal'],
    'mname':['Dushyant','Amit','Piyush','Rahul','Kashyap'],
    'lname':['Pathak','Shah','Patel','Mehta','Bagga']
}
df=pd.DataFrame(dict1)

df.sort_values(by='rollno',inplace=True,ascending=False)
print(df)