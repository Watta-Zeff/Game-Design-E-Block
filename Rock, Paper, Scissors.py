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
print("_   $$________$$$$$$$$$_________$$$         --                             --        ")
print("   $__$$_____________________$$$$___$$         ----------------------------               ")
print(" $$$$$___$$$$$$$$______$$$$$$$_______$_$                             ")
print("$______$$_________$$$$$$______________$_$$                           ")
print("$____$____$____________________________$_$_$                        ")
print("$_____$___$______________$$$$$$$$$$$___$_$_$$                       ")
print("$$$____$___$__$$$$$$$$$$$$__________$___$_$_$$                      ")
print("$___$$$$____$__$_____________________$___$_$$_$                      ")
print("$$$____$___$$__$_____________________$$__$_$__$                      ")
print("$___$__$__$$___$______________________$__$$$__$                      ")
print("$_____$$_$$____$_______________$$$____$__$_$__$                      ")



computernum = random.randint(1,3)



GameOn=True


os.system('cls')



while(GameOn):

    if 'pap' in user:
        user =int(1)
    elif 'sci' in user:
        user =int(2)
    elif 'roc' in user:
        user =int(3)
