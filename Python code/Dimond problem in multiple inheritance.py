#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      DELL
#
# Created:     25/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Diamond Shape problem in  Multiple Inheritance
class A():
    def met(self):
        print("This is a method from class A.");
class B(A):
     def met(self):
        print("This is a method from class B.")
class C(A):
    def met(self):
        print("This is a method from class C.")
class D(C,B):
    def met(self):
        print("This is a method from class D.")



#instance /objects
a=A();
b=B();
c=C();
d=D();

d.met();