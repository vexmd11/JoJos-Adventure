#SceneLoading.py
#Description: SceneLoading is used to draw and load each scene in the game and store them in to variables to be used for efficiency
#               in the main game loop. This includes everything from backgrounds, NPC's, collision, interactable objects, and
#               boundaries. It draws the entire scene and saves it as one big scene to eliminate lag from many objects being
#               created and drawn to the screen repeatedly.
#Name: Michael Bassani
#Created: Nov 20, 2017
#Last Modified: Feb 1, 2018

import pygame
from rooms import *
from Scene import *
from Portal import *
from NPC import *
from LoadImages import *
from Interactable import *


#<editor-fold desc = "LOADING TILEMAP">
# Converts large tilemap into smaller tiles, which are accessible in a 2D Array called tilemap

tilemap = []
wallmap = []
for tileX in range(0, 3):
    line = []
    wallmap.append(line)
    for tileY in range(0, 3):
        rect = (tileX*25, tileY*25, 25, 25)
        line.append(wallImage.subsurface(rect))
for tileX in range(0, 32):
    line = []
    tilemap.append(line)
    for tileY in range(0, 24):
        rect = (tileX*25, tileY*25, 25, 25)
        line.append(image.subsurface(rect))
#</editor-fold>

#<editor-fold desc = "MAPS AND BACKGROUNDS">
#Converts Character indexes with ints for tileset index
def charToInt(char):
    if char == "a":return 0
    elif char == "b": return 1
    elif char == "c": return 2
    elif char == "d": return 3
    elif char == "e": return 4
    elif char == "f": return 5
    elif char == "g": return 6
    elif char == "h": return 7
    elif char == "i": return 8
    elif char == "j": return 9
    elif char == "k": return 10
    elif char == "l": return 11
    elif char == "m": return 12
    elif char == "n": return 13
    elif char == "o": return 14
    elif char == "p": return 15
    elif char == "q": return 16
    elif char == "r": return 17
    elif char == "s": return 18
    elif char == "t": return 19
    elif char == "u": return 20
    elif char == "v": return 21
    elif char == "w": return 22
    elif char == "x": return 23
    elif char == "y": return 24
    elif char == "z": return 25
    elif char == "!": return 26
    elif char == "@": return 27
    elif char == "#": return 28
    elif char == "$": return 29
    elif char == "%": return 30
    elif char == "^": return 31

