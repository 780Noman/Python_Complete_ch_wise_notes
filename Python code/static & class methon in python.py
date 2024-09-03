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
    def change_leaves(cls,newleaves):#cls is like a Employee
        cls.No_of_leaves=newleaves;
    '''It works like a alternative constructor'''
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
##        hold=string.split("-");
##        print(hold);
##        return cls(hold[0],hold[1],hold[2]);
    '''If you not required any self and class methon then  you create
        a staticmethon.'''
    @staticmethod
    def printgood(string):
        print("This is good "+string);



o1=Employee.from_dash("Danyal-45000-labour");
print(o1.printdet());
o2=Employee.from_dash("Zain-50000-Scientist");
o1.printgood("Boy");
