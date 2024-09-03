#-------------------------------------------------------------------------------
# Name:        module1
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
#Polymorphism in python
##Abality to take various form.

class A:
    classvar1="I am a class variable in class A";
    def __init__(self):
        '''Instance variable '''
        self.var1="I am inside class A's constructor";
        self.classvar1="Instance var in class A";
        self.special="Special";
class B(A):
    classvar1="I am in class B";
    '''Constructor overriding :When any attribute override once time it cannot run again'''
    """If you want to run A class constructor after override the constructor then you use super().__init__ keyword . """
    def __init__(self):
        self.var1="I am  inside class B's constructor.";
        self.classvar1="Instance var in class B";
        super().__init__();
        print(super().classvar1)

a=A();
b=B();
'''It search first instance variable in class B if found here than print it otherwise go to the
 parent class A and found there if not found there than check back in class B class variable if class variable not found then go to the parent
 class A and check class variable exist there if exist then print it on screen.'''
#print(b.classvar1);
print(b.special,b.var1,b.classvar1);