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
#Multiple threading in python.
from threading import *
import time
class demo:
    def num(self):
        for i in range(1,6):
            print("The number is :",i);
            time.sleep(1);
    def double(self):
        for j in range(1,6):
            print("The double of number is:",2*j);
            time.sleep(1);
    def square(self):
        for k in range(1,6):
            print("The square of number is :",k*k);
            time.sleep(1);
obj=demo();
t1=Thread(target=obj.num());
t2=Thread(target=obj.double());
t3=Thread(target=obj.square());

t1.start();
time.sleep(0.2);

t2.start();
time.sleep(0.2);

t3.start();
time.sleep(0.2);

t1.join();
t2.join();
t3.join();

print("This is the main threat....");
