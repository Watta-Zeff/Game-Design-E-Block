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
name=''


print(date.strftime('%m/%d/%Y'))

ScoreLine=str(score)+" "+name+" "+date.strftime('%m/%d/%Y'+'\n')
print(ScoreLine)
#open file and write
myFile=open('sce.txt', 'a')
myFile.write(ScoreLine)
myFile.close()
myFile=open('sce.txt')
lines=myFile.readline()
print(lines)
lines=myFile.readline()
print(lines)
myFile.close()

