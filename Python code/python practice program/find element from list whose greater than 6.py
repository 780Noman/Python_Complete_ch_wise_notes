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
#list of list
l=[[1,"hello"],[2,"How"],[3,"are"],[4,"you?"]];
print(type(l));
for i,words in l:
    print(i,words);
print("\n")
st="Are you ready?";
for item in st:
    print(item,end="");
print();
#Type casting list to dict...
d=dict(l);
print(type(d));
print(d);
print(d[1]);
for key,val in d.items():
    print(key,val);
#When you need only key then...
for keys in d:
    print(keys);
# write program to create a list and print only these element whose key value greaten than 6;
li=[1,"hi",2,33,4,3,5.6,56,3,53,6,76];
print("The greate than 6 number in the list is :")
for i in li:
    if str(i).isnumeric() and i>6:
        print(i);
