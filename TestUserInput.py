import os, random
os.system('cls')

Choice1='a'
Choice2='b'
Choice3='c'



myNumber=random.randint(1,10)
myNumber2=random.randint(1,50)
myNumber3=random.randint(1-100)

GameMenu=GameOn=True

print("###############################################################")
print("#                                                             #")
print("#                       Guess a number                        #")
print("#                                                             #")
print("###############################################################")

print("a = 1-10")
print("b = 1-50")
print("c = 1-100")


while(GameMenu):
    userChoice=(input("Choose a difficulty "))

    if userChoice =='a'(input("guess a number from 1-10 "))
    if myNumber ==userChoice:
        print("You guessed it!")
        GameOn=False
    else:
        print("you got it wrong :(")
print("The number to guess was "+ str(myNumber))

    if userChoice =='b'(input("guess a number from 1-50 "))
    if myNumber2 ==userChoice:
        print("You guessed it!")
        GameOn=False
    else:
        print("you got it wrong :(")
    print("The number to guess was "+ str(myNumber))

    if userChoice =='c'(input("guess a number from 1-100 "))
    if myNumber3 ==userChoice:
        print("You guessed it!")
        GameOn=False
    else:
        print("you got it wrong :(")
    print("The number to guess was "+ str(myNumber))
