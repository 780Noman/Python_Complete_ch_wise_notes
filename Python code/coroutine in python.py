#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     29/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Coroutine in python
'''Coroutine are used in cases of time-consuming programs, such as tasks related to machine learning or deep learning algorithms,or in cases
where the program has to read a file containing a large number of data.We do not want the program to read the file or data again and again.'''
def myfunc():
    print("Hello world....");
    while True:
        value=(yield);
        print(value);
coroutine=myfunc();#generator obj
next(coroutine);#next function is used for run the coroutine
coroutine.send("Python");#Used to send data to coroutine
coroutine.send("Tutorial ");
coroutine.close();#Used for closing the coroutine.

###################################
def searcher():
    import time
    #some 4 seconds time consuming task
    book="This is book of author roobert lafore .He was a great programmer.He writes many books on C++ programming languages.";
    time.sleep(4);

    while True:
        text=(yield);
        if text in book:
            print("Your text is in the book.");
        else:
            print("Your text is not in the book.");

search=searcher();
next(search);
print("Next method run..");
search.send("programmer");
input("Press any key:");
'''coroutine not waiting 4 second for next call its run next code of while block'''
search.send("Hello");
##input("Press any key:")
##search.send("Hello");
##input("Press any key:")
##search.send("Hello");
search.close();

