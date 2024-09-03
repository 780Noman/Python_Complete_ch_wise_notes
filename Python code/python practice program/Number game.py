#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     23/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#no of guesses 9
#print no of guesses left
#no of guesses he took to finish
#game over.
gus=4;
num=10;
incre=0;
while (True):
    n=int(input("Enter a number :"));
    incre=incre+1;
    if (gus>0):
        if(num==n):
            print("Congragulation,Your choice is correct...");
            print("After",incre," time guesses you took to finish..");
            print("Number of Guesses left %d :"%gus);
            break;
        elif (num<n):
            print("Please Enter less than %d"%n);
            gus=gus-1;
            print("Number of Guesses left %d :"%gus);
        elif (num>n):
            print("Please Enter greater than %d"%n);
            gus=gus-1;
            print("Number of Guesses left : %d "%gus);
    else:
        print("Game Over");
        print("Try Again.....");
        break;



