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
#-----Sets in python----------------
#Set is an unordered collection of unique elements.
#syntax      variable_name=set(['a','b','c','d'])

s=set([1,2,3,4]);
print(type(s));
print(s);
s1=set([111,"hello","c",1122.4]);
print(s1);
#---Adding Element in sets---
s1.add("add");
print(s1);
#---frozen Set----
fs=frozenset([2,3.4,12]);
print(fs);
#fs.add(123);#You cannot add the element in frozen set but also add in set.
#-------Operation on sets---------------------
st1=set({3,4,6,7});
st2=set({2,3,9,8});
print(st1.union(st2));
print(st1.intersection(st2));
print(st1.difference(st2));
print(st1.isdisjoint(st2))
st2.remove(9);
print(st2);