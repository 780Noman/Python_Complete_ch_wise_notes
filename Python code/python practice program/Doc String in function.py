#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     23/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Function write for average..
a=10;
b=20;
c=sum((a,b));#Always putting values iteratabel.
print(c);

#user defined function.Find average
def fun1(a,b):
    average=(a+b)/2;
    return average;
print("The Average is :",fun1(10,30));

#Doc String within function.
def func2(x,y):
    """It is a doc string.It write always first line of function."""
    s=a+b;
    print("The sum is :",s);
print(func2.__doc__);
func2(3,5);