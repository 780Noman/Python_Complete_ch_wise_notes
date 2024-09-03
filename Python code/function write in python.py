#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     26/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Function-------------------
#Function is line of code that perform sum action.
#syntax       def fun_name:
#                statement(s)
def welcome():
    print("Well come to python language.");
welcome();
def add(a,b):
    c=a+b;
    print(id(a),id(b))
    print("The values of a:%d  and b:%d :"%(a,b));
    print("The sum of two number is :",c);
add(3,4);
x=10;
y=20;
add(x,y);
print(id(x),id(y))
#If you change the position of element in function.
def sub(y,x):
    total=y-x;
    print("The value of x:%d and y:%d :"%(x,y));
    print("The subtraction of two number is :",total);
sub(45,5);
sub (x=3,y=4);
#Set default value itself
def mul(a=1,b=2):
    m=a*b;
    print("The value of a:%d and b:%d is :"%(a,b));
    print("The multiplication of two number is :",m);
mul(a=4);
mul(3);
#adding many number using function.
def ad(*t):
    print("The type of li variable is  :",type(t))
    total=0;
    for i in t:
        total=total+i;
    print("The sum of all number that is passing by user :",total);
ad(3,5,6,6);
#Using function to change the element of list.
def ch_element(list):
    l[1]=10;
    print("After changing :",l);
l=[1,2,34];
print("The original list is : ",l);
ch_element(l);
#return value of function.
def re_value(a=10,b=90):
    result=a+b;
    return result;
r=re_value();
print("The sum of 2 number is :",r)




