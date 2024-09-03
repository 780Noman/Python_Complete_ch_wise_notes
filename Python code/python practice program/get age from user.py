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
#Write a program to get a age from user and inform to what you will able to drive the car.
age=int(input("Please Enter your age :"));
if age<=0 or age>100 :
    print("Not a logical age....")
elif age>18:
    print("Wow, You are able to drive a car....");
elif age==18:
    print("Sorry, I can't decide about what you will drive a car or not...")
else:
    print("You are not able to drive a car....");