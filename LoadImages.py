#LoadImages.py
#Description: Loads all images and makes them variables ready for use in other files. Used for efficiency.
#Name: Michael Bassani
#Created: Nov 20, 2017
#Last Modified: Feb 1, 2018

import pygame

#<editor-fold desc = "PLAYER IMAGE">
player_stand_forward = pygame.transform.scale(pygame.image.load("Battle Images/p_standforward.png"), (50, 50))
#</editor-fold>

#<editor-fold desc = "BACKGROUND IMAGES">
image = pygame.transform.scale( pygame.image.load("Tileset.png"), (800, 600))
wallImage = pygame.transform.scale(pygame.image.load("wallHouse.png"), (75, 75))
#</editor-fold>

#<editor-fold desc = "NPCs">

#<editor-fold desc = "NPC1">
npc1_front_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc1_front.png"), (50, 50))
npc1_right_sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load("NPC Sprites/npc1_side.png"), (50, 50)), True, False)
npc1_left_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc1_side.png"), (50, 50))
npc1_back_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc1_back.png"), (50, 50))
#</editor-fold>
#<editor-fold desc = "NPC2">
npc2_front_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc2_front.png"), (50, 50))
npc2_right_sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load("NPC Sprites/npc2_side.png"), (50, 50)), True, False)
npc2_left_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc2_side.png"), (50, 50))
npc2_back_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc2_back.png"), (50, 50))
#</editor-fold>
#<editor-fold desc = "NPC3">
npc3_front_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc3_front.png"), (50, 50))
npc3_right_sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load("NPC Sprites/npc3_side.png"), (50, 50)), True, False)
npc3_left_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc3_side.png"), (50, 50))
npc3_back_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc3_back.png"), (50, 50))
#</editor-fold>
#<editor-fold desc = "NPC4">
npc4_front_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc4_front.png"), (50, 50))
npc4_right_sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load("NPC Sprites/npc4_side.png"), (50, 50)), True, False)
npc4_left_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc4_side.png"), (50, 50))
npc4_back_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc4_back.png"), (50, 50))
#</editor-fold>
#<editor-fold desc = "NPC5">
npc5_front_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc5_front .png"), (50, 50))
npc5_right_sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load("NPC Sprites/npc5_side .png"), (50, 50)), True, False)
npc5_left_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc5_side .png"), (50, 50))
npc5_back_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/npc4_back.png"), (50, 50))
#</editor-fold>
#<editor-fold desc = "HAROLD">
harold_front_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/Harold_Front.png"), (50, 50))
harold_right_sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load("NPC Sprites/Harold_side.png"), (50, 50)), True, False)
harold_left_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/Harold_side.png"), (50, 50))
harold_back_sprite = pygame.transform.scale(pygame.image.load("NPC Sprites/Harold_ back.png"), (50, 50))
#</editor-fold>

#</editor-fold>

#<editor-fold desc = "Battle Sprites">
heart_sprite = pygame.image.load("Battle Images/heart.png")

neighbor2TAINTED_battle_sprite = pygame.transform.scale(npc5_front_sprite, (75, 70))
player_battle_sprite = pygame.transform.scale(pygame.image.load("Battle Images/p_standforward.png"), (75, 70))
player_battle_image = pygame.transform.scale(pygame.image.load("Battle Images/p_standforward.png"), (75,70))

#</editor-fold>

#<editor-fold desc = "ITEMS">
wood_sprite = pygame.transform.scale(pygame.image.load("Other Images/wood.png"), (50, 50))
rope_sprite = pygame.transform.scale(pygame.image.load("Other Images/rope.png"), (50, 50))
iron_sprite = pygame.image.load("Other Images/Iron.png")
#</editor-fold>

#<editor-fold desc = "ROCKS AND PILLARS">
boulders_sprite = pygame.transform.scale(pygame.image.load("Other Images/boulders.png"), (108, 100))
pebbles_sprite = pygame.transform.scale(pygame.image.load("Other Images/pebbles.png"), (42, 27))
rock_sprite = pygame.transform.scale(pygame.image.load("Overworld Images/rock.png"), (50, 50))
pillar_sprite = pygame.transform.scale(pygame.image.load("Other Images/pillar.png"), (50, 150))
hole_sprite = pygame.transform.scale(pygame.image.load("Other Images/hole.png"), (50, 50))
#</editor-fold>

