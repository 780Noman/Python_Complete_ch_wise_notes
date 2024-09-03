#-------------------------------------------------------------------------------
# Name:        module2
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
#faulty calcultor

print("Enter a first number :");
n1=int(input());
print("Enter a operator you (+,-,*,/) :");
op=input("Enter the opertor:");
print("Enter a second number :");
n2=int(input());

if op=='*':
    if (n1==45 and n2==3) or (n1==3 and n2==45):
        print("Result = 555");
    else:
        print("n1*n2 = ",n1*n2);
elif op=='+':
    if(n1==56 and n2==9) or (n1==9 and n2==56):
        print("Result= 77");
    else:
        print("n1+n2 = ",n1+n2);
elif op=='/':
    if(n1==56 and n2==6) or (n1==6 and n2==56):
        print("Result = 4");
    else:
        print("n1/n2 = ",n1/n2);
elif op=='-':
    print("n1-n1 = ",n1-n2);
else:
    print("Invalid input! Please try again....");
