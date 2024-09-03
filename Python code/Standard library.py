#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     31/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import numpy as np

a=np.array([1,2,3,4]);
print(a);
print(type(a));
print(a.shape);
#Arange array ---------Reshape array--------------------
b=np.arange(12).reshape(3,4);
print(b);
##from scipy import constants
##print(constants.c)#Speed of light
import pandas as pd
df=pd.DataFrame(np.random.randn(6,4),index=list(range(6)),columns=list('ABCD'));
print(df);
print(df.describe());
#Matplotlib in python-------------------
import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3];
y=[2,4,1];
plt.plot(x,y);
plt.xlabel('x-axis');
plt.ylabel('y-axis');
plt.title('My first greaph!');
plt.show();
##Create a Histogram using matplot library
from matplotlib import style
style.use('ggplot');

x=[2,4,6]
y=[12,14,16]

x2=[3,3,4];
y2=[7,14,5];
plt.bar(x,y,color='r',align='center');
plt.bar(x2,y2,color='b',align="center");

plt.title('info');
plt.ylabel('y-axis');
plt.xlabel('x-axis');
plt.show();


