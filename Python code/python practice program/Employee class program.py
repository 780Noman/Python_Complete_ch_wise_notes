#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     11/07/2023
# Copyright:   (c) DELL 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
class Employee:
    name="Nomi"
    salary=100000
    #constructor in python
    def __init__(self):
        self.name="Ahmed"
        self.salary=1200000
    #parameterized constructor
    def __init__(self,n,s):
        self.name=n
        self.salary=s
    #function
    def getsalary(self):
        return self.salary

#obj1=Employee()
#print(obj1.name,obj1.salary)
obj2=Employee("Hammad",500000)
print(obj2.name,obj2.salary)
print(obj2.salary)