#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     06/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Matplot library in python-------------
from matplotlib import pylab
print(pylab.__version__);

''' use Numpy to generate random data'''

import numpy as np
x=np.linspace(0,10,25);
y=x*x+2;
print(x);
print(y);
print(np.array([x,y]).reshape(25,2).reshape(2,25));

'''Its only takes one line command to draw'''
print(pylab.plot(x,y,'r')); #'r' stads for red color line.
#pylab.show();
'''Drawing a subgraph'''
print(pylab.subplot(1,2,1));#The bracket parameter represent(rows,columns,indexes);
print(pylab.plot(x,y,'g--'));#last parameter represent color and style...
print(pylab.subplot(1,2,2));
print(pylab.plot(y,x,'r*-'));
pylab.show()#show function are used to show graph

print(pylab.subplot(1,2,1));
print(pylab.plot(x,y,'g--'));
print(pylab.subplot(1,2,1));
print(pylab.plot(y,x,'r--'));
pylab.show();