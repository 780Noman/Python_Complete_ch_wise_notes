#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     14/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#List------------------------------------------------------------------
num=[3,45,2,5];
print("The integer list is : ",num);
fl=[3.3,56.4,2.4];
print("The floating value list is : ",fl);
ch=['c','h','a'];
print("The character value list is : ",ch);
mix=[2,"two",'c',4.5,"ali"];
print("The list contain all type of data : ",mix);
#Accessing element of list---------------------------------------------
print(mix[1]);
print(mix[0:3]);#index 3 is excluded
print(mix[3:]);
print(mix[-3]);
print(mix[::3]); #jumping index number
print(mix[::-2]);#reverse order jumping index number
#Operation on list------------------------------------------------------
#if you want to print same number multiple time then:
s="pakistan  "*5;
print(s*2);
#Concatination of list--------------------------------------------------
concat=num+ch;
print(concat);
#---------------When passing argument from list------------------------
var=list("hello world");
print(var);
print(list("Qureshi"));
#-------When you hold one element of list in single variable or remaning element
#hold in other list----------------------------------------------------
one,*other=num;
print(one,other);
start,*other,last=mix;
print(start,other,last);
#------------------Method in list--------------------------------------
print(num);
num.append(50);#append the element
print("After append mood :",num);
num.extend(ch);#extend the other list
print("After extent mood : ",num);
num.remove(3);#removing the element form the list
print("After removing the 3 from given list : ",num);
num.insert(4,'z');
print("After inserting the z at 4 index is : ",num);
fl.sort();#-------------------ERROR
print("After sorting the list num is : ",fl);
fl.pop()
print("after pop the last digit is:", fl)
#-----------------Builtin function in list----------------------------
print("The length of list num is : ",len(num));
print("The fl list is : ",fl);
print("The maximum number in list fl is : ",max(fl));
print("The minimum number in list fl is : ",min(fl));
print("The sum of number in list fl is : ",sum(fl));
avg=sum(fl)/len(fl);
print("The average of fl list element is : ",avg);
