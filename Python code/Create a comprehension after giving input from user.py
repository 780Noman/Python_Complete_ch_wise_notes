#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     28/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
list1=[];
while True:
    print("How many items do you want to enter in a list :");
    n=int(input());
   # input_string=input("Enter a list element separated by comma :");
   # list1=input_string.split(",");
    for i in range(n):
        item=input("Enter a element :");
        list1.append(item);

    print("Which comprehension do you want to make :\n1.List \n2.Dict \n3.Set");
    com=int(input());
    if com==1:
        ls=[i for i in list1];
        print(ls);
        print(type(ls));
        break;
    elif com==2:
        dic={i:j for i,j in enumerate(list1) };
        print(dic);
        print(type(dic));
        break;
    elif com==3:
        sets={i for i in list1};
        print(sets);
        print(type(sets));
        break;
    else:
        print("Invalid Input >PLease try again...");
        continue;

