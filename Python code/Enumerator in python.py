#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     10/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#enumerator in python
lis=["Ali","Ahmed","Azher","Farhan"];
##i=0;
##for name in lis:
##    if i%2 is  0:
##        print(name);
##    i+=1;

#Then we use Enumerator in python
for index,item in  enumerate(lis):
    if index%2 is not 0:
     print(f"This is my friend {item}");