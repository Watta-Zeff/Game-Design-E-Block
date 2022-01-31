#1/27/22

#Zeffaniah Knight

#make menu

#import random

#import time

#Set random int to 1-3

#Tell computer to randomly generater number from 1-3

#ask user to pick rock paper or scissors

#if user input = computernum restart 

#if user input = paper and computernum = rock user win

#if user input = rock and computernum = scissors user win

#if user input = paper and computernum = scissors user loses

#if user input =  and computernum = rock user win

import os, random

import time

os.system('cls')


print("***********************************")
print("*                                 *")
print("*             Goodbye             *")
print("*                :(               *")
print("***********************************")








def menu():
    print("                                                                     ")
    print("                 $$$                                                 ")
    print("  ___________   $___$                                                ")
    print("  ____________   $$$                                                 ")
    print("______________   $_$                                                 ")
    print("_____________    $_$                                                 ")
    print("  _________  $$$_$$$                                                 ")
    print("   ______    $$__$$$__$$$                                            ")
    print("_______  $$__ $$$$$$$___$                                            ")
    print("  ____   $______________ _$                                          ")
    print("  ____   $_________________$                                         ")
    print("______   $_________________$                                         ")
    print("______   $_____$$$$$$$$$$$$$$$                                       ")
    print("______   $____$_______________$                                      ")
    print("_____    $____$___$$$$$$$$$$$$$                                      ")
    print("_____    $___$___$___________$$$                                     ")
    print("______   $___$___$_$$$___$$$__$$                                     ")
    print("______   $___$___$_$$$___$$$__$$                                     ")
    print("______   $___$___$___________$$$                                     ")
    print("______   $____$___$$$$$$$$$$$$$                                      ")
    print("______   $_____$$$$$$$$$$$$$$                    ------------------                       ")
    print("______   $____$____________$             --------                  --------                 ")
    print("______   $____$$$$$$$$$$$$$          ------      Rock paper Scissors        ------          ")
    print("______   $___$__$__$__$__$       -----                 The Game                  -----")
    print("______   $__$$$$$$$$$$$$$$  -------                                                 -------            ")
    print("______   $__$___$__$__$__$       -----                 Contols:                  -----                   ")
    print("______   $___$$$$$$$$$$$$$$$         -----    Make sure it is all lower case   -----                ")
    print("_____   $$$_________________$$$         ----           type out              ----    ")
    print("___   $$___$$$_________$$$$$___$$         ---      which one you want       ---       ")
    print("_   $$________$$$$$$$$$_________$$$         --   Rock , Paper , scissors   --        ")
    print("   $__$$_____________________$$$$___$$         ----------------------------               ")
    print(" $$$$$___$$$$$$$$______$$$$$$$_______$_$                                                      ")
    print("$______$$_________$$$$$$______________$_$$                                                 ")
    print("$____$____$____________________________$_$_$                                          ")
    print("$_____$___$______________$$$$$$$$$$$___$_$_$$                                             ")
    print("$$$____$___$__$$$$$$$$$$$$__________$___$_$_$$                                        ")
    print("$___$$$$____$__$_____________________$___$_$$_$                                       ")
    print("$$$____$___$$__$_____________________$$__$_$__$                                       ")
    print("$___$__$__$$___$______________________$__$$$__$                                       ")
    print("$_____$$_$$____$_______________$$$____$__$_$__$                                       ")

menu()

computernum = random.randint(1,3)


GameOn=True


while(GameOn):

    userchoice=input("Make Your Choice: ")

    if 'pap' in userchoice:
        userchoice =int(1)
    elif 'sci' in userchoice:
        userchoice =int(2)
    elif 'roc' in userchoice:
        userchoice =int(3)

    if userchoice == 1 and computernum == 1:
        print("User Tie")
        time.sleep(2)
        
    if userchoice == 1 and computernum == 2:
        print("Paper Lose")
        time.sleep(2)
        
    if userchoice == 1 and computernum == 3:
        print("Paper Wins")
        time.sleep(2)
        

    if userchoice == 2 and computernum == 2:
        print("User Tie")
        time.sleep(2)
        
    if userchoice == 2 and computernum == 3:
        print("Scissors Lose")
        time.sleep(2)
        
    if userchoice == 2 and computernum == 1:
        print("Scissors Wins")
        time.sleep(2)
        

    if userchoice == 3 and computernum == 3:
        print("User Tie")
        time.sleep(2)
        
    if userchoice == 3 and computernum == 1:
        print("Rock Loses to Paper")
        time.sleep(2)
        
    if userchoice == 3 and computernum == 2:
        print("Rock Wins Over Scissors")
        time.sleep(2)
        
    os.system('cls')

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

    endchoice=input("Make Your Choice: ")
    if 'Y' in endchoice:
        computernum = random.randint(1,3)
        os.system('cls')
        (menu)
    else:
        GameOn=False 