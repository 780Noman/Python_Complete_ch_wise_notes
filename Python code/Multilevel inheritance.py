#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      DELL
#
# Created:     24/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Multileverl inheritance
'''In this program grandson class access all element attributes and method easily.'''
class dad:
    age=40;
    def show(self):
        print(f"The Age of dad is {self.age}");
class Son(dad):
    age_of_son=20;
    def printage(self):
        print(f"The Age of Son is {self.age_of_son}");
class Grandson(Son):
    Age_of_Grandson=2;
    def printage(self):
        print(f"The age of Grandson is {self.Age_of_Grandson}");
d=dad();
s=Son();
grand_S=Grandson();
grand_S.printage();
print(grand_S.age);