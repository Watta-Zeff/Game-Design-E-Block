#Zeffaniah Sadler-knight
#1/21/22

#We are going to learn the input() function
# type casting branching. looping

#declare variable for user inout

import os, random
os.system('cls')


# print("enter a number from 1-10:",end=" ")

#  #input returns a string5


# useless=int(input())
# print("the number is %.2f " %(useless/3))

# guess=int(input("please give a number"))

#guess a number
# myNumber = 9

myNumber=random.randint(1,10)
myNumber2=random.randint(1,50)
MyNumber3=random.randint(1-100)
print("###############################################################")
print("#                                                             #")
print("#                       Guess a number                        #")
print("#                                                             #")
print("###############################################################")

GameOn=True
while(GameOn):
    UserGuess=int(input("guess a number from 1-10 "))
    if myNumber ==UserGuess:
        print("You guessed it!")
        GameOn=False
    else:
        print("you got it wrong :(")
print("The number to guess was "+ str(myNumber))