#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     14/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Conversion of datatype-------------------------------
x="123";
int(x);
x=int(x);
print("After converting in interger : ",x);
x=float(x);
print("After converting in float value : ",x);
x=complex(x);
print("After converting in complex value : ",x);
print("When passing value in complex :",complex(3,5));