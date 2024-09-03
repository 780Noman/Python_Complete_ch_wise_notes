#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     28/07/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Passing argument from a functions.
def fun(*args):
    for i in args:
     print (i);
fun(19,29,24,'a','arguments');
#Another way is assignvalue show-------
print("Assign variable passing through function");
def fun1(*args,**kwargs):
    for keys,values in kwargs.items():
        print(keys,"is",values);
fun1(a=10,b=30,c='xyz');
#Nested function -------------------
def fun1():
    x=10;
    def fun2(x):
        return x+1;
    return fun2(x);
num=fun1();
print(num);
#Other nested function concept...
def func(called_fun):
    print("This is the first function.");
    def Nested_fun(called_fun):
        print("This is the nested function.");
        called_fun
    return Nested_fun(called_fun);
def outer_fun():
    print("This is the outer function.");
obj=func(outer_fun())
#creating a class at run time--------------------
#factory
B=type("Baseclass",(object,),{});
C1=type('C1',(B,),{'val':5});
C2=type('C2',(B,),{'val':10});

def classCreater(bool):
    if bool:
        return C1();
    else:
        return C2();

print(classCreater(True).val);
print(classCreater(False).val);

#Code with Harry

def funargs(*args):
    print(type(args))
    for i in args:
        print(i);
li=["ali","Ahmed","Arslan","Zain"];
funargs(*li);

def fun_args_kwargs(normal,*args,**kwargs):
    print(normal);
    for key,value in kwargs.items():
        print(f"{key} is a {value}");
di={"Hello" : "One","Murtaza":"Two","Usman":"Three"};
normal="This is the counting from 1 to 3 :";
fun_args_kwargs(normal,*li,**di)