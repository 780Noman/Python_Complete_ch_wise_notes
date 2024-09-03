#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     27/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
##############Object introspection################
"""its mean that the programmer want to check where are the object coming and which class this object and who its type where location this store etc"""
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname;
        self.lname=lname;
    def show(self):
        return f"The name is {self.fname} {self.lname}.";
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return f"The email is not set please use a setter to set email.";
        return f"{self.fname}-{self.lname}@gmail.com";
    @email.setter
    def email(self,string):
        names=string.split("@")[0];
        self.fname=names.split("-")[0];
        self.lname=names.split("-")[1];
    @email.deleter
    def email(self):
        self.fname=None;
        self.lname=None;
emp=Employee("Noman","Amjad");
print(emp.show());
print(emp.email);
print(type(emp));
print(type("This is a string."))
print(id("Hi"));
print(id("Hello world"));
print(dir(emp));## dir show how to work with method and member in class exits.

import inspect
print(inspect.getmembers(emp))