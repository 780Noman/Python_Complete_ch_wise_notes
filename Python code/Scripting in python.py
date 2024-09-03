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
#Python scripting....-----------------------------------
import os

def current_directory():
    cwd=os.getcwd();
    print(cwd);

def file_path(filename):
    path=os.path.abspath((filename));
    print(path);

current_directory();
filename="Sample.txt";
file_path(filename);

#Time module in python-----------------------------------

import time

epc=time.time();
print(epc);

localtime=time.localtime(epc);
print(localtime);
print(localtime.tm_year);
print(localtime.tm_mon);
print(localtime.tm_mday);

print(time.ctime(epc));

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


#Standard Email transfer protocol.
import smtplib

smtObj=smtplib.SMTP('smtplgmail.com',587);
smtObj.ehlo();
smtObj.starttls();
smtObj.login('nq6145841@gmail.com','nomi');
smtObj.sendmail("nq6145841@gmail.com","csd1.19.54@gmail.com",'Subject :SMTP checking \n This is a text email....');
smtObj.quit();


