#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     23/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#University has following grading system.
m=int(input("Enter a marks :"));
if m>0 and m<25:
    print("Your Grade is : F");
elif m>25 and m<45:
    print("Your Grade is : E")
elif m>45 and m<50:
    print("Your Grade is : D")
elif m>50 and m<60:
    print("Your grade is : C");
elif m>60 and m<80:
    print("Your grade is : B");
elif m>80:
    print("Your grade is : A");
else:
    print("Marks Enter should be greater than 0...\n");
