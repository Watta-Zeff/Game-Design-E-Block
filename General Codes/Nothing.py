import os, random
os.system('cls')
def menu():
    print("*                           *")
    print("*                           *")
    print("*    Guess a number menu    *")
    print("*                           *")
    print("*                           *")
    print("*        [1] 1-10           *")
    print("*        [2] 1-50           *")
    print("*        [3] 1-100          *")

#DECLARE ALL VARIABLES1
#How do we ask the user for choice
guess=0# by declaring the variable here is global variable
level=0
gameType=''

#check for the right input
# try/except
menu()  #calling the menu function
check=True
while check:
    gameType=input("Please select a level of the game ")
    try:
        gameType=int(gameType)
        if gameType >0 and gameType<4:
            check=False
        print("\nPlease enter a number between 1 and 3")
    except ValueError:
        print("Sorry, wrong input try again")

def randomNum(gameType):
    global level
    global guess
    if gameType== 1:
        guess=random.randint(1,10)  #local variable
        level=10
    if gameType==2:
        guess=random.randint(1,50)  #local variable
        level=50
    if gameType==3:
        guess=random.randint(1,100)  #local variable
        level=100

randomNum(gameType) #this is the call of the function
#ADD a MEnu

# choices  1-10
# choices 1 -50
# choices 1-100

#Select your choice

gameOn=True
#looping with condition

counter=0
