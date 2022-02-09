#Zeffaniah Sadler-Knight
2/8/22
# Word game with 3 levels: 
#        1. Fruits    
#        2. Animals 
#        3. Computer Parts    
# Choice:

#Create word lists
import os, random
os.system('cls')
word=""
guess=""
def selectWord():
    global word
    fruits=["bananas", "grapes", "waterMelon", 'blueberries', 'apples', "blackberries",
    "papaya", 'oranges', 'tomatoes', 'mangos', 'kiwis','strawberries' ]

    # size= len(fruits)
    # randy= random.randint(0,size)
    # print(randy)
    # word=fruits[randy]
    # print(word)
    word=random.choice(fruits)

def guessFunction():
    global guess
    check=True
    while check:
        try:
            guess=input("\nenter a letter to guess the word ")
            if guess.isalpha() and len(guess)==1:
                check=False
            else:
                print("only one letter please")
        except ValueError:
            print("only one letter please")
            
gameOn=True
tries=0
letterGuessed=""
selectWord()
while gameOn:
    
    guessFunction()
    letterGuessed += guess  #letterGuessed=letterGuessed + guess
    if guess not in word:
        tries +=1
        print(tries)# for testing delete when game is ready
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print(letter, end=" ")
            countLetter +=1
        else:
            print("_", end=" ")
    if tries >6:
        print("\n Sorry you ran out of chances ")
        #playGame() ask if they want to play again
    if countLetter == len(word):
        print ("\nyou guessed! ")
        #Calculate score
        #playGame()