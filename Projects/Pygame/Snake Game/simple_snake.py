# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:43:18 2018

@author: shakil
"""

import pygame
import random
pygame.init()

#colors
black=(0,0,0)
gold=(240,230,140)
maroon=(128,0,0)
crismon=(220,20,60)
white=(255,255,255)

display_width=600
display_height=400

gameDisplay=pygame.display.set_mode((display_width,display_height))

#caption
pygame.display.set_caption("Snake")

#icon
icon=pygame.image.load('snake.jpg')
pygame.display.set_icon(icon)

clock=pygame.time.Clock()
block_size=10
#frames per second
fps=21

#font
font=pygame.font.SysFont(None,25)

#score
def score(score):
    text=font.render("Score:"+str(score),True,crismon)
    gameDisplay.blit(text,[0,0])
    
def message_to_screen(msg,color,y_displace=0):
    textSurf=font.render(msg,True,color)
    textRect=textSurf.get_rect()
    textRect.center=(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)
    
def snake(block_size,snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay,maroon,[XnY[0],XnY[1],block_size,block_size])
    
def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    intro=False
                if event.type==pygame.K_q:
                    pygame.quit()
                    quit()
                    
                
        gameDisplay.fill(white)
        message_to_screen("Welcome to Snake",crismon,-70)
        message_to_screen("Eat the Apple!",crismon,-40)
        message_to_screen("Press P to play or Q to quit!",crismon,-10)
        pygame.display.update()
        
def gameLoop():
    gameExit=True
    
    lead_x=display_width/2
    lead_y=display_height/2
    
    lead_x_change=0
    lead_y_change=0
    
    snakeList=[]
    snakeLength=10
    
    randAppleX=round(random.randrange(0,display_width-block_size)/10.0)*10.0
    randAppleY=round(random.randrange(0,display_height-block_size)/10.0)*10.0
                    
    while gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    lead_x_change=block_size
                    lead_y_change=0
                elif event.key==pygame.K_LEFT:
                    lead_x_change=-block_size
                    lead_y_change=0
                elif event.key==pygame.K_UP:
                    lead_y_change=-block_size
                    lead_x_change=0
                elif event.key==pygame.K_DOWN:
                    lead_y_change=block_size
                    lead_x_change=0
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                    
        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
            pygame.quit()
            quit()
            
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,gold,[randAppleX,randAppleY,block_size,block_size])
        
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList)>snakeLength:
            del snakeList[0]
        
        snake(block_size,snakeList)
        
        score(snakeLength-10)
        
        pygame.display.update()
        
        if lead_x==randAppleX and lead_y==randAppleY:
            pygame.mixer.music.load('eat.wav')
            pygame.mixer.music.play(1)
            randAppleX=round(random.randrange(0,display_width-block_size)/10.0)*10.0
            randAppleY=round(random.randrange(0,display_height-block_size)/10.0)*10.0
            snakeLength+=1
        
        clock.tick(fps)
        
    pygame.quit()
    quit()
    
game_intro()
gameLoop()