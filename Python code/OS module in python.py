#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL

# Created:     30/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#OS module in python
import os

print(dir(os));
#check current working directory (getcwd);
print(os.getcwd());
#U could change current working directory
##os.chdir("D://");
##print(os.getcwd());
os.chdir("C://")
##f=open("Check.txt");
######Check list of folder in C directory#####
print(os.listdir("C://"));#list
######Create new folder##########
#os.mkdir("This");
#os.makedirs("Thiss/That");# create folder that inside thiss folder
#########Rename file name######
#os.rename("Nomiii.txt","Noman1.txt")
print(os.path.join("C://","/Nomi.txt"));

print(os.path.exists("C://Program Files"));

#print(os.path.isdir("C://Program Files"))

print(os.path.isfile("C://Program Files"));#its is dir not file


