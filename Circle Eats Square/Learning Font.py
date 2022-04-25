
import pygame, time, random



WIDTH=700
HEIGHT=700
wb=30
hbox=30

colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75], 'crimson':[168,26,26], 'gray':[96,96,96], 'blreen':[43,255,171] }

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

pygame.init()
wind=pygame.display.set_mode((WIDTH,HEIGHT))
wind=pygame.display.set_caption("Circle Eats Square")
#create different type of fonts

TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
text=TITLE_FNT.render('He11', 1, (125,45,30))
wind.fill((255,255,255))
wind.blit(text,(50,50))
text=INST_FNT.render("Write your instructions",1,(0,255,0))
wind.blit(text,(220,220))

wind.blit(text,(50,200))
text=INST_FNT.render("---- W to Move Up ----")
wind.blit(text,(50,150))
text=INST_FNT.render("---- S to Move Down ----")
wind.blit(text,(50,100))
text=INST_FNT.render("---- A to Move Left ----")
wind.blit(text,(50,50))
text=INST_FNT.render("---- D to Move Right ----")
pygame.display.update()

pygame.time.delay(100000)



pygame.display.update()

pygame.time.delay(1000)