stg='hello world';
print(stg);
stg="hi hello world";
print(stg.rpartition(" hello "));
print(stg);
stg='Ali said,"I\'m busy today"';
print(stg);
stg='Hamza said that "I am busy tomorrow."'
print(stg);
stg='''"My name is Noman Amjad.
My father name is Muhammad Ayub ."'''
print(stg);
print(len(stg));
print(stg[0:5]);
#for loop use to show string.
for i in stg:
    print(i,end="");
print("\n");
#Built in function within string in python.
print(stg.upper());
print(stg.lower());
print(stg.capitalize());
x=stg.split(" ");
print("The split string is :",x);
print(stg.replace("\"","'"));#jo replace krni ha wo first likhni ha 2 jo os jga rakhni ha.
#---Adding a string---
s="Noman";
st="Amjad";
name=s+" "+st;
print(name);
s1="hey";
s2="That's";
s3="Good";
st="() (), ()!".format(s1,s2,s3);
print(st);