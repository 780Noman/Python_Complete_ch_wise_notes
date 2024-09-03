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
#Local variable and global variable----------------
##l=10;#Global
##def fun(n):
## #   l=5;#Local
##    m=100;#local
##    global l;#Use keyword to take permission to change global variable.
##    l=l+12; #You can't change the global variable ...
##    print(l,m);
##    print(n,"I am Noman.");
##fun("Hi ");

x=101;
def Nomi():
    x=20;
    def ali():
        global x;
        x=100;
    #print("Before calling ali()\n",x);
    ali();
    print("After calling ali()\n",x);
Nomi();
print(x)


