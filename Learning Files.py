#Zeffaniah Knight
#Learning Files
# a) open/create a file 
# b) write 'w'
# c) append 'a' 
# d) read 'r' 
# e) close()

import pygame, os, datetime
os.system('cls')
date=datetime.datetime.now()
score=123
name='Watta'
print(date.strftime('%m/%d/%Y'))

ScoreLine=str(score)+" "+name+" "+date.strftime('%m/%d/%Y')
print(ScoreLine)
#open file and write
myFile=open('sce.txt', 'a')
myFile.write(ScoreLine)

myFile.close()

