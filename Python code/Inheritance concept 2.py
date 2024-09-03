#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     22/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Inheritance in python
class Employee:
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

#create child class
class programmer(Employee):
    No_of_holiday=30;
    def __init__(self,aname,asalary,arole,alanguage):
        self.name=aname;
        self.salary=asalary;
        self.role=arole;
        self.language=alanguage;

    def printprog(self):
        return f"The programmer  Name is {self.name}.\nSalary is {self.salary}. \nAnd role is {self.role}.\nThe knowldege of language {self.language}";

Eobj=Employee.from_slash("Mustafa/34000/Manager");

Pobj=programmer("Noman",50000,"Programmer",["Python","C/C++"]);
print(Pobj.printprog());
print(Pobj.No_of_leaves);