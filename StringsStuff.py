# #Zeffaniah Knight
# 01/31/2022
# strings array of characters
# Has many functions
import os

os.system('cls')

MyName= 'Zeffaniah Knight'

# each letter or number has a block starting with 0

MyStatement=""" My Name is so nice because
blah blah blagggg

what ever
ever"""

print (MyName[10])
print (MyStatement)

print ("My last name begins with " +MyName[6])

if 'blah' in MyStatement:
    print('true')
print('expert' not in MyStatement)
#find() will return the index of the character you are looking for.
INDEX= MyName.find(" ")
print(INDEX)