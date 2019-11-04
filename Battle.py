#Battle.py
#Description: Battle sequence class for when a battle needs to occur. It is a turn based battle where you can attack or move,
#               and which ever person (player or enemy) gets the others health to 0 first wins. The battle class allows a battle
#               object to be instantiated so sprites and enemy status like health or attack can be changed each time.
#Name: Michael Bassani
#Created: Nov 20, 2017
#Last Modified: Feb 1, 2018

__author__ = 'Michael Bassani'

import sys
import time
import pygame
pygame.init()
from pygame.locals import *
from random import *
from LoadImages import *
from Enemy import *
from PlayerBattle import *
from LoadMusic import *

#Pygame stuff
screen = pygame.display.set_mode((750, 700))
clock = pygame.time.Clock()

#Hit box for turn selection at bottom of screen
moveRect = pygame.Rect(0, 630, 250, 70)
closeRect = pygame.Rect(250, 630, 250, 70)
rangeRect = pygame.Rect(500, 630, 250, 70)

#Variables
doAnimatePlayer = False
newPlayerRect = None

#~~~Constant Variables~~~#
#Colours
white = (255, 255, 255)
green = (50, 255, 50)
#Fonts
font = pygame.font.Font("Fonts/ARCADECLASSIC.TTF", 25)
bottomMenuFont = pygame.font.Font("Fonts/ARCADECLASSIC.TTF", 30)
healthFont = pygame.font.Font("Fonts/ARCADECLASSIC.TTF", 15)
#Vars
yourTurn = font.render("Your  Turn!", False, white)
#Objects
player = PlayerBattle(0, 70*5, player_battle_sprite) #default


