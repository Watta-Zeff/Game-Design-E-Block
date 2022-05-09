#Zeffaniah Knight
#Lists and List Methods

import os, random
os.system('cls')

fruits=["bananas", "grapes", "waterMelon", 'blueberries', 'apples', "blackberries",
    "papaya", 'oranges', 'tomatoes', 'mangos', 'kiwis','strawberries' ]
#length of your array
size= len(fruits)
print(size)
fruits.append("rambutan")
for i in range(size+1):# 13 is not included
    print(fruits[i])
print(fruits[size-1])
print(fruits[-2])
print(fruits.count('bananas'))
list2=[3,6,8,9,10]
fruits.append(list2)
print(fruits)
fruits.extend(list2)
print("extend \n",fruits)
fruits.pop(-1)
fruits.extend(list2)
print("extend \n",fruits)
fruits.insert(2, "dragonfruit")