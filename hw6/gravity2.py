# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 20:49:27 2014
Gravity Video Game!
@author: ychen1, mwelches, mborges
"""

import pygame
from pygame.locals import *
import random
import math
import time

class GravityModel:
    """ Encodes the game state of Gravity: will update the states of the junk and sandra (velocities, positions, and collisions"""
    def __init__(self):
        """ This function laysout the width, height, list of spacejunkms, time, and collisions """
        self.width = size[0]
        self.height = size[1]
        self.number_of_lives = 3
        self.spacejunkm = []
        self.int_time = 0
        self.collided = False
        self.wincollide = False
        
        for i in range(640/190):
            """ Next, we neeed to create a for loop that will add space junks to the spacejunk list that will be updated """
            for j in range(240/95):              
                new_b = SpaceJunkM(random.randint(60,640),random.randint(60,480), (random.randint(1,2)), (random.randint(1,2)),random.randint(20,40),random.randint(20,40), (random.randint(50,255),0,0))
                self.spacejunkm.append(new_b)
        self.sandra = Sandra(200,450,0,0)
            
    def update(self):
        """ This update function will be called in the main area that will be run """
        # sandra will be updated, in the fact that sandra's velocity and position changes with the direction the player chooses
        # the junk will be updated, in order to find junk's velocity and position changes
        # in order to find out whether or not the junk is colliding with sandra
        
        self.sandra.update()
        for junk in self.spacejunkm:
            junk.update()
            self.collided = self.sandra.sandra_collide(junk)
            if self.collided == True:
                break
        self.wincollide = self.sandra.sandra_win() 
                  
class SpaceJunkM:
    """ Encodes the state of a moving space junk """
    def __init__(self,x,y,vx,vy,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vx = vx
        self.vy = vy
        
    def update(self):
        self.x += self.vx #updates x position using velocity
        self.y += self.vy #updates y position

        Right_limit = 640 - self.width #sets the maximum amount space junk can travel to the right
        Left_limit = 0 #same as before but for left
        Up_limit = 0 #same as before but for the upper side
        Down_limit = 480 - self.height #same as before but for lower side
        
        moveHorz = True #assumes space junk can move horizontally
        moveVert = True
        
        if self.x >= Right_limit:
            moveHorz = False
            self.x = Right_limit-1 #stops space junk from leaving via right side
            self.vx = int(-self.vx) #gets space to bounce off the wall keeping the same magnitude
        if self.x <= Left_limit-1:
            moveHorz = False
            self.x = Left_limit + 1 #for left side
            self.vx = int(-self.vx)
        if self.y <= Up_limit: #for top
            moveVert = False
            self.y = Up_limit+1
            self.vy = int(-self.vy)
        if self.y >= Down_limit: #for bottom
            moveVert = False
            self.y = Down_limit - 1
            self.vy = int(-self.vy)
        if moveHorz == True: #if the space junk is not a a screen boundary it will move normally in x direction
            self.x += self.vx
        if moveVert == True: #same but for y direction
            self.y += self.vy
            
            
class Sandra:
    """ Encode the state of the Sandra Bullock """
    def __init__(self,x,y,width,height):
        """ determines the position, width, height, color and initial velocities of Sandra (velocity is controlled by the player in the update function)"""
        self.x = 20
        self.y = 20
        self.width = width
        self.height = height
        self.color = (255,255,255)
        self.vx = 0.0
        self.vy = 0.0
    
    def update(self):
        """the update function causes the velocity and movement of Sandra to not go beyond the screen boundaries.
        THIS is similar to space junk update function """
        Right_limit = 590
        Left_limit = 0
        Up_limit = 0 
        Down_limit = 440
        
        moveHorz = True
        moveVert = True
        
        if self.x >= Right_limit:
            moveHorz = False
            self.x = Right_limit-1
            self.vx = int(-self.vx/2)
        if self.x <= Left_limit-1:
            moveHorz = False
            self.x = Left_limit + 1
            self.vx = int(-self.vx/2)
        if self.y <= Up_limit:
            moveVert = False
            self.y = Up_limit+1
            self.vy = int(-self.vy/2)
        if self.y >= Down_limit:
            moveVert = False
            self.y = Down_limit - 1
            self.vy = int(-self.vy/2)
        if moveHorz == True:
            self.x += self.vx
        if moveVert == True:
            self.y += self.vy
            
    def sandra_collide(self,junk):
        """ this function checks to see if the object Sandra collides with the space junks (specifically checking for overlapping
         positions) """
        if self.x < junk.x < (self.x + junk.width) and self.y < junk.y < (self.y+ junk.height): #checks for overlapping positions
            return True
        else:
            return False
            
    def sandra_win(self):
        """ this function checks to see if the object Sandra collides with the spaceship on the opposite side (the corner with 
        the red space ship) """
        if self.x >= 560 and self.y >= 360: #checks for overlapping positions of sandra and the spaceship location
            return True
        else:
            return False
            
class PyGameWindowView:
    """ renders the GravityModel to a pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
    
    def draw(self):
        """ This function drawes out the space junks and Sandra """
        for b in self.model.spacejunkm: # b in spacejunkm indicates each junk within the spacejunklist
            pygame.draw.rect(self.screen, pygame.Color(b.color[0], b.color[1], b.color[2]), pygame.Rect(b.x, b.y, b.width, b.height))
        pygame.draw.rect(self.screen, pygame.Color(self.model.sandra.color[0], self.model.sandra.color[1], self.model.sandra.color[2]), pygame.Rect(self.model.sandra.x, self.model.sandra.y,self.model.sandra.width,self.model.sandra.height))
        pygame.display.update() # this updates the display of the model every single time the model is updated

class PyGameKeyboardController:
    """ Manipulate game state based on keyboard input """
    def __init__(self, model):
        self.model = model
    
    def handle_pygame_event(self, event):
        """ function dictates the movement of the object by the keyboard"""
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT: # moves objects left when left key is pressed
            self.model.sandra.vx += -1.0
        if event.key == pygame.K_RIGHT: # moves objects right when right key is pressed
            self.model.sandra.vx += 1.0
        if event.key == pygame.K_UP: # moves objects up when up key is pressed
            self.model.sandra.vy += -1.0
        if event.key == pygame.K_DOWN: # moves objects down when down key is pressed
            self.model.sandra.vy += 1.0
            
def you_win():
    """ Generates text (font, position, color and how long it stays on the screen before it closes) when you win"""
    font = pygame.font.Font(None, 90)
    text = font.render(str('You Win! Go Home!'), True, (224, 248, 255))
    textRect = text.get_rect()
    textRect.centerx = model.width-320
    textRect.centery = 240
    screen.blit(text, textRect)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()

def you_lose():
    """ Generates text (font, position, color and how long it stays on the screen before it closes) when you lose """
    font = pygame.font.Font(None, 65)
    text = font.render(str('You Lose! You are space junk!'), True, (224, 248, 255))
    textRect = text.get_rect()
    textRect.centerx = model.width-320
    textRect.centery = 240
    screen.blit(text, textRect)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    
if __name__ == '__main__':
    """ Runs the commands below immediately and generates the game and adds all of the components together """
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    model = GravityModel()
    view = PyGameWindowView(model,screen)
    controller = PyGameKeyboardController(model)
    running = True
    
    background_image = pygame.image.load("starsinthesky.jpg") 
    sandraimage = pygame.image.load("GravityBullock.png") # will replace the Sandra object with an actual picture
    screen_rect = screen.get_rect()    
    
    
    while running:
        screen.blit(background_image,[0,0]) #sets the background
        screen.blit(sandraimage, [model.sandra.x,model.sandra.y]) #sets the Sandra image to the moving object and model
        if model.wincollide: # indicates that when the object reaches the final destination (the wincollide will be true) and it will run the text of the you_win function
            you_win()
            running = False
        if model.collided: # indicates that when the object gets hit by another object (the collide will be true) and it will run the text of the you_lose function
            you_lose()
            running = False
        for event in pygame.event.get(): # quits the game
            if event.type == QUIT:
                running = False

                
            controller.handle_pygame_event(event)
        
        
        model.update()
        view.draw()
        time.sleep(.001)

        
    pygame.quit()