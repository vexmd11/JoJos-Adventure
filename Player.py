#Player.py
#Description: Player class that handles all player related interactions in the game world. States like player position, speed,
#               animation index, sprites, and velocity are used to control player movement and animation, as well as move methods.
#               Player collision with other objects are also handled in this class through methods which includes NPC, Interactable,
#               and Collider classes.
#Name: Michael Bassani
#Created: Nov 20, 2017
#Last Modified: Feb 1, 2018
import pygame
from pygame.locals import *
from Portal import*
from NPC import*
from Collider import *
from Interactable import *
from Scene import *

pygame.init()

class Player:
    # <editor-fold desc = "Player States">
    xVel = 0
    yVel = 0
    speed = 3
    health = 100
    animationIndex = 0
    vertical = True
    # </editor-fold>

    # <editor-fold desc = "Player Sprites">
    standforward = pygame.transform.scale(pygame.image.load("Player Sprites/p_standforward.png"), (50, 50))
    standback = pygame.transform.scale(pygame.image.load("Player Sprites/p_standback.png"), (50, 50))
    standleft = pygame.transform.scale(pygame.image.load("Player Sprites/p_standside.png"), (50, 50))
    standright = pygame.transform.flip(standleft, True, False)

    runforward_1 = pygame.transform.scale(pygame.image.load("Player Sprites/p_runforward_1.png"), (50,50))
    runforward_2 = pygame.transform.scale(pygame.image.load("Player Sprites/p_runforward_2.png"), (50,50))
    runforward = [standforward, runforward_1, standforward, runforward_2]

    runleft_1 = pygame.transform.scale(pygame.image.load("Player Sprites/p_runside_1.png"), (50,50))
    runleft_2 = pygame.transform.scale(pygame.image.load("Player Sprites/p_runside_2.png"), (50,50))
    runleft = [standleft, runleft_1, standleft, runleft_2]
    runright_1 = pygame.transform.flip(runleft_1, True, False); runright_2 = pygame.transform.flip(runleft_2, True, False)
    runright = [standright, runright_1, standright, runright_2]

    runback_1 = pygame.transform.scale(pygame.image.load("Player Sprites/p_runback_1.png"), (50,50))
    runback_2 = pygame.transform.scale(pygame.image.load("Player Sprites/p_runback_2.png"), (50,50))
    runback = [standback, runback_1, standback, runback_2]
    sprite = standright
    # </editor-fold>

    #~~~~~~~~Constructor~~~~~~~~#
    def __init__(self):
        self.data = []
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.hitbox = pygame.Rect(xPos, yPos, 50, 50)
        self.blitted = False
        self.progress = 0
        self.timeWalking = 0
        self.money = 0
        self.inventory = []

    #~~~~~~~~Manage Position~~~~~~~~#
    # <editor-fold desc = "Get and Set Methods">
    #X Position
    def setXpos(self, xPos):
        self.xPos = xPos
    def getXpos (self):
        return self.xPos



    #Y Position
    def setYpos (self, yPos):
        self.yPos = yPos
    def getYpos (self):
        return self.yPos

    #~~~~~~~~~Manage Direction~~~~~~#
    def getXVel(self):
        return self.xVel
    def getYVel(self):
        return self.yVel

    #Method will return the correct sprite of the player at any time
    def getSprite(self):
        return self.sprite
    def setSprite(self, sprite):
        self.sprite = sprite

    #~~~~~~~Manage Speed~~~~~~~~~~#
    def setSpeed(self, speed):
        self.speed = speed
    def getSpeed(self):
        return self.speed
    # </editor-fold>

    def teleport(self, newPosX, newPosY):
        self.hitbox = pygame.Rect(newPosX, newPosY, 50, 50)

    def getHitbox(self):
        return self.hitbox



    def move(self, event):
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.yVel = -self.speed
                    self.sprite = self.standback
                    self.vertical = True
                    self.direction = "up"
                if event.key == K_DOWN:
                   self.yVel = self.speed
                   self.sprite = self.standforward
                   self.vertical = True
                   self.direction = "down"
                if event.key == K_LEFT:
                   self.xVel = -self.speed
                   self.sprite = self.standleft
                   self.vertical = False
                   self.direction = "left"
                if event.key == K_RIGHT:
                   self.xVel = self.speed
                   self.sprite = self.standright
                   self.vertical = False
                   self.direction = "right"
            if event.type == KEYUP:
                if event.key == K_UP:
                    self.yVel = 0
                    self.animationIndex = 1
                    self.sprite = self.standback
                elif event.key == K_DOWN:
                    self.yVel = 0
                    self.animationIndex = 1
                    self.sprite = self.standforward
                if event.key == K_LEFT:
                   self.xVel = 0
                   self.animationIndex = 1
                   self.sprite = self.standleft
                elif event.key == K_RIGHT:
                   self.xVel = 0
                   self.animationIndex = 1
                   self.sprite = self.standright
                if event.key == K_SPACE:
                    self.running = False

    def collision(self, scene):
        projected = pygame.Rect(self.hitbox.x + self.xVel + 10, self.hitbox.y + self.yVel + 30, 30, 15)
        for collider in scene.colliders:
            if (projected.colliderect(pygame.Rect(collider.getRect().x, collider.getRect().y + collider.getRect().height/4 , collider.getRect().width, collider.getRect().height/4 * 3))):
               return False
        for boundary in scene.boundaries:
            if (projected.colliderect(boundary.getRect())):
               return False
        for npc in scene.npcs:
            if (projected.colliderect(npc.getRect())):
               return False
        return True

    def interact(self,scene):
        for collider in scene.colliders:
            if (self.sprite == self.standback and collider.getRect().collidepoint(self.hitbox.x + 25, self.hitbox.y)) or (self.sprite == self.standright and collider.getRect().collidepoint(self.hitbox.x+ 50, self.hitbox.y+ 25)) or (self.sprite == self.standleft and collider.getRect().collidepoint(self.hitbox.x, self.hitbox.y+ 25))or (self.sprite == self.standforward and collider.getRect().collidepoint(self.hitbox.x + 25, self.hitbox.y + 50)):
                    if self.hitbox.colliderect(collider.getRect()):
                        if isinstance(collider, Interactable):
                                    return collider
                        elif isinstance(collider, Portal):
                                    return collider
        return ""

    def interactNPC(self, scene):
        for i in range(0, len(scene.npcs)):
            if self.hitbox.colliderect(scene.npcs[i].getRect()):
                if (self.sprite == self.standback and scene.npcs[i].getRect().collidepoint(self.hitbox.x + 25, self.hitbox.y)) or (self.sprite == self.standright and scene.npcs[i].getRect().collidepoint(self.hitbox.x+ 50, self.hitbox.y+ 25)) or (self.sprite == self.standleft and scene.npcs[i].getRect().collidepoint(self.hitbox.x, self.hitbox.y+ 25))or (self.sprite == self.standforward and scene.npcs[i].getRect().collidepoint(self.hitbox.x + 25, self.hitbox.y + 50)):
                    return i
        return ""

    def animate(self):
        if self.yVel > 0:
            if self.animationIndex > 3:
                self.animationIndex = 0
            self.sprite = self.runforward[self.animationIndex]
            self.animationIndex += 1
        elif self.yVel < 0:
            if self.animationIndex > 3:
                self.animationIndex = 0
            self.sprite = self.runback[self.animationIndex]
            self.animationIndex += 1
        elif self.xVel > 0:
            if self.animationIndex > 3:
                self.animationIndex = 0
            self.sprite = self.runright[self.animationIndex]
            self.animationIndex += 1
        elif self.xVel < 0:
            if self.animationIndex > 3:
                self.animationIndex = 0
            self.sprite = self.runleft[self.animationIndex]
            self.animationIndex += 1
