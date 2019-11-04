#CPT.py
#Description: This file is the main game file. It controls the story, progress in game, player collision, interaction, battling,
#               and everything else. It IS the game.
#Name: Michael Bassani
#Created: Nov 20, 2017
#Last Modified: Feb 1, 2018

from Player import *
from Enemy import *
from Player import *
from SceneLoading import *
from WellTitleScreen import *
from LoadImages import *
from LoadMusic import *
import random
from Battle import *
import time, random
from PlayerBattle import*

#Initialize pygame
pygame.mixer.init()
pygame.init()

#Objects/Variables
player_battle = PlayerBattle(0, 70*5, player_battle_image)
bertha = Interactable("Hm?",pygame.Rect(325, 300, 100, 115), bertha_sprite)
boss2 = Interactable("Hm?",pygame.Rect(325, 300, 150, 82), boss2_sprite)
boss3_onscreen = Collider(pygame.Rect(315, 315, 0, 0), boss3_sprite)
boss3_interactable = Interactable("Hm?",pygame.Rect(335, 315, 80, 70), blank)
bossPortal = Portal(door.rect, level1_boss, 350, 600)
currentMusic = level1_music

#Checks passages to other scenes in the current scene
def checkPassages():
    global currentScene
    for passage in currentScene.passages:
        #checks player position in relation to each passage, and changes the scene if the player enters the boundary
        if passage[0] == "x":
            if passage[2] == "less":
                if player.getHitbox().x < passage[1]:
                    currentScene = passage[3]
                    player.teleport(passage[4], player.getHitbox().y)
                    transition(0.3)
            elif passage[2] == "greater":
                if player.getHitbox().x > passage[1]:
                    currentScene = passage[3]
                    player.teleport(passage[4], player.getHitbox().y)
                    transition(0.3)
        else:
            if passage[2] == "less":
                if player.getHitbox().y < passage[1]:
                    currentScene = passage[3]
                    player.teleport(player.getHitbox().x, passage[4])
                    transition(0.3)
            if passage[2] == "greater":
                if player.getHitbox().y > passage[1]:
                    currentScene = passage[3]
                    player.teleport(player.getHitbox().x, passage[4])
                    transition(0.3)

#checks player interaction in the current scene
def checkInteraction():
    global triggerInteraction
    global currentScene
    if player.interact(currentScene) != "" or player.interactNPC(currentScene) != "":
        interactOutput = player.interact(currentScene) #gets the current interaction in the scene
        if triggerInteraction and (player.xVel == 0 and player.yVel == 0):
            if isinstance(interactOutput, Interactable) and interactOutput != "": #if the interaction is with an Interactable object
                textQue.append(interactOutput.getText()) #gets the Interactable objects text and displays it in textbox
                interactOutput.interacted = True
            elif isinstance(interactOutput, Portal): #if the interaction is with a Portal object
                #Handles where the player with teleport to
                if interactOutput.getNewScene() == 0:
                    loadLevel = wellTitle.mainLoop(lockLevel)
                    if loadLevel == "level 1":
                        player.teleport(370,220)
                        currentScene = level1_1
                    if loadLevel == "level 2":
                        player.teleport(370, 280)
                        currentScene = level2_1
                    if loadLevel == "level 3":
                        player.teleport(300, 25)
                        currentScene = level3_1
                    elif loadLevel == "surface":
                        player.teleport(340, 300)
                        currentScene = overworld
                    transition(0.3)
                else:
                    player.teleport(interactOutput.newPlayerX, interactOutput.newPlayerY)
                    currentScene = interactOutput.getNewScene()
                    transition(0.3)
            elif player.interact(currentScene) == "": #if interaction is with an NPC object
                #turns NPC towards the player according to player sprite
                if player.getSprite() == player.standright:
                    currentScene.npcs[player.interactNPC(currentScene)].turn(3)
                elif player.getSprite() == player.standleft:
                    currentScene.npcs[player.interactNPC(currentScene)].turn(4)
                elif player.getSprite() == player.standforward:
                    currentScene.npcs[player.interactNPC(currentScene)].turn(2)
                elif player.getSprite() == player.standback:
                        currentScene.npcs[player.interactNPC(currentScene)].turn(1)
                for text in currentScene.npcs[player.interactNPC(currentScene)].getText():
                    textQue.append(text)
                currentScene.npcs[player.interactNPC(currentScene)].spoken = True
        triggerInteraction = False
    else:
        wellTitle.reset()

#Raining function used at one point in the story
#<editor-fold desc = "RAIN">
raining = False
rain = []
def getRain():
   if len(rain) != 200:
       randX = random.randint(0, 750)
       rain.append(pygame.Rect(randX, 0, 3, 6))

def thunderstorm():
   getRain()
   for drop in rain:
       drop.y += 14
       pygame.draw.rect(screen, (0, 0, 255), drop)
       if drop.y >= 800:
           rain.remove(drop)
   flash = random.randint(1, 200)
   if flash == 66:
       screen.fill((255, 255, 255))
       pygame.display.update()
       time.sleep(0.1)
#</editor-fold>

