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

##def main():
##    pass
##
##if __name__ == '__main__':
##    main()
import pyttsx3

def main():
    print("\t\t\t\t\tWelcome to RoboSpeaker 2.3\n\n\t\t\t\t\t\t 'Created by Noman'")
    while True:
        print("\n*******************************************")
        print("\nAvailable Options:")
        print("1. Speak a sentence")
        print("2. Change voice rate")
        print("3. Change voice volume")
        print("4. Quit")
        print("********************************************")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            sentence = input("Enter the sentence to speak: ")
            speak(sentence)
        elif choice == '2':
            rate = float(input("Enter the voice rate (default: 1.0): "))
            change_rate(rate)
        elif choice == '3':
            volume = float(input("Enter the voice volume (default: 1.0): "))
            change_volume(volume)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def change_rate(rate):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)

def change_volume(volume):
    engine = pyttsx3.init()
    engine.setProperty('volume', volume)

if __name__ == '__main__':
    main()
