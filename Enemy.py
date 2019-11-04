#Enemy.py
#Description: Enemy class for battling in game. Keeps track of enemy health, attack, position, and radius of movement/attack.
#               Has some methods to make it interact with player attacks and movement.
#Name: Michael Bassani
#Created: Nov 20, 2017
#Last Modified: Feb 1, 2018

__author__ = 'Michael Bassani'
import pygame
pygame.init()

class Enemy:
    xPos = 0
    yPos = 0
    hitbox = pygame.Rect(xPos, yPos, 75, 70)
    health = 100
    attackPower = 5
    specialAttackPower = 8
    closeAttackRadius = 1
    rangedAttackRadius = 2
    moveRadiusRects = []
    attackRadiusRects = []

    def __init__(self, rect, sprite, health, attackPower, specialAttackPower):
        self.sprite = sprite
        self.hitbox = rect
        self.health = health
        self.attackPower = attackPower
        self.specialAttackPower = specialAttackPower
        self.doAnimate = False
        self.newRect = None
        self.hadTurn = False


    def move(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def takeDamage(self, damage):
        self.health-= damage

    def attack(self, player):
        player.health -= self.attackPower

    def specialAttack(self, player):
        player.health -= self.specialAttackPower