#<editor-fold desc = "FONTS AND TEXT">
#Variables
textFont = pygame.font.SysFont('Times New Roman', 30)
pressEFont = pygame.font.SysFont('Times New Roman', 16)
pressE = pressEFont.render("Continue : Z", False, (255,255,255))
gameoverFont = pygame.font.Font("Fonts/ARCADECLASSIC.TTF", 150)
respawnFont = pygame.font.Font("Fonts/ARCADECLASSIC.TTF", 50)
gameover = gameoverFont.render("GAME  OVER",False, (255, 255, 255))
respawn = respawnFont.render("Respawning at house", False, (255, 255, 255))
thankYouText = respawnFont.render("Thank you for playing!", False, (0, 0, 0))
moreLevelsText = respawnFont.render("More  levels  coming 2018!", False, (0, 0, 0))

#displays text in textbox
def displayText():
    global textQue
    if len(textQue) > 0: #textQue is used to hold text to be displayed
           pygame.draw.rect(screen, (50, 50, 50), (25, 25, 700, 125))
           pygame.draw.rect(screen, (255, 255, 255), (25,  25, 700, 125), 2)
           if isinstance(textQue[0], str):
               dialogue = textFont.render(textQue[0], False, (255, 255, 255))
               screen.blit(dialogue, (40, 50))
               screen.blit(pressE, (630, 120))
           else:
               dialogue = textFont.render(textQue[0][0], False, (255, 255, 255))
               screen.blit(dialogue, (40, 50))
               screen.blit(pressE, (630, 120))
               dialogue = textFont.render(textQue[0][1], False, (255, 255, 255))
               screen.blit(dialogue, (40, 80))
               screen.blit(pressE, (630, 120))
#</editor-fold>

#<editor-fold desc = "SCREEN AND WINDOWS">
screen = pygame.display.set_mode((800, 750)) #game screen
clock = pygame.time.Clock() #clock to keep track of game loop
wellTitle = WellTitleScreen()

#Black screen transition between rooms/scenes
def transition(wait):
    screen.fill(( 0,  0,  0))
    pygame.display.update()
    time.sleep(wait)
#</editor-fold>

#Extra Portals added in the main town/overworld to transition between houses/shops and town scene
#<editor-fold desc = "PORTALS">
house.addCollider    (Portal(pygame.Rect(450 ,590, 100, 50), overworld , 150, 240))
overworld.addCollider(Portal(pygame.Rect(150, 185,  50, 45), house     , 480, 515))

neighborHouse.addCollider    (Portal(pygame.Rect(450 ,590, 100, 50), overworld , 600, 220))
overworld.addCollider        (Portal(pygame.Rect(600, 185,  50, 45), neighborHouse , 480, 515))

shop.addCollider     (Portal(pygame.Rect(450 ,590, 100, 50), overworld , 105, 583))
overworld.addCollider(Portal(pygame.Rect(105, 528,  50, 45), shop     , 480, 515))

#passages for level 1
level1_2.passages.append(["y", 0, "less", level1_1, 650])
level1_2.passages.append(["x", 720, "greater", level1_3, 5])
level1_1.passages.append(["y", 650, "greater", level1_2, 5])
level1_3.passages.append(["x", 0, "less", level1_2, 700])
level1_3.passages.append(["y", 0, "less", level1_4, 650])
level1_4.passages.append(["y", 650, "greater", level1_3, 5])

level1_1.addCollider(Portal(pygame.Rect(385, 190, 35, 35), 0, 0, 0))
level2_1.addCollider(Portal(pygame.Rect(385, 250, 35, 35), 0, 0, 0))

#TEMPORARY HOUSE MATS PORTALS
pygame.draw.rect(house.getBackground(), (225,0,0), pygame.Rect(450,590, 100, 50))
pygame.draw.rect(house.getBackground(), (150,0,0), pygame.Rect(460,600, 80, 30))
pygame.draw.rect(shop.getBackground(), (225,0,0), pygame.Rect(450,590, 100, 50))
pygame.draw.rect(shop.getBackground(), (150,0,0), pygame.Rect(460,600, 80, 30))
#</editor-fold>

#<editor-fold desc = "INITIAL GAME STATES">
player = Player(275, 200)#initial player coordinates
currentScene = house
lockLevel = 2
triggerInteraction = False
counter = 0
textQue = []

progress = 0
doStory = True
#</editor-fold>

#<editor-fold desc = "CHARACTERS">
mom = NPC(pygame.Rect(200, 250, 50,  50), 3, "", "NEIGHBOR")
neighbor1 = NPC(pygame.Rect(245, 315, 50,  60), 2, "", "MOM")
dad = NPC(pygame.Rect(320, 280, 50, 60), 1, "", "DAD")
neighbor2 = NPC(pygame.Rect(425, 200, 50, 60), 4, "", "NEIGHBOR")
neighbor2TAINTED = NPC(pygame.Rect(425, 200, 50, 60), 5, "", "NEIGHBOR")
Harold = NPC(pygame.Rect(200, 500, 50, 60), 6, "", "HAROLD")
ironEnemy = Interactable("...", pygame.Rect(425, 200, 50, 80), neighbor2TAINTED.sprite)

def displayNPC(scene): #displays NPC in their current scene
    for NPC in scene.npcs:
        screen.blit(NPC.sprite, NPC.getRect())
#</editor-fold>

