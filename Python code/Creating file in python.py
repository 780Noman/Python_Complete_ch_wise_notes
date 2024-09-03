#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     28/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Creating a file in python
from os import path

def createFile(dest):
    if not (path.isfile(dest)):
        f=open(dest,'w');
        f.write('''Welcome to python language....''');
        f.close();
dest="C:\\Users\DELL\Documents\Sample.txt";
createFile(dest);

input("File created...")
