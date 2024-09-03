#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     25/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#File basic concept
##"r"=Open a file for reading.Defaulf mode.
#"w"=Open a file for writing.
#"x"=Creates file if not exists
#"a"=Add more content to a file.
#"t"=text mode.Default mode
#"b"=binary mode.
#+"=read and write.


#Writing and appending mode in file .....
#fptr=open("Nomi11.txt","a");#a used for append mode
##fptr=open("Nomi11.txt","w");#w used for write mode.
##le=fptr.write("Hey, How are you ?\n");#Checking length of file.
##print(le)
##
##fptr.close();

#Handle read and write mode at the same time.
fptr=open("Nomi11.txt","r+");
##print(fptr.read());
##fptr.write("Are you ready for running.");
#adding  some string in the file  then read in the program....
##print(fptr.read());

#Some seek() and tell function concept in file.
#Seek(0) function take the pointer on the 0 index of file.
#tell() function show the index of pointer .
print(fptr.tell());
print(fptr.readline());
print(fptr.tell());
print(fptr.readline());
print(fptr.tell());


fptr.seek(20);
print(fptr.readline());
fptr.close();