#Includes Boundaries and Empty Space
def loadScene(map,surface):
        x = 0
        y = 0
        for i in range(0, 29):
            for j in range (0,31):
                if not isinstance(map.tileMap[i][j], int):
                    surface.blit(tilemap[charToInt((map.tileMap[i][j])[0:1])][charToInt((map.tileMap[i][j])[1:2])], (x, y))
                elif map.tileMap[i][j] == 1:
                    map.boundaries.append(Collider(pygame.Rect(x, y, 25, 25), None))
                elif map.tileMap[i][j] >= 11:
                    surface.blit(wallmap[map.tileMap[i][j] // 10 - 1][map.tileMap[i][j] % 10 - 1], (x,y))
                    map.boundaries.append(Collider(pygame.Rect(x, y, 25, 25), None))
                x += 25
            x = 0
            y +=25

def addComponent(scene, newObject):
    if isinstance(newObject, Collider):
        for i in range(0, len(scene.colliders)):
            if newObject.getRect().y < scene.colliders[i].getRect().y:
                scene.colliders.insert(i, newObject)
        if len(scene.colliders) == 0:
            scene.colliders.append(newObject)
    elif isinstance(newObject, NPC):
        for i in range(0, len(scene.npcs)):
            if newObject.getRect().y < scene.npc[i].getRect().y:
                scene.npcs.insert(i, newObject)
        if len(scene.nps) == 0:
            scene.npcs.append(newObject)
#</editor-fold>


#<editor-fold desc = "HOUSE SCENE">
#Tile Map for House
house = Scene("House", house_ts, False)
#Create Background
#<editor-fold desc = "Colliders">

bed = Interactable("The bed is freshly made, the pillow is sunken.",(pygame.Rect(180, 140, 75, 110)), bed_sprite)
house.addCollider(Collider(pygame.Rect(265, 105, 55, 100), tallBookShelf_sprite))
house.addCollider(Collider(pygame.Rect(440, 115, 40, 100), fridge_sprite))
house.addCollider(bed)
house.addCollider(Collider(pygame.Rect(340, 145, 100, 70), sink_sprite))
house.addCollider(Collider(pygame.Rect(180, 220, 40, 60), boxes_sprite))
house.addCollider(Collider(pygame.Rect(515, 225, 95, 100), computer_sprite))
house.addCollider(Collider(pygame.Rect(355, 265, 36, 36), seat_sprite))
house.addCollider(Collider(pygame.Rect(350, 300, 100, 100), tableCloth_sprite))
house.addCollider(Collider(pygame.Rect(455, 333, 36, 36), seat_sprite))
house.addCollider(Collider(pygame.Rect(308, 345, 36, 36), seat_sprite))
house.addCollider(Collider(pygame.Rect(235, 435, 50, 75), tv_sprite))
house.addCollider(Collider(pygame.Rect(175, 495, 50, 100), greenSofa_sprite))
house.addCollider(Interactable("It hasn't been watered in weeks.",(pygame.Rect(550, 500, 40, 80)), plant_sprite))
house.addCollider(Interactable("The leaves are wilted.",(pygame.Rect(400, 500, 40, 80)), plant_sprite))
house.addCollider(Collider(pygame.Rect(290, 560, 36, 36), seat_sprite))
#</editor-fold>
houseBackground = pygame.Surface((750, 700))
loadScene(house, houseBackground); house.setBackground(houseBackground)
#</editor-fold>1

#<editor-fold desc = "NEIGHBOR HOUSE SCENE">
neighborHouse = Scene("House", house_ts, False)
loadScene(neighborHouse, houseBackground); neighborHouse.setBackground(houseBackground)

neighborHouse.addCollider(Collider(pygame.Rect(265, 105, 55, 100), tallBookShelf_sprite))
neighborHouse.addCollider(Collider(pygame.Rect(440, 115, 40, 100), fridge_sprite))
neighborHouse.addCollider(Collider((pygame.Rect(180, 140, 75, 110)), bed_sprite))
neighborHouse.addCollider(Collider(pygame.Rect(340, 145, 100, 70), sink_sprite))
neighborHouse.addCollider(Collider(pygame.Rect(180, 220, 40, 60), boxes_sprite))
neighborHouse.addCollider(Collider(pygame.Rect(515, 225, 95, 100), computer_sprite))
neighborHouse.addCollider(Collider(pygame.Rect(355, 265, 36, 36), seat_sprite))
neighborHouse.addCollider(Collider(pygame.Rect(350, 300, 100, 100), tableCloth_sprite))
neighborHouse.addCollider(Collider(pygame.Rect(455, 333, 36, 36), seat_sprite))
neighborHouse.addCollider(Collider(pygame.Rect(308, 345, 36, 36), seat_sprite))
neighborHouse.addCollider(Collider(pygame.Rect(235, 435, 50, 75), tv_sprite))
neighborHouse.addCollider(Collider(pygame.Rect(175, 495, 50, 100), greenSofa_sprite))
neighborHouse.addCollider(Collider((pygame.Rect(550, 500, 40, 80)), plant_sprite))
neighborHouse.addCollider(Collider((pygame.Rect(400, 500, 40, 80)), plant_sprite))
neighborHouse.addCollider(Collider(pygame.Rect(290, 560, 36, 36), seat_sprite))

#</editor-fold>
#<editor-fold desc = "OVERWORLD SCENE">
overworld = Scene("Overworld", overworld_ts, False)

#<editor-fold desc = "Colliders and Images">

overworld.addCollider(Collider((pygame.Rect(380, -20, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(280, -20, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(180, -20, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(80, -20, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(480, -20, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(580, -20, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(330, -10, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(530, -10, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(130, -10, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(680, -10, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(-20, -10, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(430, 10, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(230, 10, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(30, 10, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(630, 10, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(380, 40, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(280, 40, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(680, 50, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(-20, 50, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(330, 50, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(500, 50, 200, 180)), overworldHouse_sprite))
overworld.addCollider(Collider((pygame.Rect(50, 50, 200, 180)), playerHouse_sprite))
overworld.addCollider(Collider((pygame.Rect(430, 70, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(230, 70, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(380, 100, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(280, 100, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(-20, 110, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(680, 110, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(330, 110, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(430, 130, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(230, 130, 80, 100)), tree_sprite))
overworld.addCollider(Interactable("Rocks don't talk because we are rocks.",(pygame.Rect(0, 195, 50, 50)), rock_sprite))
overworld.addCollider(Interactable("...",(pygame.Rect(230, 220, 50, 50)), rock_sprite))
overworld.addCollider(Interactable("...",(pygame.Rect(430, 270, 50, 50)), rock_sprite))
overworld.addCollider(Interactable("...",(pygame.Rect(450, 230, 50, 50)), rock_sprite))
overworld.addCollider(Interactable("...",(pygame.Rect(260, 260, 50, 50)), rock_sprite))
overworld.addCollider(Collider((pygame.Rect(300, 390, 50, 50)), rock_sprite))
overworld.addCollider(Collider((pygame.Rect(150, 390, 50, 50)), rock_sprite))
overworld.addCollider(Collider((pygame.Rect(250, 400, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(190, 399, 80, 100)), tree_sprite))
overworld.addCollider(Collider((pygame.Rect(10, 400, 325, 180)), shop_sprite))
overworld.addCollider(Collider((pygame.Rect(10, 395, 325, 20)), blank))
overworld.addCollider(Collider(pygame.Rect(0, 0, 5, 800), blank))
overworld.addCollider(Collider(pygame.Rect(0, 700, 800, 5), blank))
overworld.addCollider(Collider(pygame.Rect(750, 0, 5, 800), blank))
#</editor-fold>
#Create Background
overworldBackground = pygame.Surface((750, 700))
loadScene(overworld, overworldBackground); overworld.setBackground(overworldBackground)
#</editor-fold>

#<editor-fold desc = "SHOP SCENE">
shopBackground = pygame.Surface((750, 700))
shop = Scene("House", shop_ts, False)
registerNotActive = Collider(pygame.Rect(220,150,48,168),register_sprite)
register = Interactable("You bought a rope from the shop!", (pygame.Rect(220,150,48,168)),register_sprite)
shop.addCollider(Collider(pygame.Rect(529,150,96,87),shelf_sprite))
shop.addCollider(Collider(pygame.Rect(442,150,96,87),shelf_sprite))
shop.addCollider(Collider(pygame.Rect(355,150,96,87),shelf_sprite))
shop.addCollider(Collider(pygame.Rect(355,200,48,144),shelf2_sprite))
shop.addCollider(Collider(pygame.Rect(355,250,48,144),shelf2_sprite))
shop.addCollider(Collider(pygame.Rect(355,300,48,144),shelf2_sprite))
shop.addCollider(Collider(pygame.Rect(355,350,48,144),shelf2_sprite))
shop.addCollider(Collider(pygame.Rect(470,200,48,144),shelf2_sprite))
shop.addCollider(Collider(pygame.Rect(470,250,48,144),shelf2_sprite))
shop.addCollider(Collider(pygame.Rect(470,300,48,144),shelf2_sprite))
shop.addCollider(Collider(pygame.Rect(470,350,48,144),shelf2_sprite))
shop.addCollider(Collider(pygame.Rect(580,200,48,144),shelf2_sprite))
shop.addCollider(Collider(pygame.Rect(580,250,48,144),shelf2_sprite))
shop.addCollider(Collider(pygame.Rect(580,300,48,144),shelf2_sprite))
shop.addCollider(Collider(pygame.Rect(580,350,48,144),shelf2_sprite))
shop.addCollider(registerNotActive)
shop.addCollider(Collider(pygame.Rect(220,250,48,144),shelf2flip_sprite))
shop.addCollider(Collider(pygame.Rect(220,300,48,144),shelf2flip_sprite))
shop.addCollider(Collider(pygame.Rect(220,350,48,144),shelf2flip_sprite))
shop.addCollider(Collider(pygame.Rect(220,400,48,144),shelf2flip_sprite))
shop.addCollider(Collider(pygame.Rect(220,450,48,144),shelf2flip_sprite))
shop.addCollider(Collider(pygame.Rect(185,210,48,48),shopkeeper_sprite))
shop.addCollider(Collider(pygame.Rect(220,140,48,168),blank))
loadScene(shop, shopBackground); shop.setBackground(shopBackground)

#</editor-fold>

#<editor-fold desc = "Level1 Scene1">
level1_1 = Scene("House", level1_1_ts, True)


level1_1.addCollider(Collider(pygame.Rect(450, 150, 108, 100), pygame.transform.flip(boulders_sprite, True, False)))
level1_1.addCollider(Collider(pygame.Rect(300,160, 42, 35), pebbles_sprite))
level1_1.addCollider(Collider(pygame.Rect(640, 165, 50, 150), pillar_sprite))
level1_1.addCollider(Collider(pygame.Rect(110, 165, 50, 150), pillar_sprite))
level1_1.addCollider((Collider(pygame.Rect(385, 190, 35, 35), bucket_sprite)))
level1_1.addCollider(Collider(pygame.Rect(625, 285, 50, 150), pillar_sprite))
level1_1.addCollider(Collider(pygame.Rect(125, 285, 50, 150), pillar_sprite))
level1_1.addCollider(Collider(pygame.Rect(170, 270, 50, 50), rock_sprite))
level1_1.addCollider(Collider(pygame.Rect(225,390, 42, 35), pebbles_sprite))
level1_1.addCollider(Collider(pygame.Rect(640, 405, 50, 150), pillar_sprite))
level1_1.addCollider(Collider(pygame.Rect(110, 405, 50, 150), pillar_sprite))
level1_1.addCollider(Collider(pygame.Rect(580, 450, 50, 50), rock_sprite))
level1_1.addCollider(Collider(pygame.Rect(130, 515, 108, 100), boulders_sprite))
level1_1.addCollider(Collider(pygame.Rect(520,580, 42, 35), pebbles_sprite))
level1_1Background = pygame.Surface((750, 700))
loadScene(level1_1, level1_1Background); level1_1.setBackground(level1_1Background)
#</editor-fold>
#<editor-fold desc = "Level1 Scene2">
level1_2 = Scene("1-2",level1_2_ts, True)
level1_2.addCollider(Collider(pygame.Rect(110, 15, 50, 150), pillar_sprite))
level1_2.addCollider(Collider(pygame.Rect(300,60, 42, 35), pebbles_sprite))
level1_2.addCollider(Collider(pygame.Rect(600, 120, 108, 100), boulders_sprite))
level1_2.addCollider(Collider(pygame.Rect(125, 135, 50, 150), pillar_sprite))
level1_2.addCollider(Collider(pygame.Rect(480, 135, 50, 150), pillar_sprite))
level1_2.addCollider(Collider(pygame.Rect(170, 270, 50, 50), rock_sprite))
level1_2.addCollider(Collider(pygame.Rect(110, 255, 50, 150), pillar_sprite))
level1_2.addCollider(Collider(pygame.Rect(150, 400, 108, 100), boulders_sprite))
level1_2.addCollider(Collider(pygame.Rect(400, 415, 50, 150), pillar_sprite))
level1_2.addCollider(Collider(pygame.Rect(580,520, 42, 35), pebbles_sprite))

level1_2Background = pygame.Surface((750, 700))
loadScene(level1_2, level1_2Background); level1_2.setBackground(level1_2Background)
#</editor-fold>
#<editor-fold desc = "Level1 Scene3">
level1_3 = Scene("1-3",level1_3_ts, True)
level1_3.addCollider(Collider(pygame.Rect(640, 15, 50, 150), pillar_sprite))
level1_3.addCollider(Collider(pygame.Rect(300,60, 42, 35), pebbles_sprite))
level1_3.addCollider(Collider(pygame.Rect(500, 120, 108, 100), boulders_sprite))
level1_3.addCollider(Collider(pygame.Rect(625, 135, 50, 150), pillar_sprite))
level1_3.addCollider(Collider(pygame.Rect(230, 135, 50, 150), pillar_sprite))
level1_3.addCollider(Collider(pygame.Rect(170, 270, 50, 50), rock_sprite))
level1_3.addCollider(Collider(pygame.Rect(640, 255, 50, 150), pillar_sprite))
level1_3.addCollider(Collider(pygame.Rect(150, 400, 108, 100), boulders_sprite))
level1_3.addCollider(Collider(pygame.Rect(580,520, 42, 35), pebbles_sprite))

level1_3Background = pygame.Surface((750, 700))
loadScene(level1_3, level1_3Background); level1_3.setBackground(level1_3Background)
#</editor-fold>
#<editor-fold desc = "Level1 Scene4">
level1_4 = Scene("1-4",level1_4_ts, True)

door = Interactable("This door requires a key", pygame.Rect(350, 5, 100, 100), door_closed_sprite)
level1_4.addCollider(door)

level1_4Background = pygame.Surface((750, 700))
loadScene(level1_4, level1_4Background); level1_4.setBackground(level1_4Background)
#</editor-fold>
#<editor-fold desc = "Level 1 Boss"
level1_boss = Scene("1_Boss",level1_boss_ts, False)
level1_boss.addCollider(Collider(pygame.Rect(315, 650, 25, 40), torch_sprite))
level1_boss.addCollider(Collider(pygame.Rect(315, 550, 25, 40), torch_sprite))
level1_boss.addCollider(Collider(pygame.Rect(315, 450, 25, 40), torch_sprite))
level1_boss.addCollider(Collider(pygame.Rect(420, 650, 25, 40), torch_sprite))
level1_boss.addCollider(Collider(pygame.Rect(420, 550, 25, 40), torch_sprite))
level1_boss.addCollider(Collider(pygame.Rect(420, 450, 25, 40), torch_sprite))
level1_boss.addCollider(Collider(pygame.Rect(285, 350, 25, 40), torch_sprite))
level1_boss.addCollider(Collider(pygame.Rect(450, 350, 25, 40), torch_sprite))
level1_boss.addCollider(Collider(pygame.Rect(5, 0, 5, 800), blank))
level1_boss.addCollider(Collider(pygame.Rect(0, 700, 800, 5), blank))
level1_boss.addCollider(Collider(pygame.Rect(750, 0, 5, 800), blank))
level1_boss.addCollider(Collider(pygame.Rect(0, 0, 800, 5), blank))

level1_boss_Background = pygame.Surface((750, 700))
loadScene(level1_boss, level1_boss_Background); level1_boss.setBackground(level1_boss_Background)
#</editor-fold>

#<editor-fold desc = "Level 2 Scene1"
level2_1 = Scene("2_1",level2_1_ts, False)

level2_1.addCollider((Collider(pygame.Rect(385, 250, 35, 35), bucket_sprite)))

level2_1.addCollider(Collider(pygame.Rect(200, 200, 50, 60), hole_sprite))
level2_1.addCollider(Collider(pygame.Rect(550, 200, 50, 60), hole_sprite))
level2_1.addCollider(Collider(pygame.Rect(200, 480, 50, 50), hole_sprite))
level2_1.addCollider(Collider(pygame.Rect(550, 480, 50, 50), hole_sprite))
level2_1.addCollider(Interactable("Room 1", pygame.Rect(370, 400, 50, 50), rock_sprite))

level2_1Background = pygame.Surface((750, 700))
loadScene(level2_1, level2_1Background); level2_1.setBackground(level2_1Background)
#</editor-fold>
#<editor-fold desc = "Level 2 Scene2"
level2_2 = Scene("2_2",level2_1_ts, False)
level2_2.addCollider(Collider(pygame.Rect(200, 200, 50, 50), hole_sprite))
level2_2.addCollider(Collider(pygame.Rect(550, 200, 50, 50), hole_sprite))
level2_2.addCollider(Interactable("Room 2", pygame.Rect(370, 400, 50, 50), rock_sprite))
level2_2.addCollider(Collider(pygame.Rect(200, 480, 50, 50), hole_sprite))
level2_2.addCollider(Collider(pygame.Rect(550, 480, 50, 50), hole_sprite))

level2_2Background = pygame.Surface((750, 700))
loadScene(level2_2, level2_2Background); level2_2.setBackground(level2_2Background)
#</editor-fold>
#<editor-fold desc = "Level 2 Scene3"
level2_3 = Scene("2_3",level2_1_ts, False)
level2_3.addCollider(Collider(pygame.Rect(200, 200, 50, 50), hole_sprite))
level2_3.addCollider(Collider(pygame.Rect(550, 200, 50, 50), hole_sprite))
level2_3.addCollider(Interactable("Room 3", pygame.Rect(370, 400, 50, 50), rock_sprite))
level2_3.addCollider(Collider(pygame.Rect(200, 480, 50, 50), hole_sprite))
level2_3.addCollider(Collider(pygame.Rect(550, 480, 50, 50), hole_sprite))
level2_3Background = pygame.Surface((750, 700))
loadScene(level2_3, level2_3Background); level2_3.setBackground(level2_3Background)
#</editor-fold>
#<editor-fold desc = "Level 2 Scene4"
level2_4 = Scene("2_4",level2_1_ts, False)
level2_4.addCollider(Collider(pygame.Rect(200, 200, 50, 50), hole_sprite))
level2_4.addCollider(Collider(pygame.Rect(550, 200, 50, 50), hole_sprite))
level2_4.addCollider(Interactable("Room 4", pygame.Rect(370, 400, 50, 50), rock_sprite))
level2_4.addCollider(Collider(pygame.Rect(200, 480, 50, 50), hole_sprite))
level2_4.addCollider(Collider(pygame.Rect(550, 480, 50, 50), hole_sprite))
level2_4Background = pygame.Surface((750, 700))
loadScene(level2_4, level2_4Background); level2_4.setBackground(level2_4Background)
#</editor-fold>
#<editor-fold desc = "Level 2 Scene5"
level2_5 = Scene("2_5",level2_1_ts, False)
level2_5.addCollider(Collider(pygame.Rect(200, 200, 50, 50), hole_sprite))
level2_5.addCollider(Collider(pygame.Rect(550, 200, 50, 50), hole_sprite))
level2_5.addCollider(Interactable("Room 5", pygame.Rect(370, 400, 50, 50), rock_sprite))
level2_5.addCollider(Collider(pygame.Rect(200, 480, 50, 50), hole_sprite))
level2_5.addCollider(Collider(pygame.Rect(550, 480, 50, 50), hole_sprite))
level2_5Background = pygame.Surface((750, 700))
loadScene(level2_5, level2_5Background); level2_5.setBackground(level2_5Background)
#</editor-fold>
#<editor-fold desc = "Level 2 Scene6"
level2_6 = Scene("2_6",level2_1_ts, False)
level2_6.addCollider(Collider(pygame.Rect(200, 200, 50, 50), hole_sprite))
level2_6.addCollider(Collider(pygame.Rect(550, 200, 50, 50), hole_sprite))
level2_6.addCollider(Interactable("Room 6", pygame.Rect(370, 400, 50, 50), rock_sprite))
level2_6.addCollider(Collider(pygame.Rect(200, 480, 50, 50), hole_sprite))
level2_6.addCollider(Collider(pygame.Rect(550, 480, 50, 50), hole_sprite))
level2_6Background = pygame.Surface((750, 700))
loadScene(level2_6, level2_6Background); level2_6.setBackground(level2_6Background)
#</editor-fold>
#<editor-fold desc = "Level 2 Scene7"
level2_7 = Scene("2_7",level2_1_ts, False)
level2_7.addCollider(Collider(pygame.Rect(200, 200, 50, 50), hole_sprite))
level2_7.addCollider(Collider(pygame.Rect(550, 200, 50, 50), hole_sprite))
level2_7.addCollider(Interactable("Room 7", pygame.Rect(370, 400, 50, 50), rock_sprite))
level2_7.addCollider(Collider(pygame.Rect(200, 480, 50, 50), hole_sprite))
level2_7.addCollider(Collider(pygame.Rect(550, 480, 50, 50), hole_sprite))
level2_7Background = pygame.Surface((750, 700))
loadScene(level2_7, level2_7Background); level2_7.setBackground(level2_7Background)
#</editor-fold>
#<editor-fold desc = "Level 2 Scene8"
level2_8 = Scene("2_8",level2_1_ts, False)
level2_8.addCollider(Collider(pygame.Rect(200, 200, 50, 50), hole_sprite))
level2_8.addCollider(Collider(pygame.Rect(550, 200, 50, 50), hole_sprite))
level2_8.addCollider(Interactable("Room 8", pygame.Rect(370, 400, 50, 50), rock_sprite))
level2_8.addCollider(Collider(pygame.Rect(200, 480, 50, 50), hole_sprite))
level2_8.addCollider(Collider(pygame.Rect(550, 480, 50, 50), hole_sprite))
level2_8Background = pygame.Surface((750, 700))
loadScene(level2_8, level2_8Background); level2_8.setBackground(level2_8Background)
#</editor-fold>
#<editor-fold desc = "Level 2 Boss"
level2_Boss = Scene("2_Boss",level2_1_ts, False)
level2_Boss.addCollider(Collider(pygame.Rect(550, 480, 50, 50), hole_sprite))
level2_BossBackground = pygame.Surface((750, 700))
loadScene(level2_Boss, level2_BossBackground); level2_Boss.setBackground(level2_BossBackground)
#</editor-fold>
#<editor-fold desc = "Level 2 Portals">
level2_1.addCollider(Portal(pygame.Rect(200, 200, 50, 50), level2_5, 250, 480))
level2_1.addCollider(Portal(pygame.Rect(550, 200, 50, 50), level2_4, 500, 480))
level2_1.addCollider(Portal(pygame.Rect(550, 480, 50, 50), level2_6, 250, 480))
level2_1.addCollider(Portal(pygame.Rect(200, 480, 50, 50), level2_3, 500, 200))

level2_2.addCollider(Portal(pygame.Rect(200, 200, 50, 50), level2_3, 500, 480))
level2_2.addCollider(Portal(pygame.Rect(550, 200, 50, 50), level2_6, 250, 200))
level2_2.addCollider(Portal(pygame.Rect(550, 480, 50, 50), level2_8, 250, 200))
level2_2.addCollider(Portal(pygame.Rect(200, 480, 50, 50), level2_5, 500, 200))

level2_3.addCollider(Portal(pygame.Rect(200, 200, 50, 50), level2_7, 500, 200))
level2_3.addCollider(Portal(pygame.Rect(550, 200, 50, 50), level2_1, 250, 480))
level2_3.addCollider(Portal(pygame.Rect(550, 480, 50, 50), level2_2, 250, 200))
level2_3.addCollider(Portal(pygame.Rect(200, 480, 50, 50), level2_5, 250, 200))

level2_4.addCollider(Portal(pygame.Rect(200, 200, 50, 50), level2_8, 500, 480))
level2_4.addCollider(Portal(pygame.Rect(550, 200, 50, 50), level2_6, 250, 200))
level2_4.addCollider(Portal(pygame.Rect(550, 480, 50, 50), level2_1, 500, 200))
level2_4.addCollider(Portal(pygame.Rect(200, 480, 50, 50), level2_7, 250, 200))

level2_5.addCollider(Portal(pygame.Rect(200, 200, 50, 50), level2_3, 250, 480))
level2_5.addCollider(Portal(pygame.Rect(550, 200, 50, 50), level2_2, 250, 480))
level2_5.addCollider(Portal(pygame.Rect(550, 480, 50, 50), level2_4, 500, 200))
level2_5.addCollider(Portal(pygame.Rect(200, 480, 50, 50), level2_1, 250, 200))

level2_6.addCollider(Portal(pygame.Rect(200, 200, 50, 50), level2_2, 500, 200))
level2_6.addCollider(Portal(pygame.Rect(550, 200, 50, 50), level2_8, 500, 200))
level2_6.addCollider(Portal(pygame.Rect(550, 480, 50, 50), level2_4, 500, 200))
level2_6.addCollider(Portal(pygame.Rect(200, 480, 50, 50), level2_1, 500, 480))

level2_7.addCollider(Portal(pygame.Rect(200, 200, 50, 50), level2_4, 250, 480))
level2_7.addCollider(Portal(pygame.Rect(550, 200, 50, 50), level2_3, 250, 200))
level2_7.addCollider(Portal(pygame.Rect(550, 480, 50, 50), level2_Boss, 450, 480))
level2_7.addCollider(Portal(pygame.Rect(200, 480, 50, 50), level2_8, 250, 200))

level2_8.addCollider(Portal(pygame.Rect(200, 200, 50, 50), level2_7, 250, 480))
level2_8.addCollider(Portal(pygame.Rect(550, 200, 50, 50), level2_6, 500, 200))
level2_8.addCollider(Portal(pygame.Rect(550, 480, 50, 50), level2_4, 250, 200))
level2_8.addCollider(Portal(pygame.Rect(200, 480, 50, 50), level2_2, 500, 480))

level2_Boss.addCollider((Portal(pygame.Rect(550, 480, 50, 50), level2_7, 500, 480)))
#</editor-fold>

#<editor-fold desc = "Level 3 Scene1"
level3_1 = Scene("3_1",level3_1_ts, False)
level3_1.addNPC(NPC(pygame.Rect(100, 300, 50, 50), 5, "", "ENEMY"))
level3_1.addNPC(NPC(pygame.Rect(200, 475, 50, 50), 5, "", "ENEMY"))
level3_1.addNPC(NPC(pygame.Rect(675, 250, 50, 50), 5, "", "ENEMY"))
level3_1.addNPC(NPC(pygame.Rect(625, 575, 50, 50), 5, "", "ENEMY"))
level3_1.addCollider(Collider(pygame.Rect(360, 20, 35, 35), bucket_sprite))
level3_1.addCollider(Portal(pygame.Rect(360, 20, 35, 35), 0, 0, 0))

for i in range(0, 30):
        for j in range(0, 32):
            if "*" in str(level3_1_ts[i][j]):
                level3_1.addCollider(Collider(pygame.Rect(25*j, 25*i, 25, 25), blank))

level3_1Background = pygame.Surface((750, 700))
loadScene(level3_1, level3_1Background); level3_1.setBackground(level3_1Background)
#</editor-fold>

#<editor-fold desc = "End Scene"
endScene = Scene("End", end_ts, False)

endScene_Background = pygame.Surface((750, 700))
loadScene(endScene, endScene_Background); endScene.setBackground(endScene_Background)
#</editor-fold>