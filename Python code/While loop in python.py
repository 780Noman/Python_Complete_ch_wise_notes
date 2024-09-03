#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     21/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Reverse condition apply.
i=10;
while i>=1:
    print("Pakistan zindabad");
    i-=1;
print("\nwhile loop is terminating after condition is wrong....");
#sequence condition apply.
j=1;
while j<=5:
    print("Hello World");
    j=j+1;
#Sum of first natural number.
sum1=0;
i=1;
while i<=10:
    sum1=sum1+i;
    i=i+1;
print("The sum of first 10 natural number is : ",sum1);
#The sum of even number b/w 20.
sum2=0;
j=1;
while j<=20:
    if j%2==0:
        sum2=sum2+j;
    j=j+1;
print("The sum even number b/w 20:",sum2);
#Find factorial of any number.
n=int(input("Enter a number to find factorial:"));
f=1;
v=1;
while n+1!=v:
    f=f*v;
    v+=1;
print("The factorial is : ",f);
#print the interges in revese order.
n=int(input("Enter a numer : "));
nr=0;
while n%10!=0:
    c=n%10;
    nr=nr*10+c;
    n=n//10;
print("The revese interger is : ",nr);
#Find length of list using while loop.
x=[1,3.3,"Hello",'a'];
length=0;
i=0;
try:
    while x[i]:
         length+=1;
         i+=1;
except IndexError:
     print("The length of list is : ",length);
#Find the length of typle .
x=(2,5,3.4);
l=0;
i=0;
try:
    while x[i]:
      l+=1;
      i+=1;
except IndexError:
      print("The length of tuple is : ",l);
#Create a triangle of intergers.
r=int(input("Enter a number of row:"));
i=1;
while i<=r:
    j=1;
    while j<=i:
        print(j);

