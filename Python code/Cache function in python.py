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
#######Function cache##############
'''Function caching is a way to improve code's performance by storing the function's return values.'''
import time
from functools import lru_cache

@lru_cache(maxsize=1)
def some_work(n):
    #some task taking n second
    time.sleep(n);
    return n;

if __name__=='__main__':
    print("Now running some work");
    some_work(10);
    print("Done...Calling again");
    some_work(12);
    print("Called again");
    some_work(13);
    print("HI");