#<editor-fold desc = "Gameover">
def gameoverScreen():
    global currentScene
    currentScene = house
    player.hitbox.x = 275
    player.hitbox.y = 200
    screen.fill((0, 0, 0))
    screen.blit(gameover, (25, 150))
    screen.blit(respawn, (125, 300))
    player_battle.health = 100
    player_battle.xPos = 150
    player_battle.yPos = 350
    pygame.display.update()
    time.sleep(5)
#</editor-fold>

#Items
wood = Interactable("You Found the Wood!", pygame.Rect(200, 200, 50, 50), wood_sprite)
rope = Interactable("You Found the Rope!", pygame.Rect(250, 200, 50, 50), rope_sprite)
steel = Interactable("You collected the steel!", pygame.Rect(425, 200, 50, 70), iron_sprite)

#~~~~~~~~~~~~~~~~~~~~~~~STORY HANDLING~~~~~~~~~~~~~~~~~~~~~~~#
def eventManager ():
    global currentScene
    global progress
    if progress == 0:
        textQue.append("You wake up on a sunday morning feeling tired...")
        textQue.append("There's a note on the pillow!")
        textQue.append(["\"I took a walk to the neighbors... Meet me", "over there when you wake up..."])
        textQue.append("Love Mom xoxo\"")
        progress += 1
    elif progress == 1:
        if player.hitbox.y >= 500:
            progress += 1
    elif progress == 2:
        textQue.append(["Before you walk outside, you glance", "at your hand... The note is no longer there."])
        progress += 1
    elif progress == 3:
        if currentScene == overworld:
            progress += 1
            neighborHouse.npcs.insert(0, neighbor1)
            neighborHouse.addNPC(neighbor2)
            neighbor1.sprite = neighbor1.spriteRight
            neighbor1.setText(["Oh... you're looking for your mom?", "We haven't seen her in a while either..."])
            neighbor2.setText(["You can always stop by if you ever feel lonely."])
    elif progress == 4:
        if neighbor1.spoken and player.hitbox.y > 500:
            textQue.append("I'm sorry JoJo.")
            neighbor1.sprite = neighbor1.spriteFront
            progress += 1
    elif progress == 5:
        if currentScene == overworld:
            overworld.addNPC(mom)
            progress += 1
    elif progress == 6:
        if currentScene == overworld and player.hitbox.x < 320 and player.hitbox.y < 380:
            textQue.append("Mom?")
            progress += 1
            player.speed = 0
    elif progress == 7:
        if len(textQue) == 0:
            if mom.getRect().x > 150:
                mom.sprite = mom.spriteLeft
                mom.getRect().x -= 1
            elif mom.getRect().y > 190:
                mom.sprite = mom.spriteBack
                mom.getRect().y -= 1
            else:
                currentScene.npcs.remove(mom)
                player.speed = 3
                progress +=1
                textQue.append("...")
    elif progress == 8:
        if currentScene == house:
            textQue.append(["Where did she go?", "Is this a dream...?"])
            progress += 1
            bed.interacted = False
    elif progress == 9:
        global raining
        if player.hitbox.y > 530 and (player.hitbox.x > 400 and player.hitbox.x < 540):
            player.hitbox.y = 530
            textQue.append(["This is probably all a dream...", "I should head to bed again..."])
        if bed.interacted:
            raining = True
            progress += 1
            currentScene = endScene
            player.hitbox.x += 1000
            textQue.append("You wake up to the sound of a thunderstorm outside.")
            overworld.npcs.append(dad)
            dad.sprite = dad.spriteRight
            dad.spoken = False
            bed.interacted = False
    elif progress == 10:
        if len(textQue) == 0 and currentScene == endScene:
            currentScene = house
            player.hitbox.x -= 1000
        if counter % 140 == 0:
            if dad.sprite == dad.spriteRight:
                dad.sprite = dad.spriteBack
            elif dad.sprite == dad.spriteBack:
                dad.sprite = dad.spriteRight
        if dad.spoken:
            textQue.append("Son! Why did you sneak up on me?!")
            textQue.append("I'm working on something... It's a surprise.")
            textQue.append(["It's dangerous to be working out in", "a storm like this, but..."])
            textQue.append("Your mother wanted this done.")
            textQue.append("...")
            textQue.append("Could you give me a hand, son?")
            textQue.append(["I need you to go to the shop and", "buy me some rope."])
            textQue.append("I'll need it to tie some things together.")
            textQue.append(["The shop is in the south of town,", "here's some money."])
            textQue.append("Be careful and come back quickly!")
            shop.colliders.remove(shop.colliders[15])
            shop.colliders.insert(15, register)
            progress += 1
    elif progress == 11:
        dad.setText(["Go to the shop and buy me some rope!"])
        if register.interacted:
            progress += 1
            overworld.npcs.remove(dad)
    elif progress == 12:
        if currentScene == overworld:
            if player.hitbox.y < 400:
                textQue.append("Where did he go?")
                textQue.append(["The storm seems to have gotten stronger,", "he must have went inside."])
                textQue.append("Better go after him!")
                progress += 1
                neighborHouse.npcs.remove(neighbor2)
    elif progress == 13:
        if currentScene == neighborHouse:
            neighbor1.setText(["What are you doing here in this storm!", "You should get home quickly!"])
        elif currentScene == house:
            textQue.append("What?")
            textQue.append("He's gone too?")
            textQue.append(["After you step through the door,", "the rain seems to have stopped instantaneously."])
            raining = False
            overworld.colliders.insert(31, Collider((pygame.Rect(310, 170, 110, 150)), well))
            progress += 1
            neighbor2TAINTED.rect = pygame.Rect(350, 300 , 50, 50)
            overworld.addNPC(neighbor2TAINTED)
    elif progress == 14:
        if neighbor2TAINTED.spoken:
            textQue.append("...")
            progress+=1
            neighbor1.rect = pygame.Rect(600, 220, 50, 50)
            neighbor1.sprite = neighbor1.spriteFront
    elif progress == 15:
        if len(textQue) == 0:
            player.speed = 0
            overworld.addNPC(neighbor1)
            if neighbor1.rect.y < 350:
                neighbor1.rect.y += 4
            elif neighbor1.rect.x > 400:
                neighbor1.sprite = neighbor1.spriteLeft
                neighbor1.rect.x -= 4
            else:
                progress += 1
                textQue.append("WAIT!")
                textQue.append("He is dangerous right now.")
                textQue.append(["When I finish talking to you, you will", "enter a battle with him."])
                textQue.append(["Don't worry, he's just the tutorial", "enemy, he should be easy."])
                textQue.append("Just take caution, and plan your moves!")
    elif progress == 16:
        global currentMusic
        if len(textQue) == 0:
            if neighbor2TAINTED.spoken:
                newBattle = Battle([Enemy(pygame.Rect(300, 280, 75, 70), neighbor2TAINTED_battle_sprite, 50, 5, 8)], overworld_battle_scene, player_battle)
                changeMusic(battle_music)
                transition(0.5)
                if newBattle.startBattle() == False:
                    gameoverScreen()
                    neighbor2TAINTED.spoken = False
                    player.speed = 3
                else:
                    neighbor2TAINTED.spoken = False
                    progress += 1
                    player.speed = 3
                    overworld.npcs.remove(neighbor2TAINTED)
                    textQue.append("Great job!")
                    textQue.append("Don't worry about him, he'll be fine.")
                    textQue.append("It'll just take some time to wear off.")
                    textQue.append("But you need to find your parents!")
                    textQue.append(["Head down into the well, you will", "need to defeat Three Gods of the Underworld."])
                    textQue.append("It is kill or be killed down there.")
                    textQue.append(["Even the floor beneath your feet is", "something to worry about."])
                    textQue.append(["But REMEMBER: You can always come back", "to your house and rest in bed."])
                    textQue.append("Good luck, young adventurer.")
    elif progress == 17:
        if len(textQue) == 0:
            if neighbor1.rect.y > -50:
                neighbor1.rect.y -= 4
                if counter % 5 == 0:
                    if neighbor1.sprite == neighbor1.spriteFront:
                        neighbor1.sprite = neighbor1.spriteLeft
                    elif neighbor1.sprite == neighbor1.spriteLeft:
                        neighbor1.sprite = neighbor1.spriteBack
                    elif neighbor1.sprite == neighbor1.spriteBack:
                        neighbor1.sprite = neighbor1.spriteRight
                    elif neighbor1.sprite == neighbor1.spriteRight:
                        neighbor1.sprite = neighbor1.spriteFront
            else:
                progress += 1
                textQue.append("You take a deep breath. Time to go.")
                overworld.addCollider(Portal(pygame.Rect(310, 170, 110, 150), 0, 0, 0))
                level1_1.addNPC(Harold)
                Harold.spoken = False
    elif progress == 18:
        if Harold.spoken:
            textQue.append("WELCOME VISITOR!")
            textQue.append(["WELCOME TO THE HOLLY JOLLY HAPPY", "UNDERLAND!"])
            textQue.append("MY NAME'S HAROLD! OH MAN IM SO EXCITED!")
            textQue.append(["I NEVER GET VISITORS AND NOW I HAVE A", "COOL FRIEND!"])
            textQue.append("I've been trapped down here for years.")
            textQue.append(["Maybe with your help we could both get out of here.", "Matter of fact..."])
            textQue.append(["If you can manage to defeat Bertha I reckon we", "can go deeper."])
            textQue.append("You need a weapon though...")
            textQue.append(["Bring me back some wood, steel and rope, and I'll craft", "A sword for you!"])
            progress+= 1
            Harold.setText(["You haven't collected all the materials yet!"])
            level1_3.colliders.insert(0, ironEnemy)
            level1_2.colliders.insert(0, wood)
            register.interacted = False
            player.inventory = []
    elif progress == 19:
        if "rope" in player.inventory and "steel" in player.inventory and "wood" in player.inventory:
            progress +=1
            textQue.append(["You have collected all of the items!", "Bring them to Harold!"])
            Harold.setText(["Whoa you did it!"])
            Harold.spoken = False
        if register.interacted and "rope" not in player.inventory:
            player.inventory.append("rope")
            register.interacted = False
        if ironEnemy.interacted and len(textQue) == 0:
            steelBattle = Battle([Enemy(pygame.Rect(300, 280, 75, 70), neighbor2TAINTED_battle_sprite, 100, 5, 8)], overworld_battle_scene, player_battle)
            changeMusic(battle_music)
            if steelBattle.startBattle() == False:
                gameoverScreen()
                ironEnemy.interacted = False
            else:
                ironEnemy.interacted = False
                level1_3.colliders.remove(ironEnemy)
                level1_3.addCollider(steel)
        if wood.interacted:
            level1_2.colliders.remove(wood)
            player.inventory.append("wood")
            wood.interacted = False
        if steel.interacted:
            player.inventory.append("steel")
            level1_3.colliders.remove(steel)
            steel.interacted = False
    elif progress == 20:
        if Harold.spoken:
            textQue.append("Amazing!")
            textQue.append("*Clong* *Clang*")
            textQue.append("Ta Da! A sword for you! Fit to defeat Bertha!")
            textQue.append("Okay, young one, follow me...")
            progress += 1
            player.setSpeed(0)
            Harold.sprite = Harold.spriteRight
            player_battle.closeAttackPower += 2
            player_battle.rangedAttackPower += 1
    elif progress == 21:
        if len(textQue) == 0:
            if Harold.rect.x < 300:
                Harold.rect.x += 5
            elif Harold.rect.y < 800:
                Harold.sprite = Harold.spriteFront
                Harold.rect.y += 5
            else:
                level1_1.npcs.remove(Harold)
                level1_2.addNPC(Harold)
                Harold.rect = pygame.Rect(400, 300, 50, 50)
                player.setSpeed(3)
                Harold.sprite = Harold.spriteRight
                progress += 1
    elif progress == 22:
        if currentScene == level1_2:
            player.setSpeed(0)
            if Harold.rect.x < 800:
                Harold.rect.x += 5
            else:
                level1_2.npcs.remove(Harold)
                level1_3.addNPC(Harold)
                Harold.rect = pygame.Rect(400, 300, 50, 50)
                player.setSpeed(3)
                Harold.sprite = Harold.spriteBack
                progress += 1
    elif progress == 23:
        if currentScene == level1_3:
            player.setSpeed(0)
            if Harold.rect.y > -50:
                Harold.rect.y -= 5
            else:
                level1_3.npcs.remove(Harold)
                level1_4.npcs.insert(0, Harold)
                Harold.rect = pygame.Rect(400, 150, 50, 50)
                player.setSpeed(3)
                Harold.sprite = Harold.spriteBack
                progress += 1
                Harold.spoken = False
                Harold.setText(["This is the door to Bertha's Lair."])
    elif progress == 24:
        global door
        if Harold.spoken:
            textQue.append("I'll unlock it for you... I have the key.")
            door.sprite = door_open_sprite
            level1_4.addCollider(bossPortal)
            level1_4.colliders.remove(door)
            textQue.append("I'll wait right here for you.")
            level1_4.addCollider(Collider(door.rect, door.sprite))
            Harold.spoken = False
            progress += 1
            Harold.setText(["Go on in bud, I'll wait here."])
    elif progress == 25:
        level1_boss.colliders.insert(0, bertha)
        progress += 1
    elif progress == 26:
        if bertha.interacted and len(textQue) == 0:
            textQue.append("Who are you?")
            textQue.append("How dare you approach me foolish mortal!")
            textQue.append("Do you know who I am?")
            textQue.append("Of course not...")
            textQue.append("I am Bertha! One of the Three Gods of the Underworld!")
            textQue.append(["For disturbing my thousand year slumber,", "prepare to meet your doom!"])
            progress+=1
    elif progress == 27:
        if len(textQue) == 0 and bertha.interacted:
            Bertha_battle = Battle([Enemy(pygame.Rect(450, 210, 150, 140), bertha_front_sprite, 125, 10, 13)], overworld_battle_scene, player_battle)
            changeMusic(boss_music)
            if Bertha_battle.startBattle() == False:
                gameoverScreen()
                bertha.interacted = False
                bertha.setText("Back for more?")
            else:
                progress+= 1
                bertha.interacted = False
    elif progress == 28:
        level1_boss.colliders.remove(bertha)
        textQue.append("NOOOOOOOO!")
        textQue.append(["Bertha's body sank further into the", "underworld."])
        textQue.append("Time to meet up with our buddy Harold!")
        Harold.setText(["Good job buddy! I knew you could do it!"])
        progress+= 1
    elif progress == 29:
        if len(textQue)==0:
            currentScene = level1_4
            player.hitbox.x = 325
            player.hitbox.y = 110
            Harold.spoken = False
            progress += 1
    elif progress == 30:
        if bossPortal in level1_4.colliders:
            level1_4.colliders.remove(bossPortal)
            level1_4.colliders.append(Interactable("No need to go back in here.", pygame.Rect(350, 5, 100, 101), door_closed_sprite))
        if Harold.spoken and currentScene == level1_4:
            textQue.append(["You know what happens next right?", "Time to go down a level!"])
            textQue.append(["But first you should rest up at home.", "Go take a nap and meet me down at level 2!"])
            Harold.spoken = False
            progress += 1
    elif progress == 31:
        if len(textQue) == 0:
            player.speed = 0
            Harold.sprite = harold_front_sprite
            Harold.rect.y += 3
            if Harold.rect.y >= 700:
                level1_4.npcs.remove(Harold)
                level2_1.addNPC(Harold)
                Harold.rect.x = 300
                Harold.rect.y = 300
                Harold.setText(["Get to the next boss bud!"])
                player.speed = 3
                progress+=1
    elif progress == 32:
        global lockLevel
        lockLevel = 3
        level2_Boss.colliders.insert(0, boss2)
        progress+=1
    elif progress == 33:
        if currentScene == level2_1:
            player_battle.rangedAttackPower+=1
            player_battle.closeAttackPower+=1
            Harold.sprite = harold_right_sprite
            textQue.append("HEY BUDDY! You made it safe and sound.")
            textQue.append("Next up, you have to find the second boss.")
            textQue.append(["But from the looks of it, she set up an elaborate puzzle", "to throw you off course."])
            textQue.append("You see those holes in the ground? Those are portals.")
            textQue.append("You just have to find the correct way to her lair.")
            textQue.append(["Here's a tip: Go up to those rocks to tell what", " room you're in, use them to your advantage!"])
            textQue.append("Good luck! I'll be rooting for you.")
            progress+=1
    elif progress == 34:
        if boss2.interacted:
            textQue.append("Who are you?")
            textQue.append("How did you get down here? You solved my puzzle?")
            textQue.append(["This can only mean one thing... You beat my sister,", "didn't you?"])
            textQue.append("I will not go down so easily, fiend.")
            textQue.append("Prepare for this fight to be your last!")
            progress += 1
    elif progress == 35:
        if len(textQue) == 0 and boss2.interacted:
            Boss2Fight = Battle([Enemy(pygame.Rect(450, 210, 150, 70), boss2_battle_sprite, 150, 12, 15)], overworld_battle_scene, player_battle)
            changeMusic(boss_music)
            if Boss2Fight.startBattle() == False:
                gameoverScreen()
                boss2.interacted = False
                boss2.setText("You again? Foolish.")
            else:
                boss2.interacted = False
                progress+=1
    elif progress == 36:
        textQue.append("Sister... I have failed you...")
        textQue.append("We can only rely on our older sister now...")
        textQue.append("Farewell...")
        player_battle.closeAttackPower+=1
        player_battle.rangedAttackPower+=1
        progress+=1
    elif progress == 37:
        if len(textQue) == 0:
            level2_Boss.colliders.remove(boss2)
            player.speed = 0
            Harold.rect.x = 500
            Harold.rect.y = 480
            Harold.sprite = harold_left_sprite
            level2_1.npcs.remove(Harold)
            level2_Boss.npcs.append(Harold)
            textQue.append("AMAZING BUDDY! You did it again!")
            textQue.append("There's only one more level to go!")
            textQue.append(["Make sure you rest up at home because this","next one's a toughie!"])
            textQue.append("Meet me down at level 3 soon!")
            progress += 1
    elif progress == 38:
        if len(textQue) == 0:
            Harold.sprite = harold_right_sprite
            level2_Boss.npcs.remove(Harold)
            Harold.rect.x = 350
            Harold.rect.y = 150
            level3_1.addNPC(Harold)
            lockLevel = 4
            level2_Boss.colliders = []
            level2_Boss.addCollider(Collider(pygame.Rect(200, 480, 50, 50), hole_sprite))
            level2_Boss.addCollider(Portal(pygame.Rect(200, 480, 50, 50), level2_1, 325, 480))
            player.speed = 3
            progress += 1
    elif progress == 39:
        level2_1.addCollider(Interactable("You probably don't want to do that.", pygame.Rect(200, 200, 80, 80), blank))
        level2_1.addCollider(Interactable("You probably don't want to do that.", pygame.Rect(540, 200, 80, 80), blank))
        level2_1.addCollider(Interactable("You probably don't want to do that.", pygame.Rect(540, 450, 80, 80), blank))
        level2_1.addCollider(Interactable("You probably don't want to do that.", pygame.Rect(200, 450, 80, 80), blank))
        level3_1.addCollider(boss3_onscreen)
        level3_1.addCollider(boss3_interactable)
        progress += 1
    elif progress == 40:
        if currentScene == level3_1:
            Harold.sprite = harold_back_sprite
            textQue.append("Hey BUD you finally arrived!")
            textQue.append("This is the homestretch! You're almost done.")
            textQue.append(["But this last level isn't a walk in the park", "like the last one."])
            textQue.append("This is an invisible maze! Cool right?")
            textQue.append(["You just have to find your way to the boss.", "I know you can do it!"])
            textQue.append(["Here's a tip: Try following the enemies!", "They might be blocking a path..."])
            textQue.append(["I'll be waiting for you back at the surface!", "Good luck!"])
            progress+=1
    elif progress == 41:
        if len(textQue)==0:
            player.speed = 0
            Harold.rect.y-=3
            if Harold.rect.y <= 50:
                level3_1.npcs.remove(Harold)
                progress+=1
                player.speed = 3
    elif progress == 42:
        if currentScene == level3_1:
            for npc in currentScene.npcs:
                if npc.spoken:
                    if npc != boss3_interactable:
                        enemyBattle = Battle([Enemy(pygame.Rect(450, 420, 75, 70), neighbor2TAINTED_battle_sprite, 50, 6, 8)], overworld_battle_scene, player_battle)
                        changeMusic(battle_music)
                        if enemyBattle.startBattle() == False:
                            gameoverScreen()
                            npc.spoken = False
                        else:
                            npc.spoken = False
                            currentScene.npcs.remove(npc)
        if boss3_interactable.interacted:
            progress+=1
    elif progress == 43:
        textQue.append("So you're the young lad I've heard about.")
        textQue.append("My sisters have warned me from beyond.")
        textQue.append(["If you could take both of them down,","don't think I'll be as easy."])
        textQue.append(["If you beat me, I do not deserve to,", "be a God of the Underworld!"])
        progress+=1
    elif progress==44:
        if len(textQue)==0:
            Boss3Fight = Battle([Enemy(pygame.Rect(450, 210, 150, 70), boss3_battle_sprite, 175, 13, 17)], overworld_battle_scene, player_battle)
            changeMusic(boss_music)
            if boss3_interactable.interacted:
                if Boss3Fight.startBattle() == False:
                    gameoverScreen()
                    boss3_interactable.interacted = False
                    boss3_interactable.setText("Haven't you learned your lesson?")
                else:
                    boss3_interactable.interacted = False
                    progress+=1
    elif progress == 45:
        textQue.append("You beat me young one...")
        textQue.append("I am not deserving of this title...")
        textQue.append("You persevered through many hardships...")
        textQue.append("I know what your mission was. And you succeeded.")
        textQue.append("Very well... Your wish is granted...")
        textQue.append("Farewell.")
        progress+= 1
    elif progress == 46:
        if len(textQue)==0:
            level3_1.npcs = []
            level3_1.colliders = []
            level3_1.addCollider(Collider(pygame.Rect(360, 20, 35, 35), bucket_sprite))
            level3_1.addCollider(Portal(pygame.Rect(360, 20, 35, 35), 0, 0, 0))
            textQue.append("Time to meet Harold!")
            Harold.rect.x = 340
            Harold.rect.y = 375
            Harold.sprite = harold_left_sprite
            overworld.addNPC(Harold)
            progress+=1
    elif progress == 47:
        if len(textQue)==0 and currentScene == overworld:
            Harold.sprite = harold_back_sprite
            textQue.append("CONGRATS BUDDY! You did it!")
            textQue.append("I'm sure those fights were tiring.")
            textQue.append(["Why don't you visit your house and rest?", "You might even find your wish there too!"])
            Harold.setText(["Go inside!"])
            house.addNPC(NPC(pygame.Rect(450, 400, 50, 50), 1, "", "DAD"))
            house.addNPC(NPC(pygame.Rect(510, 400, 50, 50), 3, "", "MOM"))
            progress+=1
    elif progress == 48:
        if len(textQue) == 0 and currentScene == house:
            player.hitbox.y-=3
            if player.hitbox.y <= 450:
                textQue.append("YOU: Mom? Dad?")
                textQue.append("DAD: Son! You're okay!")
                textQue.append("MOM: We're so glad you made it home safe!")
                textQue.append(["DAD: You're probably wondering what in", "the world happened to us!"])
                textQue.append("DAD: Well... to be honest we don't know.")
                textQue.append(["MOM: One moment we were at home and", "the next moment everything was black."])
                textQue.append(["DAD: It's like I just woke up from a", "weird dream, and we were both back here."])
                textQue.append("MOM: Whatever happened it's over now.")
                progress+=1
    elif progress == 49:
        if len(textQue) == 0:
            Harold.rect.x = player.hitbox.x-50
            Harold.rect.y = 550
            Harold.sprite = harold_back_sprite
            house.addNPC(Harold)
            textQue.append("MOM: Oh? Who's this?")
            progress += 1
    elif progress == 50:
        Harold.rect.y-=3
        if Harold.rect.y <= 450:
            progress+=1
    elif progress == 51:
        textQue.append("HAROLD: Hi! I'm JoJo's friend.")
        textQue.append("MOM: Oh! Why didn't you say anything JoJo?")
        textQue.append(["HAROLD: It's okay. I just wanted to come in", "and say goodbye, buddy."])
        textQue.append(["HAROLD: I'll come and visit from time to time,", "don't worry!"])
        textQue.append(["HAROLD: All that matters is that your family", "is safe and sound!"])
        textQue.append("MOM: That's so sweet... um... what was your name?")
        textQue.append("HAROLD: Harold.")
        textQue.append(["HAROLD: Anyways bud, I'm off!", "I hope to see you again soon!"])
        progress += 1
    elif progress == 52:
        if len(textQue)== 0:
            Harold.sprite = harold_front_sprite
            Harold.rect.y+= 3
            if Harold.rect.y >= 550:
                house.npcs.remove(Harold)
                progress+=1
    elif progress == 53:
        textQue.append("DAD: That was nice of him to stop by.")
        textQue.append(["MOM: So what do you say to a nice", "home cooked meal JoJo? Now that we're all okay."])
        textQue.append("DAD: Sounds good to me!")
        progress+=1
    elif progress == 54:
        if len(textQue)==0:
            player.hitbox.x = 1000
            currentScene = endScene
            textQue.append("JoJo and his family were finally together again.")
            textQue.append(["With the help of a recently made green friend,", "JoJo was able to see his parents again."])
            textQue.append(["Now that everyone is safe and sound, what", "adventures will pop up next?"])
            textQue.append("Only time will tell.")
            progress+=1
    elif progress == 55:
        if len(textQue) == 0:
            progress+=1
    elif progress == 56:
        endGame()

