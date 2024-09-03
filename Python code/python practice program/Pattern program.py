#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     25/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Exercise  print sterik pattren.
##n=int(input("Enter a number :"));
##b=int(input("Enter a boolean number :"));
##bo=bool(b);
##if bo==True:
##    for i in range(1,n+1):
##        for j in range(1,i+1):
##            print("*",end="");
##        print();
##elif bo==False:
##    for i in range(n,0,-1):#-1 decresing the value of i var/
##        print(i)
##        for j in range(1,i+1):
##            print("*",end="");
##        print();


#Next method
#Exercise  print sterik pattren.
n=int(input("Enter a number :"));
b=int(input("Enter a boolean number :"));
bo=bool(b);
if bo==True:
    for i in range(1,n+1):
         print("*"*i);
elif bo==False:
    for i in range(n,0,-1):
        print("*"*i);



