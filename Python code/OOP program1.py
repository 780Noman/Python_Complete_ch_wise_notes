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
#Employee class
class Employee:
    No_of_leaves=10;
    pass;

#create object
a1=Employee();
a2=Employee();

#create instance variable
a1.Name="Noman Amjad";
a1.sec="B";
a1.age=20;

a2.Name="Usman";
a2.sec="A";
a2.age=21;

print(a1.Name,"\n",a2.Name);
print(Employee.No_of_leaves);
print(a1.__dict__);#dict is a attributes it return a dict of instace that show many class variable are created.
Employee.No_of_leaves=11;#You change value must be using class name not from instance.
print(Employee.__dict__)
print(a1.No_of_leaves);
print(a2.No_of_leaves);
print(a2.__dict__);