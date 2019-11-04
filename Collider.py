#Collider.py
#Description: Collider class for all solid objects in game. Has a hit box and sprite. Used for collision.
#Name: Michael Bassani
#Created: Nov 20, 2017
#Last Modified: Feb 1, 2018

import pygame
class Collider:

    rect = pygame.Rect(0,0,1,1)

    def __init__(self, rect, sprite):
        self.sprite = sprite
        self.rect = rect

    def getSprite(self):
        return self.sprite
    def getRect(self):
        return self.rect
