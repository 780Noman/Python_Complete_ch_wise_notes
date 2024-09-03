#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     05/08/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import pandas as pd
import numpy as np
#String in dataframe in pandas library...
string=pd.Series(['AA','B','COW',np.nan,'BBA','OWL']);
print(string);

#some operation on pandas string............
print(string.str.lower());
print(string.str.upper())