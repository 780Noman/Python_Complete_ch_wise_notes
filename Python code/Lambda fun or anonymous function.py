#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     03/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Lamba function or anonymous functions
def add(x,y):
    return x+y;
minus=lambda a,b:a-b;#Both are same

##def minus(a,b):#Same to lambda function
##    return a-b;

print(minus(4,2));

##def a_first(a):
##    return a[1];#Return 1 index
a=[[1,14],[4,5],[11,3]];
a.sort(key=lambda x:x[1]);
print(a);