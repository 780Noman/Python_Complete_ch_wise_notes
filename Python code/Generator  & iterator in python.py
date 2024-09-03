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
'''
Iterable = __iter__()  or __getitem__()
Iterator = __next__()
Iteration
'''
##for i in range(50):
##    print(i);

##create generator
def gen(n):
    for i in range(n):
        yield i;#Yeild mean  generate a value on the fly.
g=gen(3);
##print(g.__next__());
##print(g.__next__());
##print(g.__next__());
for i in g:
    print(i);

st="Noman";
##for ch in st:
##    print(ch);
ier=iter(st)
print(ier.__next__());
print(ier.__next__());
print(ier.__next__());
print(ier.__next__());
