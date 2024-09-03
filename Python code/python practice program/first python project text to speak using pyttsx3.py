#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     11/07/2023
# Copyright:   (c) DELL 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

##if __name__ == '__main__':
##    main()
###RoboSpeaker project
##import os
##print("\t\t\t\t\tWelcome to RoboSpeaker 2.3\n\n\t\t\t\t\t\t 'Created by Noman'")
##while True:
##    query=input("What do you want me to speak Now : ")
##    if query=='q':
##        break
##    command=f"[speaker]::speak {query}"
##    os.system(command)
#------------------------------------------------------------------------------
import pyttsx3

def main():
    print("\n\t\t\t\t\tWelcome To RoboSpeaker 3.4 \n\n\t\t\t\t\t\t\'Created by Nomi")
    while True:
        query=input("What do you Want me to Speak Now : ")
        if query=='q':
            speak("Bye Bye friend..")

            break
        speak(query)
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)#speech the provided text using say()
    engine.runAndWait()#ensure that text is spoken before go to next line

if __name__=='__main__':
     main()

