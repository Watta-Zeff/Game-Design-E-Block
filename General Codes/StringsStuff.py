# #Zeffaniah Knight
# 01/31/2022
# strings array of characters
# Has many functions
import os

import os, random

os.system('cls')

MyName= 'Zeffaniah Knight'

# each letter or number has a block starting with 0

MyStatement=""" My Name is so nice because
blah blah blagggg

what ever
ever"""


print (MyName[10])
print (MyStatement)

print ("My last name begins with " +MyName[10])

if 'blah' in MyStatement:
    print('true')
print('expert' not in MyStatement)

#find() will return the index of the character you are looking for.

INDEX= MyName.find(" ")

print(INDEX)
wordLen=len(MyName)
print(wordLen) #your last index is len -1

print(MyName[8])

#for loop in range 0 to limit

for i in range(wordLen-1):
    if "a" in MyName[i]:
        print(i, end=", ")
print("")
print("done")

# MyStatement=MyStatement.lower()
# print(MyStatement)
# print("Thank you, the letter is "+ letter)
# if letter in MyStatement:
#     print ("Great")

check=True
while check:
    letter=input("Dear user, please give us a nice letter ")
#alpha is a function that makes sure that the input is only letters.
    if len(letter)>1 or not letter.isalpha():
        print("Bad")
    else:
        check=False
print("ready to play the game")



for elem in MyName:
    print(elem, end=" ")
guess=random.choice(MyName)
print(guess)
words=["Radio", "Clues", "suite", "peter", "robot"]
word=random.choice(MyName)
print(word)
for i in range(len(word)):
    if letter == word[i]:
        print(letter, end= " ")
    else:
        print("_", end=" ")
