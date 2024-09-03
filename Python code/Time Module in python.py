#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     05/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Time module in python
import time

initial=time.time();#get 1 second
k=0;
while(k<45):
    print("HELLO WORLD");
##    time.sleep(2);#It pause the system to 2 second.
    k+=1;
print(f"While loop ran in {time.time()-initial} Seconds");

initial2=time.time();
for i in range(45):
    print("Hellow World");
print(f"For loop ran in {time.time()-initial2} Second");

# If you want ot get local time

localtime=time.asctime(time.localtime(time.time()));
print(localtime);