#Random enemy battling encounters
def randomEncounter(background):
    num = randint(1, 1500)
    if num == 7:
        player.xVel = 0
        player.yVel = 0
        #starts a battle
        WildBattle = Battle([Enemy(pygame.Rect(300, 280, 75, 70), pygame.transform.scale(neighbor2TAINTED.spriteFront, (75, 70)), 49, 5, 8)], background, player_battle)
        changeMusic(battle_music)
        if WildBattle.startBattle() == False: #if player loses
            gameoverScreen()

#plays music for the current scene
def playMusic(currentScene):
    global currentMusic
    if (currentScene == overworld or currentScene == shop or currentScene == neighborHouse or currentScene == house) and currentMusic != overworld_music:
        changeMusic(overworld_music)
    elif (currentScene == level1_1 or currentScene == level1_2 or currentScene == level1_3 or currentScene == level1_4 or currentScene == level1_boss) and currentMusic != level1_music:
        changeMusic(level1_music)
    elif (currentScene == level2_1 or currentScene == level2_2 or currentScene == level2_3 or currentScene == level2_4 or currentScene == level2_5 or currentScene == level2_6 or currentScene == level2_7 or currentScene == level2_8 or currentScene == level2_Boss) and currentMusic != level2_music:
        changeMusic(level2_music)
    elif currentScene == level3_1 and currentMusic != level3_music:
        changeMusic(level3_music)

