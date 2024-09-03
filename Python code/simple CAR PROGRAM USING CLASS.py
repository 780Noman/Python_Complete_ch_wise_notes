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
#Write a program using class to describe the feature and method of car.
class car:
    def __init__(self,speed,year):
        self.speed=speed;
        self.year=year;
    def getspeed(self):
        print("The Maximum speed is : ",self.speed);
        print("The model is :",self.year);
    def setspeed(self,speed):
        self.speed=speed;

BMW=car(300,2014)
FORD=car(350,2022)
#########car.getspeed(BMW);
##########car.getspeed(FORD);


BMW.getspeed();
BMW.setspeed(122);
BMW.getspeed()
FORD.getspeed();