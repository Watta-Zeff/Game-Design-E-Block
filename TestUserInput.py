import os, random
os.system('cls')

Choice1='a'
Choice2='b'
Choice3='c'



myNumber=random.randint(1,10)
myNumber2=random.randint(1,50)
myNumber3=random.randint(1,100)

GameMenu=GameOn=True

print("###############################################################")
print("#                                                             #")
print("#                       Guess a number                        #")
print("#                                                             #")
print("#                          a = 1-10                           #")
print("#                          b = 1-50                           #")    
print("#                          c = 1-100                          #")
print("#                       Choose a difficulty                   #")
print("###############################################################")



while(GameMenu):
    userChoice=(input("choice: "))

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