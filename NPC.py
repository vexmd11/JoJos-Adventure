#NPC.py
#Description: NPC class is a sub class of interactable class. Has the same functions as an interactable object but uses specific
#               NPC sprites and methods to handle NPC movement. Used in collision.
#Name: Michael Bassani
#Created: Nov 20, 2017
#Last Modified: Feb 1, 2018
__author__ = 'Michael Bassani'

import pygame
from LoadImages import *
pygame.init()

from Interactable import *

class NPC(Interactable):

    #~~~~~~~~Constructor~~~~~~~~#
    def __init__(self, rect, npcNum, text, name):
        self.rect = rect
        self.name = name
        self.text = text
        self.spoken = False
        if npcNum == 1:
            self.spriteFront = npc1_front_sprite
            self.spriteRight = npc1_right_sprite
            self.spriteLeft = npc1_left_sprite
            self.spriteBack = npc1_back_sprite
        elif npcNum == 2:
            self.spriteFront = npc2_front_sprite
            self.spriteRight = npc2_right_sprite
            self.spriteLeft = npc2_left_sprite
            self.spriteBack = npc2_back_sprite
        elif npcNum == 3:
            self.spriteFront = npc3_front_sprite
            self.spriteRight = npc3_right_sprite
            self.spriteLeft = npc3_left_sprite
            self.spriteBack = npc3_back_sprite
        elif npcNum == 4:
            self.spriteFront = npc4_front_sprite
            self.spriteRight = npc4_right_sprite
            self.spriteLeft = npc4_left_sprite
            self.spriteBack = npc4_back_sprite
        elif npcNum == 5:
            self.spriteFront = npc5_front_sprite
            self.spriteRight = npc5_right_sprite
            self.spriteLeft = npc5_left_sprite
            self.spriteBack = npc5_back_sprite
        elif npcNum == 6:
            self.spriteFront = harold_front_sprite
            self.spriteRight = harold_right_sprite
            self.spriteLeft = harold_left_sprite
            self.spriteBack = harold_back_sprite
        self.sprite = self.spriteFront



    #~~~~~~~~Turning~~~~~~~~#
    def turn(self, index):
        if (index == 1):
            self.sprite = self.spriteFront
        elif index == 2:
            self.sprite = self.spriteBack
        elif index == 3:
            self.sprite = self.spriteLeft
        else:
            self.sprite = self.spriteRight
