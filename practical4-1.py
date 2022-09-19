#Aim1: Concatenate the names i.e fname,mname,lname
import numpy as np
import pandas as pd
dict1={
    'fname':['Ishan','Vedant','Dhara','Dhruvi','Vishal'],
    'mname':['Dushyant','Amit','Piyush','Rahul','Kashyap'],
    'lname':['Pathak','Shah','Patel','Mehta','Bagga']
}
df=pd.DataFrame(dict1)
df["fullname"]=df["fname"]+df["mname"]+df["lname"]
print(df)