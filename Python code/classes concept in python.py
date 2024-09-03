#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     20/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Class in python
class student:
    pass
o1=student();#instance of class/object
o2=student();
##print(o1,o2);

o1.name="Noman";
o1.cls=12;
o1.sec='A';
print(o1.name);
o2.name="Ahmed";
print(o1.sec,o2.name);
o2.sub=["English","Urdu"];
print(o1.cls,o2.sub)
