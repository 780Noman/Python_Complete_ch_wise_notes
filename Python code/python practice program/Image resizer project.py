#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     13/07/2023
# Copyright:   (c) DELL 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import cv2

#configureable parameters
source="D:\\3rd semester doc\\Python code\\python practice program\\Nature.jpg"
destination="D:\\3rd semester doc\\Python code\\python practice program\\NewPic.png"
scale_percent =50

src= cv2.imread(source,cv2.IMREAD_UNCHANGED)
cv2.imshow("title",src)

#Percent by which the image is resized

#Calculate the 50 percent of original dimensions
new_width =int(src.shape[1]*scale_percent/100)
new_height=int(src.shape[0]*scale_percent/100)

#resize image
output = cv2.resize(src,(new_width,new_height))

cv2.imwrite(destination,output)
cv2.waitKey(0)


