#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     16/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#---------------Tuple in Python----------------------------------
print("#---------------Tuple in Python----------------------------------")
#tuple is a collection of immuteable hetrogeneous python objects.
#it alse contain all type of data.
t=();
print(t);
print(type(t));
city="rwp",;
print(city);
city=("lahore",);
print(city);
city=("isl","rwp","lahore","gujrat");
print(city);
list1=[1,2,3,4];
list1.append(5);
print("List can be append : ",list1);
#city.append("karachi");#tuple can't be appended.
#--------------concatination of tuple---------------------------
num=1,2,3,4;
ch=('a','b','c');
conc=num+ch;
print("After concatenation of two tuple is : ",conc);
print("After concatenation of ch and city typle is : ",ch+city);
#---------------Nesting of typle------------------------------
nest=(ch,num);
print("The Nesting tuple is : ",nest);
neste=((34,67.3,1.4),('#','@'));
print(neste);
#--------------------Repetition of element---------------------
rep=("Rwp  ",)*5;
print("The 0 repeated 5 time : ",rep);
print("After that :",rep*2);
#------------------Slicing in tuple---------------------------
num=(1,2,3,4,5,6,7,8,9);
print(num[:4]);
print("Jumping from 1 index is :",num[::2]);
print("Revese order jump from 2 index is : ",num[::-3]);
#--------------Unpacking-------------------------------------
#When passing a element as a argument from tuple .
upack=tuple("Hellow world");
print("The unpacking tuple is : ",upack);
#Assign a value to variable using a tuple.------------------
num=(1,2,3,4);
a,b,c,d=num;
print(a,b,c,d);
s,*other,e=num;
print(s,"\n",other,"\n",e);
#---------------Deleting a tuple----------------------------
tpl=(2.3,4.4,2.1,6.2);
print("The tuple is : ",tpl);
del tpl;#del keyword use to delete the tuple.
#print(tpl);
v=[1,2,3];
print("The list is :",v);
del v;
#print(v);After deleting the list cann't be show.
#-------------------Built in function with tuple------------
tpl=(2.3,4.4,2.1,6.2);
s=sum(tpl)
print("The total sum of tpl is :",s);
print("The maximum number in the tpl is :",max(tpl));
print("The minimum number in the tpl is :",min(tpl));
print("The average of tpl element is : ",sum(tpl)/len(tpl));
#----------Converting list to tuple-----------------------
lst=[1,2,3,4];
print(lst);
print(type(lst));
tup=tuple(lst);
print("After converting : ",type(tup));
print(tup);
tpl=(2.3,4.4,2.1,6.2);
print(tpl);
l=list(tpl);
print(type(l));
print(l);
#-----------Nesting tuple within a list------------------
lst=[(1,2,3,4),('a','b','c')];
print("The nesting of two tuple in list :",lst);
lst.append((3.3,4.4));
print("After appending the lst is : ",lst);
lst.remove(lst[0]);
print("After removing the 0 index is :",lst);
#------------Nesting list within a tuple-----------------
tup=([1,2,3,4],[3.3,5.4,6.3]);
print("The nesting of 2 list within a tuple is : ",tup);
#tup.append(['e','a']);You cannot appending the tuple.
tup[0].append(5);
tup[1].append(7.3);
print("After appending the element of list that nested in tuple is : ",tup);#only when they are list.
tup[0].remove(2);
tup[1].remove(5.4);
print("After removing the element of list that are nested in tuple is : ",tup);#only when they are list.
tup[0].extend(tpl);
print("After extended the tup to tpl then : ",tup);