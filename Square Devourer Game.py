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
from pickle import TRUE
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

#circle hitbox
c_wbox = 20
c_hbox = 20
xh = xc-(rad/1.5)
yh = yc-(rad/1.5)
hitbox=pygame.Rect(xh,yh,c_wbox,c_hbox)

#creating the rect object
square=pygame.Rect(xs,ys,wbox,hbox)

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle Eats Square')



#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75], 'crimson':[168,26,26], 'gray':[96,96,96], 'blreen':[43,255,171], 'black':[0,0,0] }



MAIN =True
INST= False
Settings = False
Level1 = False
Level2 = False
Level3 = False
Score=False
Exit = False


#List for messages 
MenuList=['Instructions', 'Settings', 'Level 1', 'Level 2', 'Level 3', 'Scoreboard', 'Exit']
SettingList=['Screen Size', 'Circle Color', 'Background Color']
#Get colors
background= colors.get('blreen')

cr_color=colors.get('red')
randColor=''
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor) == background:
            sq_color= colors.get(randColor)
            
        else:
            colorCheck=False

changeColor()
sq_color= colors.get(randColor)
    






#Menu / Instructions



#create different type of fonts

TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('arial.ttf', 40)
INST_FNT=pygame.font.SysFont('arial.ttf', 40)

def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (125,45,30))
    screen.fill((255,255,255))

    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
    #get the width of the text


#Create First Button


#Create square for menu
xMs=50
yMs=250
wb=50
hb=50

menu_sq=colors.get('black')

square=pygame.Rect(xMs,yMs,wbox,hbox)
#This function uses a parameter
def MainMenu(Mlist):
    txty=250
    menu_sq.y=250
    for i in range (len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(0,0,0))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen, menu_sq, square )
        square.y +=50
        txty+=50




pygame.display.update()

pygame.time.delay(1000)












# text=INST_FNT.render("---- W to Move Up ----")
# screen.blit(text,(50,250))
# text=INST_FNT.render("---- S to Move Down ----")
# screen.blit(text,(50,150))
# text=INST_FNT.render("---- A to Move Left ----")
# screen.blit(text,(50,100))
# text=INST_FNT.render("---- D to Move Right ----")






#Jump Code

MAX=10
jumpCount=MAX
JUMP=False

#End Game

while check:

    if MAIN:
        screen.fill(background)
        TitleMenu("Menu")
    MainMenu(MenuList)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False




#Keybinds
    keys=pygame.key.get_pressed() #this returns a list
    if case.type ==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        print(mouse_pos)
    if ((mouse_pos[0] >20 and mouse_pos [0] <60) and (mouse_pos[1] >250 and mouse_pos [1] <290)) or INST:
        MAIN=False
        screen.fill(background)
        TitleMenu('Instructions')
        INST=TRUE



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

# #Varun's:
# keys = pygame.key.get_pressed() #this returns a list
# if keys [pygame.K_a] and square.x >= move:
#     square.x-= move
# if keys [pygame.K_d] and square.x <WIDTH-wbox:
#     square.x += move 
# if keys [pygame.K_w] and square.y>=move:
#     square.y -= move
# if keys [pygame.K_s] and square.y<= HEIGHT-(hbox+move):
#     square.y += move
# #Circle movement
# if keys [pygame. K_LEFT] and xc >=move:
#     xc-=move
#     hitbox.x-=move
# if keys [pygame. K_RIGHT] and xc <= WIDTH -move:  
#     xc+=move
#     hitbox.x+=move
# if keys [pygame. K_UP] and yc >=move:  
#     yc-=move
#     hitbox.y-=move
# if keys [pygame. K_DOWN] and yc <= HEIGHT -move:
#     yc+=move
#     hitbox.y+=move 
# #collisions
# if square.colliderect(hitbox):
#     xs=random.randint(0,WIDTH-wbox)
#     ys=random.randint(0, HEIGHT-hbox)
#     changeColor()
#     sqcolor=colors.get(randColor)
#     square = pygame.Rect(xs,ys,wbox,hbox)
#     rad+=10
#     c_wbox+=13.5
#     c_hbox+=13.5
#     xh=xc-(rad/1.5)
#     yh=yc-(rad/1.5)
#     hitbox=pygame.Rect(xh,yh,c_wbox,c_hbox)