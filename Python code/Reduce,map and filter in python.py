#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     18/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Map in python--------------------------------------------------!!!!!!!!!!!!

numbers=["3","34","64"];

##for i in range(len(numbers)):
##    numbers[i]=int(numbers[i]);
##numbers[2]=numbers[2]+1;
##print(numbers[2]);

"""map(int,numbers) first argument is a function that you want to apply on the list
second argument of name of list which you want to apply."""

numbers=list(map(int,numbers));
numbers[1]=numbers[1]+1;
print(numbers[1]);

##def sq(x):
##    return x*x;
num=[2,3,5,2,4,3,7];
square=list(map(lambda x:x*x,num));
print("Square of all element of list\n",square);

def cube(x):
    return x*x*x;
def squares(n):
    return n*n;

func=[squares,cube];
print("Square and cube [s,q]:\n")
for i in range(5):
    val=list(map(lambda x:x(i),func));
    print(val);

#----------------Filter in python-----------------------------
#It retrun true value only
list1=[1,2,3,4,5,6,7,8];
def is_grteater_5(n):
    return n>5;
gr_than_5=list(filter(is_grteater_5,list1));
print("Number greater than 5 :",gr_than_5);

#----------------Reduce in python---------------------------
from functools import reduce
list2=[1,2,3,4];
##num=0;
##for i in list2:
##    num=num+i;
##print(num);

numb=reduce(lambda x,y:x+y,list2);
print("Using Reduce to add the list element :\n",numb);




