#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     18/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


#write a program that get a number from user that is less than hundred ..
##num=float(input("Enter a number :"));
##while(True):
##    if num<=100 and num>0:
##         num=float(input("Enter a number :"));
##    continue;
##print("Sorry ,You enter the number is greater than 100...");
while(True):
    num=int(input("Enter a number :"));
    if num>100:
        print("Congrates,You enter a number is greater than 100.");
    else:
        print("Try again...!!");