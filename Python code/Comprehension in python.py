#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     27/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


######### Comprehension in python ##############
##l=[];
##for i in range(100):
##    if i%3==0:
##        l.append(i);
##print(l);

###########List Comprehension syntax&&&&&&&&&&&&&&&&&&&&&&
ls=[i for i in range(100) if i%3==0];
print(ls);

############ Dictionary comprehension ##################
dict1={i:f"Item {i}" for i in range(30) if i%2==0};
dict2={i:f"Item {i}" for i in range(5)}
print(type(dict1));
print(dict1,"\n",dict2);

'''Change the dict syntax values:key form'''
dict2={value:key for key,value in dict2.items()};
print(dict2);

##########Set comprehension ###############
set_comp={alpha for alpha in ["A","B","A","C"]};
print(type(set_comp));
print(set_comp);

########Generator Comprehension################
evens =(i for i in range(10) if i%2==0);
print(type(evens));
#print(evens.__next__());
for i in evens:
    print(i)
