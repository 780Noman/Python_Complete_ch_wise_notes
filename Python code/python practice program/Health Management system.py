#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     26/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Health Management System.

#Getting time.
def gettime():
    import datetime;
    return datetime.datetime.now();

def log():
    print("\n\t\tChoose Your Client\n");
    client=int(input("\n1.Ali \n2.Ahmed  \n3.Zain"));
    if client==1:
        while True:
            print("\nWhat do you want to log for Ali:");
            choice=int(input("\n1.Diet  \n2.Activity"));
            if choice==1:
                f=open("Ali diet.txt","a"); # with open("Ali diet.txt","a") as f;
                data=input("Enter What has Ali Eaten?\n");
                f.write(str([str(gettime())])+" "+data+"\n");
                f.close();
                ch=int(input("Do you want to log more for Ali? \n1.Yes \n2.No\n"));
                if ch==1:
                    continue;
                else:
                    break;
            else:
                f=open("Ali exe.txt","a"); # with open("Ali exe.txt","a") as f;
                data=input("How much time has Ali worked out?\n");
                f.write(str([str(gettime())])+" "+data+"\n");
                f.close();
                ch=int(input("Do you want to log more for Ali? \n1.Yes \n2.No\n"));
                if ch==1:
                    continue;
                else:
                    break;
    elif client==2:
        while True:
            print("What do you want to log for Ahmed ?");
            choice=int(input("\n1.Diet \n2.Activity\n"));
            if choice==1:
                f=open("Ahmed diet.txt","a");
                data=input("Enter What Has Ahmed Eaten?");
                f.write(str([str(gettime())])+" "+data+"\n");
                f.close();
                ch=int(input("Do you want to log more for Ali? \n1.Yes \n2.No\n"));
                if ch==1:
                    continue;
                else:
                    break;
            else:
                f=open("Ahmed exe.txt","a");
                data=input("Enter How much time has Ahmed worked out?\n");
                f.write(str([str(gettime())])+" "+data+"\n");
                f.close();
                ch=int(input("Do you want to log more for Ali? \n1.Yes \n2.No\n"));
                if ch==1:
                    continue;
                else:
                    break;
    elif client==3:
        while True:
            print("What do you want to log for Zain?");
            choice=int(input("\n1.Diet \n2.Activity\n"));
            if choice==1:
                f=open("Zain diet.txt","a");
                data=input("Enter What Has Zain Eaten?");
                f.write(str([str(gettime())])+" "+data+"\n");
                f.close();
                ch=int(input("Do you want to log more for Ali? \n1.Yes \n2.No\n"));
                if ch==1:
                    continue;
                else:
                    break;
            else:
                f=open("Zain exe.txt","a");
                data=input("Enter how much time has Zain worked out?");
                f.write(str([str(gettime())])+"  "+data+"\n");
                f.close();
                ch=int(input("Do you want to log more for Ali? \n1.Yes \n2.No\n"));
                if ch==1:
                    continue;
                else:
                    break;
def retrieve():
    print("\n\t\tChoose your client\n");
    client=int(input("\n1.Ali \n2.Ahmed  \n3.Zain\n"));
    if client==1:
        while True:
            print("What do you want to retrieve for Ali?\n");
            choice=int(input("\n1.Diet \n2.Activity\n"));
            if choice==1:
               f=open("Ali diet.txt","r"); #with open("Ali diet.txt") as f;#don't need to write "r" here;
               print(f.readlines());  #for i in f:
               f.close();              #print(i,end="");
               ch=int(input("Do you want to Retrieve more record for Ali? \n1.Yes \n2.No\n"));
               if ch==1:
                  continue;
               else:
                    break;
            else:
                f=open("Ali exe.txt","r");
                print(f.readlines());
                f.close();
                ch=int(input("Do you want to retrieve more  record for Ali? \n1.Yes \n2.No\n"));
                if ch==1:
                    continue;
                else:
                    break;
    elif client==2:
        while True:
           print("What do you want retrieve for Ahmed ?\n");
           choice=int(input("\n1.Diet \n2.Activity\n"));
           if choice==1:
              f=open("Ahmed diet.txt","r");
              print(f.readlines());
              f.close();
              ch=int(input("Do you want to retrieve more record for Ahmed? \n1.Yes \n2.No\n"));
              if ch==1:
                    continue;
              else:
                    break;
           else:
            f=open("Ahmed exe.txt","r");
            print(f.readlines());
            f.close();
            ch=int(input("Do you want to retrieve more record for Ahmed? \n1.Yes \n2.No\n"));
            if ch==1:
                continue;
            else:
                break;
    elif client==3:
        while True:
            print("What do you want to retrieve for Zain?\n")
            choice=int(input("\n1.Diet \n2.Activity\n"));
            if choice==1:
                f=open("Zain diet.txt","r");
                print(f.readlines());
                f.close();
                ch=int(input("Do you want to Retrieve more  record for Zain? \n1.Yes \n2.No\n"));
                if ch==1:
                  continue;
                else:
                  break;
            else:
                f=open("Zain exe.txt","r");
                print(f.readlines());
                f.close();
                ch=int(input("Do you want to retrieve more record for Zain? \n1.Yes \n2.No\n"));
                if ch==1:
                  continue;
                else:
                  break;
print("\n\n\n\t\t*************************************\n")
print("\t\tWELCOME TO HEALTH MANAGEMENT SYSTEM\n");
print("\t\t*************************************\n");
print("What Do you want to do:");
i=int(input("Enter a choice:\n1.log \n2.retrieve\n"));
if i==1:
    log();
elif i==2:
    retrieve();
else:
    print("Worng input!!!!");

