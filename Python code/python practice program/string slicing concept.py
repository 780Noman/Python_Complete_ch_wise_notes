#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     17/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#string slicing concept
s="Hello world!";
s1='hello everyone'
s2='''how are you'''
print(s1,s2,s)
print(type(s));
print(len(s));
print(s);
print(s[::2]);# 2 are used for skiping 1 character from string.
print(s[0:5]);
print(s[-6:]);#acces reverse index character.
print(s[2:-5]);#when using - sign then the one index less start counting...
print(s[2::12])
#When you want to reverse the string then.
print(s[::-1]);#using -1 for string reversing .

# built in function for string
print(s.isalnum());#false
print(s.isalpha());#false
print(s.endswith("ld!"));#True
print(s.endswith("hello"));#false
print(s.replace("w","W"));


# How to attaching two string...
s1="hi, ";
s2="How are you?";
print(s1,end=" ");
print(s2);

print("hello","Are you ready?",end="");
