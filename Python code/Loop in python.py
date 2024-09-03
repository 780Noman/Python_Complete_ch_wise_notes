#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      DELL
#
# Created:     19/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#----while loop in python------
#syntax
#while expression :
#    statement(s)
#python always input a value from user in string you must to change in required datatype
val=int(input("Enter a any number that is multiple of 7 :"));
while val%7!=0:# must enter a colon in end of loop and if statement

 val=int(input("Enter a any number that is multiple of 7 :"));
else:
    print("%d is a multiple of 7."%val);# %d is using for place holder and for multiple values  print("%d is a multiple of 7."%(val,val1...))
 #---  for loop in python----------
 #syntax    for counter in sequence:
  #  statement(s);
  #---------------------------------------------
x=[1,2,"Hello"];
for i in x :
    print(i);
    #-----------------------------------------
y="Hello World";
for i in y:
    print(i,end="");
    #---------------------Nested for loop-------------------
x=[[1,2,3],['a','b','c']];
print("\n");
for i in x:
    print("\n");
    for j in i:
        print(j,end="");
  #---Controling loop Using break keyword-------
#Transfer control to the statement right after the loop.
x="Hey there, How are you.";
print("\n");
for i in x:
    if i==",":
        break;
    print(i,end="");
 #----another keyword continue------
# skip the statement following it and returns control to the beginning of the loop.
print("\n");
for i in [1,3,45,67,9]:
    if i>10:
        continue;
    print(i);




