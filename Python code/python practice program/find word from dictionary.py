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
#Create a dictionary and take input  word from the user and return the meaning of the words from the dictionary.
d={"mutabe":"Which value can be change...",
"Immutable":"Which value can't be change...",
"Noun":"Noun is a name of person or a thing...",
"set":"Set is a well defined collection of distinct objects..."};
word=input("Whose word meaning you are trying to find :");
print(d[word]);

