#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     20/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Decorators in python
##def function1():
##    print("Hello world");
##fun2=function1;
##del function1;
##fun2();

##def funcret(num):
##    if num==0:
##        return print;
##    if num==1:
##        return int;
##a=funcret(0);
##print(a);

##def executor(func):
##    func("this is passing of print function as a argument..");
##executor(print);

def dec12(func1):
    def nowexe():
        print("Executing now");
        func1();
        print("Executed successfully");
    return nowexe;
@dec12
def who_is_Ali():
    print("Ali is a good boy. ");
##who_is_Ali=dec1(who_is_Ali);
who_is_Ali();

