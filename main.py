# This file was created by Alejandro Torres

#import libraries
import pygame
import sys
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self,x = 5
        self.y = 4
        self.pos = Vector2(self.x,self.y) #storing 2d data
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x,self.pos.y,cell_size,cell_size)
        pygame.draw.rect(surface,color,rectangle)

pygame.init() #module in pygame
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock() 

while True:
    for event in pygame.event.get(): #event loop is a user input 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #ends code that is ran off (closes code)

    screen.fill((175,215,70)) #RGB tuple
    pygame.display.update() #draw all elements of the game
    clock.tick(60) #how many frames per second the while loop can run for


