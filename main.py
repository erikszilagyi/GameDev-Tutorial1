import pygame, sys, time

#initialize pygame so that we can use all of the built in functions in the pygame library
pygame.init()

windowSize = (800,600)

screen = pygame.display.set_mode(windowSize)

myriadProFont = pygame.font.SysFont("myriadProFont",48)

helloWorldText = myriadProFont.render("hello world",1, (100,100,255),(255,255,255))

x,y = 0,0

while 1:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: sys.exit()


    screen.blit(helloWorldText, (x,y))

    pygame.display.update()