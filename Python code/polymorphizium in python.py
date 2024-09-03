#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     27/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#polymorphizium in python
class car: #parent class
    def __init__(self,model):
        self.model=model;

class OD(car): #child class
    def accelerate(self):
        print("140");
class BMW(car): #child class
    def accelerate(self):
        print(150);
class toyota(car):
    def accelerate(self):
        print(160);
objL=[OD("2016"),BMW("2000"),toyota("2020")];

for obj in objL:
    print(obj.model+" : ",end=" ");
    obj.accelerate();