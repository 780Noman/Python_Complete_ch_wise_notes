#-------------------------------------------------------------------------------
# Name:        module1
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
##
##Abstraction
##Encapsulation
##Inheritance
##Polymorphism
#Public private and protected specifier
class Employee:
    pub="Public specifier";
    _protect="Proctect specitier";
    __private="Private specifier";
    No_of_leaves=20;
    def __init__(self,aname,asalary,arole):
        self.name=aname;
        self.salary=asalary;
        self.role=arole;
    #self keyword accept instace and show the instace variable.
    def printdet(self):
        return f"The Name is {self.name}.\nSalary is {self.salary}.\nNumber of leaves {self.No_of_leaves}. \nAnd role is {self.role}.";
    @classmethod
    def change_leave(cls,newleaves):
        cls.No_of_leaves=newleaves;
    @classmethod
    def from_slash(cls,string):
        return cls(*string.split("/"));
    @staticmethod
    def printgood(strings):
        print("My name is "+strings);
instance=Employee("Basit",50000,"Typist");
print(instance.pub);
print(instance._protect)
print(instance._Employee__private);#Nemangling in python because u cann't you private var in outside the class.
