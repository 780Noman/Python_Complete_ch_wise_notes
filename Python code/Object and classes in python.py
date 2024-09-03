#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     26/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#class and object in python.
class person:
    def __init__(self):
        self.name="Noman";
        self.age=19;
        self.gender="male";
    def talk(self):
        print("Hi ,I'm  ",self.name);
    def vote(self):
        if(self.age<18):
            print("You are not eligible to vote.");
        else:
            print("You are eligible to vote....");
#creating object in python.
#obj=person()
#person.talk(obj);
#person.vote(obj);
#other method -------------
obj=person();
obj.talk();
obj.vote();
#When many object are created by the user.
class man:
    def __init__(self,n,a,g):#
     self.name=n;
     self.age=a;
     self.gender=g;
    def talking(self):
        print("Hi, How are you ",self.name);
    def voting(self):
        if(self.age<18):
            print("You are not eligible to vote......");
        else:
            print("Yes, You are eligible to vote.......");
obj1=man("Ali",34,"Male");
obj2=man("Hammad",13,"male");
print(obj1.name,obj2.name)
obj1.talking();
obj1.voting();
obj2.talking();
obj2.voting();
