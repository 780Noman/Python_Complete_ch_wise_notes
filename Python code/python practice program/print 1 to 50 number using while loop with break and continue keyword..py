#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     18/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#print a 1 to 50 numbers using while loop;
i=1;
while(i<50):
    if i<=5:
        i+=1;
        continue;
    print(i);
    if i==44:
        break;
    i=i+1;
print("loop are terminating...")