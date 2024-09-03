#-------------------------------------------------------------------------------
# Name:        module2
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
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname;
        self.lname=lname;
       ## self.email=f"{fname}-{lname}@gmail.com";

    def explain(self):
        return f" This employee is {self.fname} {self.lname}";
    @property
    def email(self):
        if self.fname==None or self.lname ==None:
            return "Email is not set.Please set it using setter.";
        return f"{self.fname}-{self.lname}@gmail.com";
    @email.setter #first you write method name which you want to set.
    def email(self,string):
        names=string.split("@")[0];
        self.fname=names.split("-")[0];
        self.lname=names.split("-")[1];
    @email.deleter
    def email(self):
        self.fname=None;
        self.lname=None;



pak_supporter=Employee("Noman","Amjad");
print(pak_supporter.explain())
print(pak_supporter.email);

pak_supporter.lname="Qureshi";
print(pak_supporter.lname);
print(pak_supporter.email);
'''Its line required setter that set the it'''
pak_supporter.email="abc-xyz@gmail.com";#create email setter function for this line.
print(pak_supporter.email);
'''If you want to delete the email attribute than write a deleter function'''
del pak_supporter.email;
print(pak_supporter.email)