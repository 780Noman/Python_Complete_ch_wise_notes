#-------------------------------------------------------------------------------
# Name:        module1
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
#--Dictionary in python-----
#dictionary is unordered collection of data stored as a pair of key and value.
#syntax  variable_name={key1:value1 ,key2 :value2.....};
d={};
print(d);
d1={1:"welcome",2:"to",3:"python"};
print(d1);
d2={"name":"Noman","age":20,"profession":"student"};
print(d2);
d3=dict({1:"welcome",2:"to",3:"python",4:"toturial"});
print(d3);
#--Second method----
d4=dict([(1,"welcome"),(2,"to"),(3,"python")]);
print(d4);
#---Nested dictionary---------------------------
d5={"name":{"First":"Noman","last":"Amjad"},"age":19,"profession":"student"};
print(d5);
#-----------Adding Element in dictionary----------------
d={};
d[0]="Hello";
print(d);
d[1]=("How", "are", "you.");
print(d);
d["name"]="Noman";
print(d);
#--Set a element in dictionary---
d["name"]={"first":"Noman","last":"Amjad"};
print(d);
#----Accessing element of dictionary----
print(d["name"]);
print(d["name"]["last"]);
print(d.get(1));
#---Deleting element from dictionary---
d.pop(0);
print(d);
d.popitem();
print(d);
print(d3);
#---Builtin function within dictionary--------
print(d3.values());
keys={'a','b','c','d'};
value=1;
print(dict.fromkeys(keys,value));
d.clear();
print(d);
Ndict=dict({1:"Ali",2:"Ahmed",3:"Arslan"});
print(Ndict);
newd=Ndict.copy();
#When you want to delete the item from dictnary.
del newd[2];
print(newd);
newd.update({4:"Ahsan"});
print(newd);
newd[3]="Haider";
print(newd);

