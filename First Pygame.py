import os, time
import pygame as p

#initialize pygame
p.init()
#define colors
white=[255,255,255]
red=[255,0,0]
mag=[255,0,255]
Aqua=[51,153,255]
mystery=[47,192,229]

#create your window/screen


width=600
height=700
screen=p.display.set_mode((width,height))

p.display.set_caption("My Window")
screen.fill(mystery)
p.display.update()
p.time.delay(5000)
screen.fill(red)
p.display.update()
p.time.delay(5000)
screen.fill(white)
p.display.update()
p.time.delay(5000)

#define a rectangle
#position
x=20
y=30
#w and h of rect
wbox=50
hbox=50
square=p.Rect(x,y,wbox,hbox)
square2=p.Rect(x+200, y+200, wbox, hbox)
run=True
while run:

    screen.fill(mag)

    for event in p.event.get():
        if event.type== p.QUIT:
            run =False
    p.draw.rect(screen,(white), square)
    p.draw.rect(screen,(red), square2)
    p.display.update()
    p.time.delay(100)
