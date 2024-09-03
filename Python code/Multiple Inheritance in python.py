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
#Multiple Inheritance in python
class Employee:
    var="Employee class";
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
class player:
    var="Player class";
    No_of_games=4;
    def __init__(self,aname,agame):
     self.name=aname;
     self.game=agame;
    def printdet(self):
        return f"The Name is {self.name}.Played the Game is {self.game}";
class Coolprogrammer(Employee,player):#When you write the class first then the constructor of this class called before .
    language="C++/C";
    def printlang(self):
      return  self.language;

o1=Employee("Nomi",255,"Instructor");
o2=Employee("Haider",432,"Scientist");

p=player("Ali Raza",["Cricket"]);
print(p.printdet());
coolPro=Coolprogrammer("Zain",34000,"Manager");
de=coolPro.printdet();
print(coolPro.printlang())
print(de);
print(coolPro.var);
