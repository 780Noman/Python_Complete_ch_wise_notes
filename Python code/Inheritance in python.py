#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     27/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
class vehicle:
    def __init__(self,speed,name,model):
        self.name=name;
        self.model=model;
        self.speed=speed;
    def getdata(self):
        print("The maximum speed is : ",self.speed);
        print("Model is : ",self.model);
        print("Name is : ",self.name);

######Child classes (Inheritance).


class truck(vehicle):        #Child class
    def accelerate(self):
        print('123');
    def opentrunk(self):
        print("Trunk has been opened");

class bike(vehicle):
    def accelerate(self):
        print('111');
v=vehicle(340,"BMW",2022);
v.getdata();
print("The data of truck is : \n");
t=truck(344,'Mazda',2002);
t.getdata();
t.accelerate();
t.opentrunk();
print("The data of bike is :\n");
b=bike(120,"Honda",2010);
b.accelerate();
b.getdata();
