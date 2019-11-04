#Portal.py
#Description: Portal class is a sub class of Collider class. A portal is a solid object which is why it is a sub class, but has
#               different uses. The portal connects two scenes so the player can travel to different areas.
#Name: Michael Bassani
#Created: Nov 20, 2017
#Last Modified: Feb 1, 2018
import pygame, sys
from Collider import *

class Portal(Collider):

    def __init__(self, rect, newScene, newPlayerX, newPlayerY):
        self.rect = rect
        self.newScene = newScene
        self.newPlayerX = newPlayerX
        self.newPlayerY = newPlayerY

    def getNewPlayerX(self):
        return self.newPlayerX
    def getNewPlayerY(self):
        return self.newPlayerY
    def getNewScene(self):
        return self.newScene
