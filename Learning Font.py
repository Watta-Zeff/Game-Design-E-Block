import pygame, time

pygame.init()
wind=pygame.display.set_mode((700,700))
wind=pygame.display.set_caption("testing")
#create different type of fonts

TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
text=TITLE_FNT.render('Daddy', 1, (125,45,30))
wind.fill((255,255,255))
wind.blit(text,(50,50))
text=INST_FNT.render("Write your instructions",1,(0,255,0))
wind.blit(text,(220,220))
pygame.display.update()

pygame.time.delay(1000)