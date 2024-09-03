#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     17/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
"""writer a program you take a input 2 numbers from user and perform some
arithimetic operator on it."""
print("Enter a first number :");
var1=input();
print("You enter a number is :",var1);
print("Enter a second number :");
var2=input();
print("You enter a number is :",var2);
print("The sum of two numbers is : ",int(var1)+int(var2));

#subtraction of two number----------
print("The subtraction of given number is ;",int(var1)-int(var2));

#multiplication of two number is -------
print("The multiplication of given  number is : ",int(var1)*int(var2));

#division of two given number is ---------
print("THe division of given numbers is : ",int(var1)/int(var2));

#division of two given number is without decimal point -----------
print("The division of given numbers is without decimal point is :",int(var1)//int(var2));