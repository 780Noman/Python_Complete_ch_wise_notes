#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     03/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Modules in python
import random
random_num=random.randint(0,10);#give a any random num b/w 0 and 10.
print(random_num);


rand=random.random()*100;
print(rand);

lst=["Nomi","Ali","Arslan","Moin"];
choice=random.choice(lst);
print(choice);