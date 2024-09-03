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
#Write the output of the following code.
price=20;
quantity=5;
amount=price*quantity;
if amount>100:
    if amount>500:
        print("Amount is greater than 500.");
    else:
        if amount<500 and amount>400:
            print("Amount is between 400 and 500");
        elif amount<500 and amount>300:
            print("Amount is between 300 and 500");
        else:
            print("Amount is between 200 and 500");
elif amount==100:
    print("Amount is 100");
else:
    print("Amount is less than 100.")
