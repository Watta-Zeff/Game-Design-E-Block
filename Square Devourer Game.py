#Zeffaniah Sadler-Knight
#learning how to draw circles and rectangles
#use keys to move objects
#Using Dictionaries

#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square, 
#circle will  get larger, and a new rect should appear somewhere on the screen
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE               Jump
#initialize pygame
import os, random, time, pygame
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700
check=True #for the while loop
move=5 #pixels
#square variables
xs=20
ys=20
wbox=30
hbox=30
#circle variables
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)
#creating the rect object
square=pygame.Rect(xs,ys,wbox,hbox)

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#Menu / Instructions
# pygame.init()
# wind=pygame.display.set_mode((700,700))
# wind=pygame.display.set_caption("Circle Eats Square Game")
# #create different type of fonts

# TITLE_FNT=pygame.font.SysFont('arial.ttf', 80)
# MENU_FNT=pygame.font.SysFont('arial.ttf', 40)
# INST_FNT=pygame.font.SysFont('arial.ttf', 30)
# text=TITLE_FNT.render('Watta', 1, (125,45,30))
# wind.fill((255,255,255))
# wind.blit(text,(50,50))
# text=INST_FNT.render("Write your instructions",1,(0,255,0))
# wind.blit(text,(220,220))
# pygame.display.update()

# pygame.time.delay(1000)

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75], 'crimson':[168,26,26], 'gray':[96,96,96], 'blreen':[43,255,171] }

#Get colors
background= colors.get('blreen')

cr_color=colors.get('red')
randColor=''
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if randColor == background:
            sq_color= colors.get(randColor)
            
        else:
            colorCheck=False

changeColor()
sq_color= colors.get(randColor)
    

#Jump Code

MAX=10
jumpCount=MAX
JUMP=False

#End Game

while check:
    screen.fill(background)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    

#Keybinds
    keys=pygame.key.get_pressed() #this returns a list
    if keys[pygame.K_a] and square.x >=move:
        square.x -= move #substract 5 from the x value
    if keys[pygame.K_d] and square.x <WIDTH-(wbox+move):
        square.x += move

    #Jumping Part
    if not JUMP:
        if keys[pygame.K_w] and square.y >= move:
            square.y -= move
        if keys[pygame.K_s] and square.y < HEIGHT - (hbox+move):
            square.y += move
        if keys[pygame.K_SPACE]:
            JUMP=True
    else:
        if jumpCount >=-MAX:
            square.y -= jumpCount*abs(jumpCount)/2
            jumpCount-=1
        else:
            jumpCount=MAX
            JUMP=False

    

#Finish circle
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xc >=rad+ move:
        xc -=move
    
    if keys[pygame.K_RIGHT] and xc < WIDTH - (rad+move):
        xc +=move

    if keys[pygame.K_UP] and yc >=rad+ move:
        yc -=move
    
    if keys[pygame.K_DOWN] and yc < HEIGHT - (rad+move) :
        yc +=move

    if keys[pygame.K_LEFT] and xc >=rad:
        xc -= move #substract 5 from the x value


#Check Collide
    CheckCollide = square.collidepoint((xc,yc))
    if CheckCollide:
        square.x=random.randint(wbox, WIDTH)
        square.y=random.randint(hbox, HEIGHT)
        changeColor()
        sq_color=colors.get(randColor)
        rad +=move

#Draw Rectangle and Circle
    pygame.draw.rect(screen, sq_color, square)
    pygame.draw.circle(screen, cr_color, (xc,yc), rad)

#Display Screen
    pygame.display.update()
    pygame.time.delay(10)


