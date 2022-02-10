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

def menu():
    print("*******************************************************")
    print("*                                                     *")
    print("*                                                     *")
    print("*                 Word Guessing Game                  *")
    print("*                                                     *")
    print("*                    Choose from                      *")
    print("*                       Fruits                        *")
    print("*                       Animals                       *")
    print("*                  or Computer Parts                  *")
    print("*                                                     *")
    print("*******************************************************")






def selectWord():
    global word
    fruits=["bananas", "grapes", "waterMelon", 'blueberries', 'apples', "blackberries",
    "papaya", 'oranges', 'tomatoes', 'mangos', 'kiwis','strawberries' ]
    animals=["dog", "cat", "crocodile", "squid", "monkey", "shark", "spider", "snake",
    "snail", "lion", "salmon", "gorilla", "horse", "cow", "lizard" ]
    computerparts=["motherboard", "battery", "wires", "cpu", "fans", "chassis", "rgb",
    "ram", "storage", "computer" ]

    # size= len(fruits)
    # randy= random.randint(0,size)
    # print(randy)
    # word=fruits[randy]
    # print(word)
    check = True
    while check:
        try:
            choice= int(input("Choice: "))
            if choice > 0 and choice < 4:
                check = False
        except ValueError:
            print("Sorry try again")

        if choice==1:
            word=random.choice(fruits)
        elif choice==2:
            word=random.choice(animals)
        elif choice ==3:
            word=random.choice(computerparts)

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
menu()
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
def endgame():
    print("*****************************************")
    print("*                                       *")
    print("*                                       *")
    print("*             Game----Over              *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*****************************************")