#changes music to the passed file
def changeMusic(music):
    global currentMusic
    currentMusic = music
    pygame.mixer.music.stop()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(1)
    time.sleep(1)

#End game screen handling
def endGame():
    screen.blit(overworldBackground, (0, 0))
    for collider in overworld.colliders:
        if not isinstance(collider, Portal):
            screen.blit(collider.sprite, (collider.rect.x, collider.rect.y))
    screen.blit(player_stand_forward, (375, 352))
    screen.blit(npc1_front_sprite, (325, 350))
    screen.blit(npc3_front_sprite, (425, 350))
    screen.blit(harold_front_sprite, (475, 350))
    screen.blit(npc2_front_sprite, (275, 350))
    screen.blit(npc4_front_sprite, (225, 350))
    screen.blit(thankYouText, (95, 125))
    screen.blit(moreLevelsText, (65, 450))
    pygame.display.update()
    time.sleep(10)
    sys.exit()




#~~~~~~~~~~~~~~~~~~~~~~~GAME LOOP~~~~~~~~~~~~~~~~~~~~~~~#

while True:
    playMusic(currentScene) #plays music

    clock.tick(60) #60 fps
    counter +=1
    mouse_pos = pygame.mouse.get_pos()

    #If player rests in bed it will play a small scene and refill health
    if currentScene==house and bed.interacted == True:
        textQue.append("You took a quick nap to recharge.")
        currentScene = endScene
        player.hitbox.x = 1000
        player_battle.health = 100
        if progress != 9:
            bed.interacted = False
    if bed.interacted == False and currentScene == endScene and len(textQue) == 0:
        player.hitbox.x = 275
        currentScene = house

    #Checks if story is enabled and plays the story if true
    if doStory:
            eventManager()
            if counter == 1:
                currentScene = house
    elif counter == 1:
        overworld.addCollider(Portal(pygame.Rect(310, 170, 110, 150), 0, 0, 0)); overworld.colliders.insert(31, Collider((pygame.Rect(310, 170, 110, 150)), well))


    # <editor-fold desc = "PLAYER MOVEMENT">
    if len(textQue) == 0:
        if player.collision(currentScene) : #player collision in current scene
            if player.vertical:
                player.getHitbox().move_ip(0, player.getYVel())
            else:
                player.getHitbox().move_ip(player.getXVel(), 0)
        if counter % 7  == 0:
            player.animate()

    # </editor-fold>

    #<editor-fold desc = "EVENT HANDLING">
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_z: #z Key to interact with objects
                if not len(textQue) > 0:
                    triggerInteraction = True
                else:
                    textQue.remove(textQue[0])
        player.move(event)
        player.collision(currentScene)
    #</editor-fold>

    checkPassages() #check current scene passages to other scenes

    #<editor-fold desc = "PLAYER INTERACTION">
    checkInteraction() #interaction with npcs or interactables
    triggerInteraction = False
    #</editor-fold>

    #Draws the current scene
    #<editor-fold desc = "BACKGROUND">
    screen.fill((0, 0, 0))
    screen.blit(currentScene.getBackground(), (0,0))
    player.blitted = False
    for i in currentScene.colliders: #draws colliders
            if not isinstance(i, Portal): #if it isnt a portal
                if player.getHitbox().y < i.getRect().y and not player.blitted:
                    displayNPC(currentScene)
                    screen.blit(player.getSprite(), player.getHitbox())
                    player.blitted = True
                screen.blit(i.getSprite(), i.getRect())
    #</editor-fold>

    #Blit the Player into the Scene
    if not player.blitted:
        displayNPC(currentScene)
        screen.blit(player.getSprite(), player.getHitbox())

    #Handles rain
    if raining==True and currentScene == overworld:
        thunderstorm()

    #Random enemy encounters if the scene permits it
    if currentScene.encounterEnemies and len(textQue) == 0:
       randomEncounter(pygame.transform.scale(pygame.image.load("Battle Scenes/OverworldBattleScene.png"), (750, 560)))

    #displays textbox and text if there is any stored
    displayText()

    pygame.display.update()
