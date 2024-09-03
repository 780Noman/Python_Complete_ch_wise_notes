#*args and **kwargs 
#when we want to pass multiple arguments in function we use like list argument
def function(*args):
    if (len(args)==3):
        print("My name is ",args[0],"and my age is",args[1],"and my gender is",args[2])
    else:
        print("My name is ",args[0],"and my age is",args[1])
#when we want to pass multiple arguments in function we use like dictionary argument
def func_dict(**kwargs):
    for key,value in kwargs.items():
        print(key,"is",value)
def master(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,"is",value)

dic={"name":"Noman","age":19,"gender":"male","city":"Rawalpindi"}
func_dict(**dic);
lis=["Noman Amjad",20,"male"]
function(*lis)
function("Nomi",20,"male")
master("hi",*lis,**dic)