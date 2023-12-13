# This file was created by Alejandro Torres

#import libraries
import pygame
import random
import sys
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10), Vector2(3,10)] #putting 3 blocks next to each other to make body of snake
        self.direction = Vector2(0,0) #position of snake head and where the w,a,s,d keys will begin to start
        self.new_block = False

    def draw_snake(self):
        for block in self.body: #create a rectangle
            x_pos = int(block.x * cell_size) #turn to integer value 
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos, cell_size,cell_size) 
            pygame.draw.rect(screen,(135,206,250),block_rect) #drawing snake

    def move_snake(self):
            if self.new_block == True: 
                body_copy = self.body[:] #element at end dissapears
                body_copy.insert(0,body_copy[0] + self.direction) #adding element at front so snake moves forward
                self.body = body_copy[:]
                self.new_block = False #restricting snake growth to not be infinite
            else:
                body_copy = self.body[:-1] 
                body_copy.insert(0,body_copy[0] + self.direction) 
                self.body = body_copy[:]

    def add_block(self):
        self.new_block = True 

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)] #when game restarts snake will revert to orignal position
        self.direction = Vector2(0,0) #when game restarts snake will not keep moving on and keep its origianl direction
    
class FRUIT:
    def __init__(self):
        self.randomize() #randomize wherever the fruit spawns

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size),cell_size,cell_size) #positions of fruit
        pygame.draw.rect(screen,(220,20,60),fruit_rect) #color of fruit

    def randomize(self): 
        self.x = random.randint(0,cell_number-1) #-1 in order for randomization to not spawn off the screen
        self.y = random.randint(0,cell_number-1) #-1 in order for randomization to not spawn off the screen
        self.pos = Vector2(self.x,self.y) 

class MAIN:
    def __init__(self):
        self.snake = SNAKE() 
        self.fruit = FRUIT()

    def update(self): #checking for whenever the following happen, the game will update to keep up with it
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self): #drawing all elements that I have created
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: #when snake eats fruit
              self.fruit.randomize() #when collided with fruit, new fruit will spawn in random location
              self.snake.add_block() #when collided with fruit snake will have a block added to it

        for block in self.snake.body[1:]: #if fruit spawns on snake when the game starts
            if block == self.fruit.pos: # if fruit spawns in on snake at the random chance, then it will randomize again
                self.fruit.randomize()

    def check_fail(self): #check if snake is outside of screen and if it hits itself
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number: #sets boundaries for x and y
            self.game_over() #if snake touches boundaries of the game the game will end

        for block in self.snake.body[1:]: #if snake touches itself the game will end
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset() #when the following two collisions happen then the game will restart to how it orignally was
    
    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number): #making grass spawn in at every other row
            if row % 2 == 0:
                for col in range(cell_number): #making grass spawn in at every other column
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
    def draw_score(self):
        score_text = str(len(self.snake.body)-3)  #length of snake determines score, -3 because snake orignally starts with 3 blocks
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        screen.blit(score_surface,score_rect)


pygame.init() #module in pygame
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock() 
game_font = pygame.font.Font(None, 25)

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
            if event.key == pygame.K_w:
                if main_game.snake.direction.y != 1: #if you go up you cannot go down
                    main_game.snake.direction = Vector2(0,-1) #-1 to y to move up
            if event.key == pygame.K_d:
                if main_game.snake.direction.x != -1: # if you go to the right you cannot go left
                    main_game.snake.direction = Vector2(1,0) #+1 to x to move right
            if event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1) #+1 to y to move down
            if event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0) #-1 to x to move left

    screen.fill((175,215,70)) #RGB tuple
    main_game.draw_elements()
    pygame.display.update() #draw all elements of the game
    clock.tick(60) #how many frames per second the while loop can run for


