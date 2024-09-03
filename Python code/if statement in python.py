#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     19/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#----if statement in python-------
#syntax-  if condition:
    #Statements to execute if
    #condition is true;
a=60;
if a<50 :
         print("This is if statement body .This is the  true condition.");
print("This is the outside the if block");
#---If else statement in python-----
i=21;
if i%2 == 0:
    print("\nThe number is even.");
else:
    print("\nThe number is odd.")
#--Nested if statement -----
c=21;
if c<25:
    if c%2==0:
        print("\nc is an even number less than 25.");
    else:
        print("\nc is an odd number less than 25.");
else:
    print("\nc is greater then 25.")
#------if-elif-else ladder in python------
var='e';
if var=='a':
  print("\nthis is the vowel a.");
elif(var=='e'):
     print("\n This is the vowel e.");
elif var =='i':
     print("\n This is the vowel i.");
elif var=='o':
     print("\n This is the vowel o.");
elif var=='u':
     print("\n This is the vowel u.");
else:
     print("\nThis character is not a vowel....");

list1=[1,2,43,54];
if 43 in list1:
    print("The number 43 exist in the given list...");
if 12 not in list1:
    print("The number 12 is not exist in the given list... ");

#Write a code in one line.
n=100;
if n>1: print("n is greater than 1.");

print("n is less than 20 .") if n<20 else print("n is greater than 20.")


#--------------Match case statement in python----------------------------
num=int(input("Enter a Number : "))
match num:
    case 1:
        print("this is case 1.")
    case 2:
        print("this is case 2.")
        for i in range(1,11):

            print("2*",i,"=",2*i,"\n")
    case 3:
        print("this is case 3.")
        for i in range(1,11):

            print("3*",i,"=",3*i,"\n")
    case _:
        print("invalid input please try again...!!!")
