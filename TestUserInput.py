import os, random
os.system('cls')


myNumber=random.randint(1,10)
myNumber2=random.randint(1,50)
myNumber3=random.randint(1,100)

GameMenu=GameOn=True
userChoice=''
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

menu()

check=True
while check:
    try:
        userChoice=(input("choice: "))
        if userChoice =='a' or userChoice=='b' or userChoice =='c':
            check = False
    except ValueError:
        print("Sorry, wrong choice, please enter a number 1 to 3 only >:(")


while(GameMenu):

    if userChoice =='a':
        usernum = int(input("guess a number from 1-10 "))
        if usernum == myNumber:
            print("You guessed it!")
            break
            
        else:
            print("you got it wrong :(")
            print("The number to guess was "+ str(myNumber))
            break

    if userChoice =='b':
        usernum = int(input("guess a number from 1-50 "))
        if usernum == myNumber2:
            print("You guessed it!")
            break

        else:
            print("you got it wrong :(")
            print("The number to guess was "+ str(myNumber2))
            break
    if userChoice =='c':
        usernum = int(input("guess a number from 1-100 "))
        if myNumber3 ==userChoice:
            print("You guessed it!")
            break

        else:
            print("you got it wrong :(")
            print("The number to guess was "+ str(myNumber3))
            break

os.system('cls')

menu()