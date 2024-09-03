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
#Create a fibonacci series
#0,1,1,2,3,5,8,13.....;
def fib_seq(n):
    if n==1:
        return 0;#retrun 0 index of fibonaccii sequence
    elif n==2:
        return 1;
    else :
        return fib_seq(n-1)+fib_seq(n-2);
print("Enter a index number :");
num=int(input());
print("The Number is given index is :",fib_seq(num));
