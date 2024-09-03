#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     04/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Pandas Series
#--Series is a one-dimensional array with labels. It can contain any data type including interges strings floats,Python and more.
import pandas as pd
#check pandas verion
print(pd.__version__);

#Series Create ,manipulate,Querry,Delete......

#Creating a series from a list.
arr=[0,1,2,3,4,5];
s1=pd.Series(arr);
print(s1);

order=[1,2,3,4,5,6]
s2=pd.Series(arr,index=order);
print(s2);

import numpy as np
n=np.random.randn(5)#Create a random Ndarray
print(n)

index=['a','b','c','d','e'];
s2=pd.Series(n,index=index);
print(s2);

#Create series from dictionary
d={'a':1,'b':2,'c':3,'d':4};
s3=pd.Series(d);
print(s3);

#You can modify the index of series
print(s1);
s1.index=['A','B','C','D','E','F'];
print(s1);

#slicing the Series .
a=s1[:-1];
print(a);

#Appending the two series.
s4=s3.append(s1)
print(s4);

#Droping index from Series.
print(s4.drop('F'));

#Series operation---------------------------
arr1=[0,1,2,3,4,5,7];
arr2=[6,7,8,9,5];
s5=pd.Series(arr2);
print(s5);

s6=pd.Series(arr1);
print(s6);

#Mathematics operation (+,-,/)
print(s5.add(s6));
print(s5.sub(s6));
print(s5.div(s6));

#Find median max and min values.
print('Median is :',s6.median());
print('Max is :',s6.max());
print('Min is : ',s6.min());

#Create data frame in pandas library.
dates=pd.date_range('today',periods=6); #Define time sequence as index
print(dates);

num_arr=np.random.randn(6,4);#Import numpy random array .
columns=['A','B','C','D'];#USe the table as the column name.

df1=pd.DataFrame(num_arr,index=dates,columns=columns);
print(df1);

#Create dataframe with dictionary array.
data={'animal':['cat','snake','dog','cat','elephant','cow','tiger','fox'],
    'age':[3.5,6,0.2,np.nan,8,6.4,np.nan,5],
    'priority':['yes','no','yes','yes','no','yes','no','no']};
labels=['a','b','c','d','e','f','i','j'];
df2=pd.DataFrame(data,index=labels);
print(df2);

#See datatype of array.
print(df2.dtypes)

#Head function.....
df3=df2.head(6);
print(df3);

#Tail function using extract last index values......
print(df2.tail(3));

#Print index and column,values of Dataframe.
print(df2.index);
print(df2.columns);
print(df2.values);

#Show statistical data of dataframe.
print(df2.describe())

#Tranport vertical to horizontal the dataframe...
print(df2.T)

#Sorting value in dataframe ....
print(df2.sort_values(by='age'));

#Silicing dataframe-------------------
print(df2[0:6]);#a,b,c are are index of the dataframe..

#Query dataframe by tag-------------------
print(df2[['age','priority']])

#Query rows 2,3----------------
print(df2.iloc[1:3]);

#Copying of dataframe 1 to other...............
df3=df2.copy();
print(df3);

#When you want to null dataframe then--------------
print(df3.isnull());

#When you change a value in datafrome-----------
df3.loc['f','age']=5.6;
print(df3);

#Some logical operation of dataframe value-----------
print(df3.mean())

print(df3['age'].max());

print(df3['age'].min());

print(df3['age'].sum());#Other method of sum...

print(df3.sum());#All column sum are show here.

#String in dataframe in pandas library...
string=pd.Series(['AA','B','COW',np.nan,'BBA','OWL']);
print(string);

#some operation on pandas string............
print(string.str.lower());
print(string.str.upper());

#Operations for Datafrome missing values............
df4=df3.copy();
print(df4);

print(df4.fillna(4));#Print missing value in rows & columns

df5=df3.copy();
#Removing these row that has contain missing values------
print(df5.dropna(how='any'));

#File operation on dataframe-------------------
df3.to_csv('animal.csv');

df_animal=pd.read_csv('animal.csv');
print(df_animal.head(4));

##df3.to_excel('animal.dat',sheet_name='Sheet1');
##df_animal2=pd.read_excel('animal.dat','Sheet1',index_col=None ,na_values=['NA']);
##print(df_animal2);



