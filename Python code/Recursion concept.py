#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      DELL
#
# Created:     02/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Recursion in Python
#n!=n*n-1*n-2*n-3......1;
def fun_iterative(n):
    fac=1;
    for i in range(n):
        fac*=(i+1);
    return fac;

def fun_recursive(n):
    if n==1:
        return 1;
    else:
        return n*fun_recursive(n-1);
num=int(input("Enter a Number :"));
print("The factorial through iterative approuch is :",fun_iterative(num));
print("The factorial through recursive approuch is :",fun_recursive(num));

