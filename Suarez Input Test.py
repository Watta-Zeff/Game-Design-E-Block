#Zeffaniah Sadler-knight
#1/21/22

#We are going to learn the input() function
# type casting branching. looping

#declare variable for user inout

import os, random
from traceback import print_stack
os.system('cls')


# print("enter a number from 1-10:",end=" ")

#  #input returns a string5


# useless=int(input())
# print("the number is %.2f " %(useless/3))

# guess=int(input("please give a number"))

#guess a number
# myNumber = 9


def menu():

    print("###############################################################")
    print("#                                                             #")
    print("#                       Guess a number                        #")
    print("#                                                             #")
    print("#                       Choice 1 = 1-10                       #")
    print("#                       Choice 2 = 1-50                       #")
    print("#                       Choice 3 = 1-100                      #")
    print("#                                                             #")
    print("###############################################################")
#Checking for correct user input

menu()  #calling the function menu
check=True
while check:
    try:

        choice=int(input("Choice: "))
        check = False
    except ValueError:
        print("Sorry, wrong choice, please enter a number 1 to 3 only >:(")

if choice == 1:
    myNumber=random.randint(1,10)
elif choice == 2:
    myNumber=random.randint(1,50)
elif choice == 3:
    myNumber= random.randint(1,100)
print(choice)

GameOn=True
while(GameOn):
    userGuess=int(input("Give me a number"))
    if myNumber ==userGuess:
        print("you guessed it!")
        GameOn=False
    else:
        print("Better Luck Next Time", myNumber)
print("The number to guess was " + str(myNumber))

os.system('cls')
menu()