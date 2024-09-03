#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     21/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
class Employee:
    #class variable
    No_of_leaves=10;
    #constractor
    def __init__(self,aname,asalary,arole):
        self.name=aname;
        self.sal=asalary;
        self.role=arole;

    #self keyword accept instace and show the instace variable.
    def printdet(self):
        return f"The Name is {self.name}.\nSalary is {self.sal}.\nNumber of leaves {self.No_of_leaves}. \nAnd role is {self.role}.";

    @classmethod
    def change_leaaves(cls,newleaves):#cls is like a Employee
        cls.No_of_leaves=newleaves;
    @classmethod
    def from_dash(cls,string):

        return cls(*string.split("-"))
##        hold=string.split("-");
##        print(hold);
##        return cls(hold[0],hold[1],hold[2]);


o3=Employee.from_dash("Danyal-45000-labour");
print(o3.printdet())
o1=Employee("Zain",34000,"Scientist");
print(o1.printdet());
o1.change_leaaves(35);
print(o1.No_of_leaves);
##obj1=Employee();
##obj2=Employee();
##
##obj1.name="Noman Amjad";
##obj1.salary=100000;
##obj1.role="Programer";
##
##obj2.name="Basit";
##obj2.salary=120000;
##obj2.role="Manager";
##
##print(obj2.printdet());
##print(obj1.rintdet());
