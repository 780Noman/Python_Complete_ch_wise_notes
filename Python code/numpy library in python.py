#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     01/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Numpy library in python-----
import numpy as np

a=np.array([1,2,3]);
print(a)
print(a.shape);
print(type(a))
print(a[1]);
import time
import sys

##print("System version...");
##print(sys.version);
##print("System information...");
##print(sys.int_info);

b=range(1000);
print(sys.getsizeof(5)*len(b));

c=np.arange(1000);
print(c.size*c.itemsize);
size=100000;

l1=range(size);
l2=range(size);
A1=np.arange(size);
A2=np.arange(size);

start=time.time();
result=[(x+y) for x,y in zip(l1,l2)];
print(result);
print("Python list took :",(time.time()-start)*1000);

start=time.time();
result=A1 + A2;
print("Numpy array took :",(time.time()-start)*1000);

#Basic operation on array using numpy ----------------------------------
a=np.array([[1,2],[1,4],[5,6]]);
print(a)
print(a.dtype)
print(a.ndim)
print(a.itemsize)
print(a.shape)

a=np.array([[1,3,4],[5,3,3]],dtype=np.float64);
print(a)
print(a.itemsize)
print(a.shape)

a=np.array([[3,4,5],[4,2,6]],dtype=np.complex)
print(a)

#print 2d array of 0
print(np.zeros((2,2)))

#print 2d array of 1
print(np.ones((2,3)))

#Range ---------------
l=range(5);
print(l);

#Range of numpy array.
print(np.arange(5))

#Concatination Example-------------

print("\nConcatination Example...:");
print(np.char.add(['hello','hi'],[' world',' xyz']));

print(np.char.multiply('hello',3));#its take 2 argument/

print(np.char.center('hello',20,fillchar='*'));#e.g *******hello****

print(np.char.title("how are you doing?"));#taking a title

print(np.char.lower(['HELLO','WORLD']))#array in lowercase

print(np.char.lower('HI, HOW ARE YOU.'));#convert lowercase

print(np.char.upper(['python','file']));#array in uppercase

print(np.char.upper('coding'));

print(np.char.capitalize("are you muslim."));#capitalizing first letter.

print(np.char.split("Ali is a good boy."));#spliting into words

print(np.char.splitlines("Hello,\n Are you ready."))#split in to line

print(np.char.strip(['admin','aima','alyan'],'a'))#Remving a letter first & last

print(np.char.join([':',','],['12022','hi']))#join two array togater.

print(np.char.replace("He is good boy.",'is','was'));