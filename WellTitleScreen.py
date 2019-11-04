#WellTitleScreen.py
#Description: In game title screen for level selection. Player clicks on the level to go to.
#Name: Michael Bassani
#Created: Nov 20, 2017
#Last Modified: Feb 1, 2018

import pygame, sys
from pygame.locals import *
pygame.init()

class WellTitleScreen:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((750, 700))
        self.black = (0, 0, 0)
        self.levelFont = pygame.font.Font("Fonts/ARCADECLASSIC.TTF", 75)
        self.msgFont = pygame.font.Font("Fonts/ARCADECLASSIC.TTF", 45)
        self.lockLevel = 2
        self.msg1 = self.msgFont.render("Return", True, ( 200, 200 , 200))
        self.msg2 = self.msgFont.render("To", True, (200, 200, 200))
        self.msg3 = self.msgFont.render("Surface", True, (200, 200, 200))

        self.bg = pygame.transform.scale(pygame.image.load("Title Images/mossystone.png"), (1024, 700))
        self.lock = pygame.transform.scale(pygame.image.load("Title Images/lock.png"), (52, 60))
        self.arrowWhite = pygame.transform.scale(pygame.image.load("Title Images/bucket.png"), (300, 330))
        self.arrowBlue = pygame.transform.scale(pygame.image.load("Title Images/red arrow.png"), (300, 330))

        self.levelOneRect = pygame.Rect(350, 10, 350, 75)
        self.levelTwoRect = pygame.Rect(350, 110, 350, 75)
        self.levelThreeRect = pygame.Rect(350, 210, 350, 75)
        self.levelFourRect = pygame.Rect(350, 310, 350, 75)
        self.levelFiveRect = pygame.Rect(350, 410, 350, 75)
        self.levelSixRect = pygame.Rect(350, 510, 350, 75)
        self.levelSevenRect = pygame.Rect(350, 610, 350, 75)
        self.arrowRect = pygame.Rect(20, 200, 300, 330)

        self.rects = [self.levelOneRect, self.levelTwoRect, self.levelThreeRect, self.levelFourRect, self.levelFiveRect, self.levelSixRect, self.levelSevenRect]
        self.menu = True

    def drawLevels(self, locklevel):
        pygame.draw.rect(self.screen, self.black, self.levelOneRect, 3)
        self.level_one = self.levelFont.render("LEVEL 1", True, (255, 255, 255))
        self.screen.blit(self.level_one, (360, 10))
        pygame.draw.rect(self.screen, self.black, self.levelTwoRect, 3)
        self.level_two = self.levelFont.render("LEVEL 2", True, (255, 255, 255))
        self.screen.blit(self.level_two, (360, 110))
        pygame.draw.rect(self.screen, self.black, self.levelThreeRect, 3)
        self.level_three = self.levelFont.render("LEVEL 3", True, (255, 255, 255))
        self.screen.blit(self.level_three, (360, 210))
        pygame.draw.rect(self.screen, self.black, self.levelFourRect, 3)
        self.level_four = self.levelFont.render("LEVEL 4", True, (255, 255, 255))
        self.screen.blit(self.level_four, (360, 310))
        pygame.draw.rect(self.screen, self.black, self.levelFiveRect, 3)
        self.level_five = self.levelFont.render("LEVEL 5", True, (255, 255, 255))
        self.screen.blit(self.level_five, (360, 410))
        pygame.draw.rect(self.screen, self.black, self.levelSixRect, 3)
        self.level_six = self.levelFont.render("LEVEL 6", True, (255, 255, 255))
        self.screen.blit(self.level_six, (360, 510))
        pygame.draw.rect(self.screen, self.black, self.levelSevenRect, 3)
        self.level_seven = self.levelFont.render("LEVEL 7", True, (255, 255, 255))
        self.screen.blit(self.level_seven, (360, 610))

        if locklevel < 8 and locklevel > 0:
            for i in range(locklevel,8):
                self.screen.blit(self.lock, (635, i*100 - 85))

        self.screen.blit(self.arrowWhite, self.arrowRect)
        self.screen.blit(self.msg1, (100, 560))
        self.screen.blit(self.msg2, (150, 590))
        self.screen.blit(self.msg3, (90, 620))
    def mainLoop(self, locklevel):
        while (self.menu):
            self.clock.tick(60)
            mouse = pygame.mouse.get_pos()

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.bg, (0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    for i in range (0, len(self.rects)):
                        if self.rects[i].collidepoint(mouse) and locklevel > i+1:
                            if self.rects[i] == self.levelOneRect:
                                return "level 1"
                            elif self.rects[i] == self.levelTwoRect:
                                return "level 2"
                            elif self.rects[i] == self.levelThreeRect:
                                return "level 3"
                            elif self.rects[i] == self.levelFourRect:
                                return "level 4"
                            elif self.rects[i] == self.levelFiveRect:
                                return "level 5"
                            elif self.rects[i] == self.levelSixRect:
                                return "level 6"
                            else:
                                return "level 7"
                    if self.arrowRect.collidepoint(mouse):
                        self.menu = False
                        return"surface"



            for rect in self.rects:
                if rect.collidepoint(mouse):
                    pygame.draw.rect(self.screen, (50, 50, 50), rect)

            self.drawLevels(locklevel)

            if self.arrowRect.collidepoint(mouse):
                self.arrowRect.y  = 185
            else:
                self.arrowRect.y = 200

            pygame.display.update()

    def reset(self):
        self.menu = True
