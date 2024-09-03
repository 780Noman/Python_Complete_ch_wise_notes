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
import PyPDF2

pdfiles= ["D:\\3rd semester doc\\Python code\\python practice program\\sample.pdf","D:\\3rd semester doc\\Python code\\python practice program\\1.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile=open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('D:\\3rd semester doc\\Python code\\python practice program\\merged.pdf')
print("Pdf file merged Succussfully ..... Go to location and check.......")