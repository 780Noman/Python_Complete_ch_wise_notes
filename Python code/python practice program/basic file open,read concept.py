#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     24/08/2022
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
#"+"=read and write.


fptr=open("Nomiii.txt","rt");#"rb"=binary form.
#content=fptr.read();#If you iterate the content variable in loop then print character one by one.
#if you want to read line by line without using function.
##for line in fptr:
##    print(line,end=" ");

##print("\nUsing readline function to print line...");
##print(fptr.readline());
##print(fptr.readline());

print("\nUsing readlines function then print the list of file.");
print(fptr.readlines());
fptr.close();#file must close after working.


##content=f.read(2);#Read only first 2 character.
##print(content);
##
##content=f.read(2);#Read next 2 character..
##print(content);





