#Interactable.py
#Description: Sub class of Collider class. Same functions as a collider but has text that appears when interacted with.
#               Solid object and still used with collision.
#Name: Michael Bassani
#Created: Nov 20, 2017
#Last Modified: Feb 1, 2018

from Collider import *

class Interactable(Collider):

    def __init__(self, text, rect, sprite):
        self.text = text
        self.sprite = sprite
        self.rect = rect
        self.interacted = False

    def getText(self):
        return self.text
    def setText(self, text):
        self.text = text
