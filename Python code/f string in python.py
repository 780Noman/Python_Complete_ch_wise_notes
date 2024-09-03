#-------------------------------------------------------------------------------
# Name:        module2
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
#F string in python
import math
me="Noman";
a1=19;
##s="This is %s"%me;
##print(s);
##
###Second method
##st="This is %s %s"%(me,a1);
##print(st);

#Dot format
s="My Name is {1} .I am a {0} year old.";#Set index num in brackets.
a=s.format(a1,me);
print(a);

#f string method
st=f"I am a {me} .I am {a1} year old . We use expression {2*4} ,{math.cos(45)}";
print(st);



