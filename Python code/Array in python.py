#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     22/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
from array import *
arr=array('i',[-1,2,7,4,5]);
print(type(arr))
print(arr);
print(arr.buffer_info())
print(arr[1]);
#Using for loop accessing each element in array.
for i in arr:
    print(i);
#using pointer in for loop to access element.
for pnt in range(1,4):
    print(pnt,arr[pnt]);
#using built in function reverse is used to revese array.
arr.reverse();
print("After reversing the given array is :",arr);
#appending the array.
arr.append(10);
print("After appending the array is :",arr);
#Removing element from array is .
arr.remove(7);
print("After removing the 7 from the array is : ",arr);
print(arr[2]);
print("Enter value in index function to find index of value :",arr.index(10));
#Enter by user size of array.
ary=array("i",[]);
print(ary);
x=int(input("Enter a size of array :"));
print("Enter %d elemests"%x);
#Using for loop to enter a element of array .
for i in range(x):
    n=int(input());
    ary.append(n);
print(ary);
