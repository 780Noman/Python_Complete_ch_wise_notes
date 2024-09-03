#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     20/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
###-----------For loop in python----------------
##x=[2,3.4,"hi"];
##for i in x :
##    print(i);
##y="Hey, how are you?";
##for i in y :
##    print(i,end="");
###Print any even number that range b/w 20.
##print("\nPrint any even number that range b/w 20.\n");
##for i in range(0,21):
##    if i %2 == 0:
##        print(i);
###Print any odd number that range b/w 20.
##print("Print any odd number that range b/w 20.\n");
##for i in range(0,20):
##    if i%2!=0:
##        print(i);
###Print sum of even number b/w 20.
##print("Print sum of even number b/w 20.");
##sum1=0;
##for i in range(0,21):
##    if i%2==0:
##        sum1=sum1+i;
##print(sum1);
###--Nested For loop in python .------------------------------
###Make a triangel of digit.
n=int(input("Enter a number :"));
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="");
    print();

### Two matrix sum .
##r=int(input("Enter a number of Row :"));
##c=int(input("Enter a number of column :"));
##X=[];
##val=[];
##for i in range(0,r):
##    for j in range(0,c):
##        val.insert(j,int(input("Enter the %d * %d element :"%(i,j))));
##    X.insert(i,val);
##    val=[];
##Y=[];
##for i in range(0,r):
##    for j in range(0,c):
##        val.insert(j,int(input("Enter the %d * %d element :"%(i,j))));
##    Y.insert(i,val);
##    val=[];
##sum1=[];
##for i in range(0,r):
##    for j in range(0,c):
##        val.insert(j,X[i][j]+Y[i][j]);
##    sum1.insert(i,val);
##    val=[];
##    print(sum1);
#**********************Else statement with for loop****************
ls=["Noman","Ahmed","Basit"];
for i in ls:
    if i=="Ahmed":
      print(i);
      #break

else:
    print("This for loop ended successfully...")