class Battle:
    #Constructor
    def __init__(self, enemies, background, passedPlayer):
        global player
        player = passedPlayer
        #Variables
        self.bgSquare = pygame.Rect(0, 0, 75, 70)
        self.currentRectX = 0
        self.currentRectY = 0
        self.move = False
        self.attack = False
        self.playerTurn = True
        self.textShown = False
        self.text = ""
        self.attackType = ""
        self.enemies = enemies
        self.numEnemies = len(enemies) - 1
        self.damagedEnemy = 0
        self.bg = background
        self.currentEnemyTurn = 0
        self.thisEnemy = self.enemies[0]
        if enemies[0].hitbox.height == 140:
            enemies[0].rangedAttackRadius = 3
            enemies[0].closeAttackRadius = 2
        if enemies[0].hitbox.width == 140 and enemies[0].hitbox.height == 70:
            enemies[0].rangedAttackRadius = 3


    #Draws board
    def drawBoard(self):
        for i in range(0, 10):
            for j in range(1, 9):
                currentRect = pygame.Rect(75*i, 70*j, 75, 70)
                pygame.draw.rect(screen, white, currentRect, 1)

    #Draws radius around player for attack/move
    def drawRadius(self, list, colour): #pass a list of squares around the player, draws with colour
        for i in range(0, len(list)):
            pygame.draw.rect(screen, colour, list[i])
            pygame.draw.rect(screen, white, list[i], 1)

    #Checks if a selected spot is within a certain radius of an object
    def within(self, rad, currentRect, player): #pass radius around player, current square you're checking, and a player
        if player.hitbox.x > currentRect.x:
            higherX = player.hitbox.x
            lowerX = currentRect.x
        else:
            higherX = currentRect.x
            lowerX = player.hitbox.x

        if player.hitbox.y > currentRect.y:
            higherY = player.hitbox.y
            lowerY = currentRect.y
        else:
            higherY = currentRect.y
            lowerY = player.hitbox.y

        #returns true if square is in radius of the player
        if higherX-lowerX <=75*rad and higherY-lowerY <= 70*rad:
                return True
        return False #false otherwise

    #Checks if the player is within an enemy's list to attack.move
    def checkPlayerWithinEnemy(self, list): #pass a list of squares around the enemy
        for i in range(0, len(list)):
                currentRect = list[i]
                if currentRect == player.hitbox:
                    return True #returns true if player is in
        return False #false otherwise

    #Enemy Turn
    def enemyTurn(self):
        #Generates random number, enemy's turn is based on the number  (attack/move)
        if not self.thisEnemy.doAnimate:
            randNum = randint(1, 2)
            self.move = False
            self.attack = False
            if randNum == 1 and len(self.thisEnemy.moveRadiusRects) != 0:
                self.enemyMove() #moves
                self.displayTopText("Enemy moves!")
            else:
                self.enemyAttack() #attacks
                self.displayTopText(text)
            self.thisEnemy.hadTurn = True

    #Enemy movemeny
    def enemyMove(self):
        global doAnimateEnemy, newEnemyRect

        #Only runs if the enemy has spaces to move to
        if len(self.thisEnemy.moveRadiusRects) != 0:
            while True:
                #Chooses random square to move to in it's radius
                randNum = randint(0, len(self.thisEnemy.moveRadiusRects))

                #Check if the player or any enemies are on that square
                for i in range(len(self.thisEnemy.moveRadiusRects)):
                    c=0
                    rect = pygame.Rect(self.thisEnemy.moveRadiusRects[i].x, self.thisEnemy.moveRadiusRects[i].y, self.thisEnemy.hitbox.width, self.thisEnemy.hitbox.height)
                    if i == randNum and not rect.colliderect(player.hitbox): #checks if player is on that square
                        if len(self.enemies) > 1: #only runs through if there is more than 1 enemy
                            for j in range(len(self.enemies)):
                                if self.enemies[j].hitbox != self.thisEnemy.moveRadiusRects[i] and not self.enemies[j].hitbox.colliderect(self.thisEnemy.hitbox):
                                    c+=1
                                if c == 0: #counter equals 0 if no one is on that square
                                    self.thisEnemy.doAnimate = True
                                    self.thisEnemy.newRect = pygame.Rect(self.thisEnemy.moveRadiusRects[i].x,self.thisEnemy.moveRadiusRects[i].y  ,5, 5)
                                    return
                        else: #other wise don't need to check for other enemies
                            self.thisEnemy.doAnimate = True
                            self.thisEnemy.newRect = pygame.Rect(self.thisEnemy.moveRadiusRects[i].x,self.thisEnemy.moveRadiusRects[i].y  ,5, 5)
                            return


    #Enemy attack
    def enemyAttack(self):
        global text
        #random number generated to decide between close or ranged attack
        randNum = randint(1, 2)
        if randNum == 1: #ranged attack
            if self.checkPlayerWithinEnemy(self.thisEnemy.attackRadiusRects): #checks if player is within enemy's radius
                player.takeDamage(self.thisEnemy.attackPower) #player takes damage
                damage = str(self.thisEnemy.attackPower)
                text = "Enemy attacks you from a range! You took " + damage + " damage!"
                screen.blit(heart_sprite, (player.hitbox.x + 15, player.hitbox.y-50)) #displays damage on screen
                damageText = healthFont.render(str(self.thisEnemy.attackPower), False, white)
                damage = int(damage)

                #Displays text at the top of screen for enemy's turn
                if damage < 10:
                    screen.blit(damageText, (player.hitbox.x + 36, player.hitbox.y - 30))
                else:
                    screen.blit(damageText, (player.hitbox.x + 32, player.hitbox.y - 30))
            else:
                text = "Enemy attacks you were out of range!"
        else: #close attack
            if self.checkPlayerWithinEnemy(self.thisEnemy.moveRadiusRects): #checks if player is within enemy's radius
                player.takeDamage(self.thisEnemy.specialAttackPower) #player takes damage
                damage = str(self.thisEnemy.specialAttackPower)
                text = "Enemy attacks you from close range! You took " + damage + " damage!"
                screen.blit(heart_sprite, (player.hitbox.x + 15, player.hitbox.y-50)) #displays damage on screen
                damageText = healthFont.render(str(self.thisEnemy.specialAttackPower), False, white)
                damage = int(damage)

                #displays text at the top of the screen for enemy's turn
                if damage < 10:
                    screen.blit(damageText, (player.hitbox.x + 36, player.hitbox.y - 30))
                else:
                    screen.blit(damageText, (player.hitbox.x + 32, player.hitbox.y - 30))
            else:
                text = "Enemy attacks you were out of range!"
        self.thisEnemy.hadTurn = True

    #Animate the player moving
    def animatePlayer(self, rect):
        global doAnimatePlayer

        #compares the rect it is moving to with the player hitbox and animates the player accordingly
        if rect.x < player.hitbox.x:
            player.hitbox.x -= 3
        elif rect.x > player.hitbox.x:
            player.hitbox.x += 3
        elif rect.y < player.hitbox.y:
            player.hitbox.y -= 2
        elif rect.y > player.hitbox.y:
            player.hitbox.y += 2
        if rect.x == player.hitbox.x and rect.y == player.hitbox.y:
            self.playerTurn = False
            doAnimatePlayer = False

    #Animate enemy moving
    def animateEnemy(self, rect): #compares the rect it is moving to with the enemy hitbox and animates the enemy accordingly
        if rect.x < self.thisEnemy.hitbox.x:
            self.thisEnemy.hitbox.x -= 3
        elif rect.x > self.thisEnemy.hitbox.x:
            self.thisEnemy.hitbox.x += 3
        elif rect.y < self.thisEnemy.hitbox.y:
            self.thisEnemy.hitbox.y -= 2
        elif rect.y > self.thisEnemy.hitbox.y:
            self.thisEnemy.hitbox.y += 2
        if rect.x == self.thisEnemy.hitbox.x and rect.y == self.thisEnemy.hitbox.y:
            self.thisEnemy.doAnimate = False

    #Gets the attack radius of the player for ranged attacks
    def playerAttack(self):
        player.attackRadiusRects = [] #reset all the squares in the list

        #Gets all the squares (complicated pattern so it was done individually)
        for i in range(0, 7):
            if i == 0:
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x, player.hitbox.y-70*3, 75, 70))
            elif i == 1:
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x, player.hitbox.y-70*2, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x-75, player.hitbox.y-70*2, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x+75, player.hitbox.y-70*2, 75, 70))
            elif i == 2:
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x, player.hitbox.y-70*1, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x-75*2, player.hitbox.y-70*1, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x-75, player.hitbox.y-70*1, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x, player.hitbox.y-70*1, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x+75, player.hitbox.y-70*1, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x+75*2, player.hitbox.y-70*1, 75, 70))
            elif i == 3:
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x-75*3, player.hitbox.y, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x-75*2, player.hitbox.y, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x-75, player.hitbox.y, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x+75, player.hitbox.y, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x+75*2, player.hitbox.y, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x+75*3, player.hitbox.y, 75, 70))
            elif i == 4:
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x-75*2, player.hitbox.y+70*1, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x-75, player.hitbox.y+70*1, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x, player.hitbox.y+70*1, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x+75, player.hitbox.y+70*1, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x+75*2, player.hitbox.y+70*1, 75, 70))
            elif i == 5:
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x, player.hitbox.y+70*2, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x-75, player.hitbox.y+70*2, 75, 70))
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x+75, player.hitbox.y+70*2, 75, 70))
            elif i == 6:
                player.attackRadiusRects.append(pygame.Rect(player.hitbox.x, player.hitbox.y+70*3, 75, 70))

    #Checks if mouse is colliding with a rect in a list, sets it to specified colour
    def checkMouseRect(self, list, colour):
        mouse = pygame.mouse.get_pos()
        for i in range (0, 10):
            for j in range(1, 9):
                currentRect = pygame.Rect(75*i, 70*j, 75, 70)
                for r in range(0, len(list)):
                    if list[r].collidepoint(mouse):
                        pygame.draw.rect(screen, colour, list[r])
                        pygame.draw.rect(screen, white, list[r], 1)
                if currentRect.collidepoint(mouse):
                    currentColour = (255, 50, 50)
                    pygame.draw.rect(screen, currentColour, currentRect)
                else:
                    pygame.draw.rect(screen, white, currentRect, 1)

    #Displays the bottom menu for player controls
    def displayBottomMenu(self, mouse):
        pygame.draw.rect(screen, (100, 100, 100), (0, 630, 750, 70))
        pygame.draw.rect(screen, white, (0, 630, 750, 68), 2)
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 750, 70))

        pygame.draw.rect(screen, (200, 0, 0), moveRect)
        pygame.draw.rect(screen, (0, 200, 0), closeRect)
        pygame.draw.rect(screen, (0, 0, 200), rangeRect)
        if moveRect.collidepoint(mouse):
            pygame.draw.rect(screen, (255, 0, 0), moveRect)
        elif closeRect.collidepoint(mouse):
            pygame.draw.rect(screen, (0, 255, 0), closeRect)
        elif rangeRect.collidepoint(mouse):
            pygame.draw.rect(screen, (0, 0, 255), rangeRect)


        displayText = bottomMenuFont.render("MOVE", False, (0, 0, 0))
        screen.blit(displayText, (40,650))
        displayText = bottomMenuFont.render("CLOSE ATTACK", False, (0, 0, 0))
        screen.blit(displayText, (270,650))
        displayText = bottomMenuFont.render("RANGE ATTACK", False, (0, 0, 0))
        screen.blit(displayText, (520,650))

    #displays the text at top of screen for enemy turns
    def displayTopText(self, text):
        global textShown
        textShown = True
        pygame.draw.rect(screen, (50, 50, 50), (0, 0, 750, 70))
        pygame.draw.rect(screen, white, (0, 0, 750, 68), 2)

        displayText = font.render(text, False, white)
        screen.blit(displayText, (10, 10))
        pygame.display.update()
        time.sleep(2)


    #~~~~~BATTLE SEQUENCE~~~~~#
    def startBattle(self):
        #Sets player position
        player.hitbox.x = 150
        player.hitbox.y = 350

        #Main loop
        global doAnimatePlayer, newPlayerRect
        while True:
            #60fps
            clock.tick(60)

            #Variables
            self.textShown = False
            self.damagedEnemy = -1
            mouse = pygame.mouse.get_pos()
            self.numEnemies = len(self.enemies)

            if (self.numEnemies == 0): #checks if enemies are dead
                pygame.mixer.music.stop()
                if player.health <= 0:
                    player.health = 1
                return True
            screen.blit(self.bg, (0, 70)) #background

            #~~~EVENT HANDLING~~~#
            for event in pygame.event.get():
                if event.type == QUIT: #quit button
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN: #Mouse clicks
                    for i in range(len(player.moveRadiusRects)): #checks if click collides with a square in the players moving rad
                        c=0
                        if self.move == True: #if player chooses to move, and mouse clicks it, player moves
                            if player.moveRadiusRects[i].collidepoint(mouse):
                                for enemy in self.enemies: #checks if enemies are in that square
                                    if enemy.hitbox.colliderect(player.moveRadiusRects[i]):
                                        c+= 1
                                if c == 0: #counter is 0 if no one is in the square
                                    doAnimatePlayer = True
                                    self.move = False
                                    newPlayerRect = player.moveRadiusRects[i]
                                    break

                        #Checks if mouse click collides with a square in the players close attacking radius
                        if self.attackType == "close" and self.attack is True:
                            if player.moveRadiusRects[i].collidepoint(mouse):
                                for enemy in self.enemies: #checks all enemies
                                    if enemy.hitbox.colliderect(player.moveRadiusRects[i]): #if an enemy is in the square they take damage
                                        enemy.takeDamage(player.closeAttackPower)
                                        self.playerTurn = False
                                        self.damagedEnemy = enemy
                                        self.attack = False
                                        break
                    #Checks if mouse click collides with a square in the players ranged attacking radius
                    if self.attackType == "ranged" and self.attack == True:
                        for k in range (len(player.attackRadiusRects)):
                            if player.attackRadiusRects[k].collidepoint(mouse):
                                for enemy in self.enemies: #checks all enemies
                                    if enemy.hitbox.colliderect(player.attackRadiusRects[k]): #if an enemy is in the square they take damage
                                        enemy.takeDamage(player.rangedAttackPower)
                                        self.playerTurn = False
                                        self.damagedEnemy = enemy
                                        self.attack = False
                                        break
                    #Checks if mouse click collides with a turn button at the bottom of the screen
                    if moveRect.collidepoint(mouse):
                            self.move = True
                            self.attack = False
                    elif rangeRect.collidepoint(mouse):
                            self.attack = True
                            self.move = False
                            self.attackType = "ranged"
                    elif closeRect.collidepoint(mouse):
                            self.attack = True
                            self.move = False
                            self.attackType = "close"
                    break


            #Animates player moving to the square they choose if true
            if doAnimatePlayer:
                self.animatePlayer(newPlayerRect)

            #Resets player attack and move squares
            player.attackRadiusRects = []
            player.moveRadiusRects = []

            #Goes through all enemies
            for enemy in self.enemies:
                enemy.moveRadiusRects = [] #reset
                enemy.attackRadiusRects = [] #reset

                #~~~~DEPENDING ON ENEMY HITBOX SIZE, MOVING AND ATTACKING SQUARES ARE DETERMINED DIFFERENTLY~~~~#
                if enemy.hitbox.width == 75 and enemy.hitbox.height == 70: #enemy hitbox is 75x70
                    for i in range(0, 10):  #goes through all squares on the board and determines move/attack radius accordingly
                        for j in range(1, 9):
                            currentRect = pygame.Rect(i*75, j*70, 75, 70)
                            if self.within(enemy.closeAttackRadius, currentRect, enemy) and not enemy.hitbox.colliderect(currentRect):
                                if enemy.hitbox != currentRect:
                                    enemy.moveRadiusRects.append(currentRect)
                            if self.within(enemy.rangedAttackRadius, currentRect, enemy) and not enemy.hitbox.colliderect(currentRect):
                                if enemy.hitbox!= currentRect:
                                    enemy.attackRadiusRects.append(currentRect)
                elif enemy.hitbox.width == 150 and enemy.hitbox.height == 70: #enemy hitbox is 150x70
                    for i in range(0, 10): #goes through all squares on the board and determines attack radius accordingly
                        for j in range(1, 9):
                            currentRect = pygame.Rect(i*75, j*70, 75, 70)
                            if self.within(enemy.rangedAttackRadius, currentRect, enemy) and not enemy.hitbox.colliderect(currentRect):
                                if enemy.hitbox!= currentRect:
                                    enemy.attackRadiusRects.append(currentRect)
                    for i in range(0, 9): #goes through all squares on the board EXCEPT one column and determines move radius accordingly
                        for j in range(1, 9):
                            currentRect = pygame.Rect(i*75, j*70, 75, 70)
                            if self.within(enemy.closeAttackRadius, currentRect, enemy) and not enemy.hitbox.colliderect(currentRect):
                                if enemy.hitbox != currentRect:
                                    enemy.moveRadiusRects.append(currentRect)
                elif enemy.hitbox.width == 150 and enemy.hitbox.height == 140: #enemy hitbox is 150x140
                    for i in range(0, 10): #goes through all squares on the board and determines attack radius accordingly
                        for j in range(1, 9):
                            currentRect = pygame.Rect(i*75, j*70, 75, 70)
                            if self.within(enemy.rangedAttackRadius, currentRect, enemy) and not enemy.hitbox.colliderect(currentRect):
                                if enemy.hitbox!= currentRect:
                                    enemy.attackRadiusRects.append(currentRect)
                    for i in range(0, 9): #goes through all squares on the board EXCEPT one column and one row and determines move radius accordingly
                        for j in range(1, 8): #(CONT) so enemy doesnt go off screen
                            currentRect = pygame.Rect(i*75, j*70, 75, 70)
                            if self.within(enemy.closeAttackRadius, currentRect, enemy) and not enemy.hitbox.colliderect(currentRect) and not player.hitbox.colliderect(currentRect):
                                if enemy.hitbox != currentRect:
                                    enemy.moveRadiusRects.append(currentRect)

            #Determine player move radius squares
            for i in range(0, 10):
                for j in range(1, 9):
                    currentRect = pygame.Rect(i*75, j*70, 75, 70)
                    if self.within(player.closeAttackRadius, currentRect, player):
                        if player.hitbox != currentRect:
                            player.moveRadiusRects.append(currentRect)
            self.playerAttack() #gets player ranged attack radius

            #draw board
            self.drawBoard()
            if self.move == True:
                self.drawRadius(player.moveRadiusRects, (100, 100, 255))
                self.checkMouseRect(player.moveRadiusRects, (50, 50, 255))

            #draws radius around player for close or ranged attack
            if self.attack == True:
                if self.attackType == "close":
                    self.drawRadius(player.moveRadiusRects, (100, 255, 100))
                    self.checkMouseRect(player.moveRadiusRects, (50, 255, 50))
                if self.attackType == "ranged":
                    self.drawRadius(player.attackRadiusRects, (100, 255, 100))
                    self.checkMouseRect(player.attackRadiusRects, (50, 255, 50))

            #draws player and determines if player is dead or not
            if player.health <= 0:
                player.health = 0
                pygame.mixer.music.stop()
                return False
            screen.blit(player.sprite, player.hitbox)

            #Draw enemies
            for enemy in self.enemies:
                screen.blit(enemy.sprite, enemy.hitbox)
                if enemy.health <= 0:
                    enemy.health = 0

            #If enemy is damaged, damage shows up above their health bar
            for enemy in self.enemies:
                if self.damagedEnemy == enemy: #checks all enemies
                    if self.attackType == "ranged":
                        screen.blit(heart_sprite, (enemy.hitbox.x + 15, enemy.hitbox.y-50))
                        damageText = healthFont.render(str(player.rangedAttackPower), False, white)
                        if player.rangedAttackPower < 10:
                            screen.blit(damageText, (enemy.hitbox.x + 36, enemy.hitbox.y - 30))
                        else:
                            screen.blit(damageText, (enemy.hitbox.x + 32, enemy.hitbox.y - 30))
                    elif self.attackType == "close":
                        screen.blit(heart_sprite, (enemy.hitbox.x + 15, enemy.hitbox.y-50))
                        damageText = healthFont.render(str(player.closeAttackPower), False, white)
                        if player.closeAttackPower < 10:
                            screen.blit(damageText, (enemy.hitbox.x + 36, enemy.hitbox.y - 30))
                        else:
                            screen.blit(damageText, (enemy.hitbox.x + 32, enemy.hitbox.y - 30))

            #Displays bottom menu controls
            self.displayBottomMenu(mouse)

            #Displays your turn at top of screen
            screen.blit(yourTurn, (10, 10))

            #Determines if it is the players turn
            if self.currentEnemyTurn == self.numEnemies and not self.thisEnemy.doAnimate:
                self.playerTurn = True
                self.currentEnemyTurn = 0

            #Determines current enemy
            thisEnemy = self.enemies[self.currentEnemyTurn-1]

            #Move controls off screen during enemy turn so player cannot press them
            if not self.playerTurn:
                moveRect.y = 1000
                closeRect.y=1000
                rangeRect.y=1000
                if not self.thisEnemy.hadTurn:
                    self.enemyTurn() #enemy turn
                elif self.thisEnemy.doAnimate:
                    self.animateEnemy(thisEnemy.newRect)
                else:
                    self.currentEnemyTurn += 1
                    self.thisEnemy.hadTurn = False
            else: #put controls back
                moveRect.y = 630
                closeRect.y= 630
                rangeRect.y= 630

            #removes enemy from battle if health is 0
            for enemy in self.enemies:
                if enemy.health <=0:
                    self.enemies.remove(enemy)

            #Draw health bars last so they can always be seen
            for enemy in self.enemies:
                pygame.draw.rect(screen, (255, 0, 0), (enemy.hitbox.x-12, enemy.hitbox.y-10, enemy.health, 5))
            pygame.draw.rect(screen, (255, 0, 0), (player.hitbox.x-12, player.hitbox.y-10, player.health, 5))
            player_health = healthFont.render(str(player.health), False, white)
            screen.blit(player_health, (player.hitbox.x - 12, player.hitbox.y - 25))

            pygame.display.update()
