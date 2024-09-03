#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     03/09/2022
# Copyright:   (c) DELL 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Create a game (snake water gun).
"""If you choose a snake and random function choose water then you are winner.
if you choose a snake and random fun choose a gun then you are loss the game.
if you choose a gun and random fun choose a water then you are loss the game .
you can try this game only 5 time and after that show the result how had the winner ?"""

import random

print("Enter Numbers of rounds  do you want to play :");
rounds=int(input());
d_rounds=0;
p_p=0;
c_p=0;
draw=0;
while(rounds>=1):
    c_list=["Snake","Water","Gun"];
    c_choice=random.choice(c_list);

    print("Enter your choice : \n1.Snake \n 2.Water \n3.Gun");
    p_choice=input();

    if p_choice=="Snake":
        if c_choice=="Snake":
            print("Draw !!!\n");
            draw+=1;
        elif c_choice=="Water":
            print("You Win");
            p_p+=1;
        else:
            print("Computer Win");
            c_p+=1;
        d_rounds+=1;
    elif p_choice=="Water":
        if c_choice=="Water":
            print("Draw !!!");
            draw+=1;
        elif c_choice=="Snake":
            print("Computer Win");
            c_p+=1;
        else:
            print("You win");
            p_p+=1;
        d_rounds+=1;
    elif p_choice=="Gun":
        if c_choice=="Gun":
            print("Draw !!!");
            draw+=1;
        elif c_choice=="Water":
            print("Computer Win");
            c_p+=1;
        else:
            print("You win");
            p_p+=1;
        d_rounds+=1;
    else:
        print("Invalid Input");
    rounds-=1;
print("_______Game Over___________\n")
print("''''''Total score''''''' ");
print("\nNo.of rounds draw between cpu and player is :");
print(f"{d_rounds} rounds");
print(f"No. of time player  won :{p_p}");
print(f"No.of time cpu won :{c_p}");
print(f"No. of time draw the Game :{draw}");
if c_p==p_p:
    print("GAME TIE\n");
elif c_p>p_p:
    print("Computer win and you loose !!!!!!!!\n");
else:
    print("You win and computer loose !!!!!!!\n" )


