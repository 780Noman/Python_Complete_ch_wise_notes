#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     18/10/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
    #-----------first class work---------
##a=100;
##b=20;
##c=30;
##sum1=a+b;
##print("a+b",c);
##print("Second Method :\n");
##x=int(input("Enter x value: "));
##y=int(input("Enter y value :"));
##z=int(input("Enter z value :"));
##print(x+y,z);

 #------------Second class work---------
print("Guess a Number :");
num=int(input());
if num>10 and num<20:
    print("\nCorrect Guess... \n");
else:
    print("\n Incorrect Guess!!!");

print("Are you a Robot?\n1.Yes \n2.No\n");
chk=input();
if chk=="yes":
    print("\nSorry! Robot are not allowed here!!!");
else:
    print("Welcome to Python World....");
print("Create a password :");
cp=input();
numOne=int(input("Enter Num One :"));
numTwo=int(input("Enter Num two :"));
print("Enter passoword to display Result:")
ep=input();
if cp==ep:
    sums=numOne+numTwo;
    print("\nResult :",sums);
else:
    print("\nWrong password !!!!!");

for i in range(5):
    print("Hello world !!!");

num=int(input("Enter a number :"));
for i in range(num):
    print("hi..");
