#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     23/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
n=input("Enter a number one :");
num=input("Enter a number two :");
#Using try block
try:
   print("Result :",int(n)+int(num));
except Exception as e:
    print("Some error occur",e);
print("This line is very important for printing..");

####################
f=open("Zain Diet.txt");
try:#Run this code
    f1=open("Nomiii.txt");
except Exception as e:
    #Executed this code when there is an exception.
    print(e);
##You can write many type of exception


except EOFError as e:
    print(" EOF  error are created .",e);
except IOError as e:
    print("Print IO error are created .",e)
else:
    print("This will run only if except is not running.");
finally:
    ##It used for code cleaning its code run anyway in program.
    print("Run this code anyway....");
    f.close();
print("Improtant stuff..");