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
#Threading in python
from threading import *
def show():
    print("This is child thread.");
t=Thread(target=show())
t.start()
print("This is a parent thread.")
#Creating class thread
class Mythread(Thread):
    def run(self):
        for i in range(5):
            print("\nThis is a child class.");
t=Mythread()
t.start()
for i in range(5):
    print("\nThis is the main thread.");

#Using object to create thread.
class demo:
    def show(self):
        for i in range(3):
            print("\n This is demo class.");
obj=demo()
t=Thread(target=obj.show());
t.start();
for i in range(3):
    print("\n This is parent thread ....")
