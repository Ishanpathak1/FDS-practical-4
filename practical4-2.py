import numpy as np
import pandas as pd
dict1={
    'fname':['Ishan','Vedant','Dhara','Dhruvi','Vishal'],
    'mname':['Dushyant','Amit','Piyush','Rahul','Kashyap'],
    'lname':['Pathak','Shah','Patel','Mehta','Bagga']
}
df=pd.DataFrame(dict1)
df["fullname"]=df["fname"]+df["mname"]+df["lname"]
a=df.values.tolist()
print(a)
print("\n")
b=df["fname"].values.tolist()
print(b)
print("\n")
c=df["mname"].values.tolist()
print(c)
print("\n")
d=df['lname'].values.tolist()
print(d)
print("\n")
e=df['fullname'].values.tolist()
print(e)