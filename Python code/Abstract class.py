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


#Abstract Base class & @abstractmethod

from abc import ABC,abstractmethod
##from abc import ABCMeta,abstractmethod

##class shape(metaclass=ABCMeta):
class shape(ABC):
    ''' @abstractmethod enforce that the printarea function in all subclass
       must have defining.'''
    @abstractmethod
    def printarea(self):
        return 0;

class Rectangle(shape):
    types="Rectangle";
    sides=4;
    def __init__(self):
        self.lenght=6;
        self.breadth=7;

    def printarea(self):
        return self.lenght*self.breadth;

rect1=Rectangle();
print(rect1.printarea());
"""We can't create obj of the abstract class"""
#shp=shape();