#1/26/22
# Zeffaniah Knight

import os, random
import time
os.system('cls')


myNumber=random.randint(1,10)
myNumber2=random.randint(1,50)
myNumber3=random.randint(1,100)

GameMenu=GameOn=True
userChoice=''

endChoice=''



def endmenu():
    print("###############################################################")
    print("#                                                             #")
    print("#                                                             #")
    print("#                         play again?                         #")
    print("#                                                             #")
    print("#                                                             #")    
    print("#                      Y (Yes) or N (No)                      #")
    print("#                                                             #")
    print("#                                                             #")
    print("###############################################################")

def menu():

    print("###############################################################")
    print("#                                                             #")
    print("#                       Guess a number                        #")
    print("#                                                             #")
    print("#                          a = 1-10                           #")
    print("#                          b = 1-50                           #")    
    print("#                          c = 1-100                          #")
    print("#                                                             #")
    print("#                      Choose a difficulty                    #")
    print("###############################################################")

def randomnumgame():
    menu()

    check=True
    while check:
        try:
            userChoice=(input("choice: "))
            if userChoice =='a' or userChoice=='b' or userChoice =='c':
                check = False
        except ValueError:
            print("Sorry, wrong choice, please enter a number 1 to 3 only >:(")
            break

    # if choice>0 and choice <4
    #Check=False
        while(GameMenu):

            if userChoice =='a':
                usernum = int(input("guess a number from 1-10 "))
                if usernum == myNumber:
                    print("You guessed it!")
                    time.sleep(5)
                    break
                    
                else:
                    print("you got it wrong :(")
                    print("The number to guess was "+ str(myNumber))
                    time.sleep(5)
                    break

            if userChoice =='b':
                usernum = int(input("guess a number from 1-50 "))
                if usernum == myNumber2:
                    print("You guessed it!")
                    time.sleep(5)
                    break

                else:
                    print("you got it wrong :(")
                    print("The number to guess was "+ str(myNumber2))
                    time.sleep(5)
                    break
            if userChoice =='c':
                usernum = int(input("guess a number from 1-100 "))
                if myNumber3 ==userChoice:
                    print("You guessed it!")
                    time.sleep(5)
                    break

                else:
                    print("you got it wrong :(")
                    print("The number to guess was "+ str(myNumber3))
                    time.sleep(5)
                    break

os.system('cls')

endmenu()
while endChoice : (input(" "))

if endChoice =='y':
    randomnumgame()
if endChoice =='n':
    os.system('cls')
    print("goodbye")
