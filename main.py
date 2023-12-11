# This file was created by Alejandro Torres

#import libraries
import pygame
import random
import sys
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10), Vector2(7,10)] #putting 3 blocks next to each other
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body: #crreate a rectangle
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos, cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122),block_rect)

    def move_snake(self):
        body_copy = self.body[:-1] #element at end dissapears
        body_copy.insert(0,body_copy[0] + self.direction) #adding element at front so snake moves forward
        self.body = body_copy[:]


class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number-1) #-1 in order for random to not spawn off screen
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()

    def draw_elements(self):
            self.fruit.draw_fruit()
            self.snake.draw_snake()

pygame.init() #module in pygame
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock() 



SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) #triggered every 150 milliseconds

main_game = MAIN()

while True:
    for event in pygame.event.get(): #event loop is a user input 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #ends code that is ran off (closes code)
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0,-1) #-1 to y to move up
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1,0) #+1 to x to move right
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0,1) #+1 to y to move down
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1,0) #-1 to x to move left

    screen.fill((175,215,70)) #RGB tuple
    main_game.draw_elements()
    pygame.display.update() #draw all elements of the game
    clock.tick(60) #how many frames per second the while loop can run for


