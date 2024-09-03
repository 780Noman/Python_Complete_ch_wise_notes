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
a=25
b=47
operator=input("Please Enter a Operator (+,-,/,*) :"h)
if (operator=='+'):
    print("Result :",a+b)
elif (operator=='-'):
    print("Result :",a-b)
elif (operator=='/'):
    print("Result :",a/b)
elif (operator=='*'):
    print("Result :",a*b)
else:
    print("Invalid input!Please Try again....")