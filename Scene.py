#Scene.py
#Description: The scene class controls all objects and backgrounds portrayed in a room/scene. It uses a tile map to display the scene,
#               and has colliders, NPC's, passages to other scenes, and boundaries to control player interaction with everything.
#               A scene is made for every room in the game.
#Name: Michael Bassani
#Created: Nov 20, 2017
#Last Modified: Feb 1, 2018

class Scene:
    def __init__(self, name, tileMap, encounterEnemies):
        self.name = name
        self.tileMap = tileMap
        self.colliders = []
        self.boundaries = []
        self.npcs = []
        self.passages = []
        self.encounterEnemies = encounterEnemies

    def addCollider(self, collider):
        self.colliders.append(collider)

    def addNPC(self, NPC):
        self.npcs.append(NPC)

    def setBackground(self, background):
        self.background = background

    def getBackground(self):
        return self.background

    def getTileMap(self):
        return self.tileMap
