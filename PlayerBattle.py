#PlayerBattle.py
#Description: This class controls the player in battle sequences. It keeps track of position, health, attack power, and move/attack
#               radius. It has methods that allow it to interact with enemy movements or attacks.
#Name: Michael Bassani
#Created: Nov 20, 2017
#Last Modified: Feb 1, 2018

__author__ = 'Michael Bassani'
import pygame
pygame.init()

class PlayerBattle:

    xPos = 0
    yPos = 0
    hitbox = pygame.Rect(xPos, yPos, 75, 70)
    health = 100
    closeAttackPower = 10
    rangedAttackPower = 7
    closeAttackRadius = 1
    rangedAttackRadius = 3
    moveRadiusRects = []
    attackRadiusRects = []

    def __init__(self, xPos, yPos, sprite):
        self.xPos = xPos
        self.yPos = yPos
        self.sprite = sprite
        self.hitbox = pygame.Rect(xPos, yPos, 75, 70)

    def move(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def takeDamage(self, damage):
        self.health-= damage

    def attack(self, player):
        player.health -= self.rangedAttackPower

    def specialAttack(self, player):
        player.health -= self.closeAttackPower