#<editor-fold desc = "SHOP SPRITES">
shelf_sprite=pygame.transform.scale(pygame.image.load("Furniture/shitsholder.png"),(96,87))
register_sprite=pygame.transform.scale(pygame.image.load("Furniture/register.png"),(48,168))
shelf2_sprite=pygame.transform.scale(pygame.image.load("Furniture/shitsholder2.png"),(48,144))
shelf2flip_sprite=pygame.transform.flip(shelf2_sprite,True,False)

shopman_sprite=pygame.transform.scale(pygame.image.load("NPC Sprites/npc4_side.png"),(48,48))
shopkeeper_sprite=pygame.transform.flip(shopman_sprite,True,False)
#</editor-fold>

#<editor-fold desc = "DOORS">
door_closed_sprite = pygame.transform.scale(pygame.image.load("Other Images/level1door.png"), (100, 100))
door_open_sprite = pygame.transform.scale(pygame.image.load("Other Images/level1dooropen.png"), (100, 100))
door_sprite= pygame.transform.scale(pygame.image.load("Other Images/level1door.png"), (100, 100))
#</editor-fold>

#<editor-fold desc = "BATTLE SCENES">
overworld_battle_scene = pygame.transform.scale(pygame.image.load("Battle Scenes/OverworldBattleScene.png"), (750, 560))
#</editor-fold>

#<editor-fold desc = "OVERWORLD">
tree_sprite = pygame.transform.scale(pygame.image.load("Overworld Images/tree.png"), (80, 100))
shop_sprite = pygame.transform.scale(pygame.image.load("Overworld Images/shop.png"), (325, 180))
overworldHouse_sprite = pygame.transform.scale(pygame.image.load("Overworld Images/overworldHouse.png"), (200, 180))
playerHouse_sprite = pygame.transform.scale(pygame.image.load("Overworld Images/playerHouse.png"), (200, 180))
well = pygame.transform.scale(pygame.image.load("Overworld Images/well.png"), (110, 150))
#</editor-fold>

#<editor-fold desc = "FURNITURE">
fridge_sprite = pygame.transform.scale(pygame.image.load("Furniture/fridge.png"), (60, 100))
torch_sprite = pygame.image.load("Other Images/lantern.png")
bed_sprite = pygame.transform.scale(pygame.image.load("Furniture/bed.png"), (75, 110))
plant_sprite = pygame.transform.scale(pygame.image.load("Furniture/housePlant.png"), (40, 80))
sink_sprite = pygame.transform.scale(pygame.image.load("Furniture/sink.png"), (100, 70))
computer_sprite = pygame.transform.scale(pygame.image.load("Furniture/computer.png"), (95, 100))
tableCloth_sprite = pygame.transform.scale(pygame.image.load("Furniture/tableCloth.png"), (100, 100))
seat_sprite = pygame.transform.scale(pygame.image.load("Furniture/seat.png"), (36, 36))
tallBookShelf_sprite = pygame.transform.scale(pygame.image.load("Furniture/tallBookshelf.png"), (55, 100))
tv_sprite = pygame.transform.scale(pygame.image.load("Furniture/tv.png"), (50, 75))
greenSofa_sprite = pygame.transform.scale(pygame.image.load("Furniture/greenSofa.png"), (50, 100))
boxes_sprite = pygame.transform.scale(pygame.image.load("Furniture/boxes.png"), (40, 60))
#</editor-fold>

#<editor-fold desc = "BOSSES">
bertha_sprite = pygame.transform.scale(pygame.image.load("Battle Images/Bertha_Front_Stand.png"), (100, 100))
bertha_front_sprite = pygame.transform.scale(pygame.image.load("Battle Images/Bertha_Front_Stand.png"), (150, 140))
boss2_sprite = pygame.transform.scale(pygame.image.load("Battle Images/whiteboss.png"), (150, 82))
boss2_battle_sprite = pygame.transform.scale(pygame.image.load("Battle Images/whiteboss.png"), (140, 70))
boss3_sprite = pygame.transform.scale(pygame.image.load("Battle Images/blackboss.png"), (135, 75))
boss3_battle_sprite = pygame.transform.scale(pygame.image.load("Battle Images/blackboss.png"), (140, 70))
#</editor-fold>

#<editor-fold desc = "MISC Sprites">
blank = pygame.image.load("Other Images/blank.png")
bucket_sprite = pygame.transform.scale(pygame.image.load("Title Images/bucket.png"), (35, 35))
#</editor-fold>