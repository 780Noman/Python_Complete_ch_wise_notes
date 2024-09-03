#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     26/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Operator overloading
############# Dunder method#################
'''The method that started with underscore and ended with underscore are called dender method'''
class Employee:
    No_of_leaves=10;
    def __init__(self,aname,asalary,arole):
        self.name=aname;
        self.salary=asalary;
        self.role=arole;
    def printdet(self):
        return f"The name is {self.name}. \nThe salary is {self.salary}.\n The role is {self.role}.";
    @classmethod
    def modify(cls,new_leaves):
        No_of_leaves=new_leaves;
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"));
    @staticmethod
    def printstr(string):
        print("This is a good "+string);
    def __add__(self,other):
        return self.salary + other.salary;
    def __truediv__(self,other):
        return self.salary / other.salary;
    def __floordiv__(self,other):
        return self.salary // other.salary;
    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}')";
    '''The str function preference first to execute rather than repr function if you want to call the repr function than write repr(obj).
    If str not exist in the class the repr automaticaly executed.'''
    def __str__(self):
        return f"The name is {self.name}.\n The salary is {self.salary}.\n The role is {self.role}.";
emp1=Employee("Noman",3000,"Programmer");
emp2=Employee("Murtaza",4000,"Scientist");
print(emp1);

print(emp1+emp2);
print(emp1/emp2);
print(emp1//emp2);
