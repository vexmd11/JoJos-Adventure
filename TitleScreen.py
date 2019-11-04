#TitleScreen.py
#Description: Starting title screen for the game. Has a play button, instructions, and a quit button, graphics and music
#Name: Michael Bassani
#Created: Jan 28, 2018
#Last Modified: Feb 1, 2018

__author__ = 'Michael Bassani'

from SceneLoading import *
import pygame, sys
from pygame.locals import *
from LoadMusic import *
pygame.init()

background = overworldBackground

clock = pygame.time.Clock()
screen = pygame.display.set_mode((750, 700))

#Fonts
titleFont = pygame.font.Font("Fonts/ARCADECLASSIC.TTF", 75)
menuFont = pygame.font.Font("Fonts/ARCADECLASSIC.TTF", 55)
insFont = pygame.font.Font("Fonts/ARCADECLASSIC.TTF", 30)

#Text
title = titleFont.render("JoJos Bizzare", False, (255, 255, 255))
bgTitle = titleFont.render("JoJos Bizzare", False, (0, 0, 0))
title2 = titleFont.render("Adventure", False, (255, 255, 255))
bgTitle2 = titleFont.render("Adventure", False, (0, 0, 0))
playText = titleFont.render("Play", False, (0, 0, 0))
instructionsText = menuFont.render("Instructions", False, (0, 0, 0))
quitText = titleFont.render("Quit", False, (0, 0, 0))
backText = titleFont.render("BACK", False, (0, 0, 255))
insText = titleFont.render("Instructions", False, (255, 255, 255))
insTextbg = titleFont.render("Instructions", False, (0, 0, 0))
playerText = insFont.render("This is JoJo! He is your character", False, (255, 255, 255))
moveText = insFont.render("You  can  move  him  with  the  arrow  keys", False, (255, 255, 255))
interactText = insFont.render("By  pressing                 you  can  interact", False, (255, 255, 255))
interactText2 = insFont.render("with  NPCs  and  objects  around  you!", False, (255, 255, 255))
zText = menuFont.render("Z", False, (0, 0, 0))
zText2 = menuFont.render("Z", False, (255, 255, 255))
battleText = insFont.render("Sometimes  interacting  with  people  will", False, (255, 255, 255))
battleText2 = insFont.render("cause  a  battle  to  start!  Battling  is", False, (255, 255, 255))
battleText3 = insFont.render("controlled  with  your  mouse  or  track pad!", False, (255, 255, 255))
healText = insFont.render("You  can  always  heal  from  battle  by", False, (255, 255, 255))
healText2 = insFont.render("sleeping  in  your  bed  at  home!", False, (255, 255, 255))
puzzleText = insFont.render("To  get  to  each  levels  boss  you", False, (255, 255, 255))
puzzleText2 = insFont.render("must  solve  the  levels  puzzle!", False, (255, 255, 255))
bossText = insFont.render("Beat  all  three  of  the  bosses  to", False, (255, 255, 255))
bossText2 = insFont.render("complete  the  game!", False, (255, 255, 255))

#Graphics
player = player_battle_sprite
npc = pygame.transform.scale(npc2_front_sprite, (75, 70))
bucket = pygame.transform.scale(bucket_sprite, (50, 50))
heart = pygame.transform.scale(heart_sprite, (75, 70))
bed = pygame.transform.scale(bed_sprite, (60, 95))
boss = boss2_sprite
hole = pygame.transform.scale(hole_sprite, (75, 70))

#Hitbox's
playRect = pygame.Rect(200, 300, 375, 90)
instructionsRect = pygame.Rect(200, 425, 375, 90)
quitRect = pygame.Rect(200, 550, 375, 90)
backRect = pygame.Rect(100, 625, 175, 75)

#Play Music
pygame.mixer.music.load(overworld_music)
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(1)

def instructions():
    while True:
        clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if backRect.collidepoint(mouse_pos):
                    return

        screen.blit(background, (0, 0))
        for collider in overworld.colliders:
            screen.blit(collider.sprite, (collider.rect.x, collider.rect.y))

        screen.blit(insTextbg, (20, 25))
        screen.blit(insText, (25, 30))

        screen.blit(player, (20, 125))
        screen.blit(playerText, (100, 125))
        screen.blit(moveText, (100, 155))

        screen.blit(npc, (20, 200))
        screen.blit(bucket, (650, 210))
        screen.blit(interactText, (100, 200))
        screen.blit(zText, (303, 180))
        screen.blit(zText2, (308, 185))
        screen.blit(interactText2, (100, 230))

        screen.blit(heart, (20, 275))
        screen.blit(battleText, (100, 275))
        screen.blit(battleText2, (100, 305))
        screen.blit(battleText3, (100, 335))

        screen.blit(bed, (20, 360))
        screen.blit(healText, (100, 380))
        screen.blit(healText2, (100, 410))

        screen.blit(hole, (20, 455))
        screen.blit(puzzleText, (100, 455))
        screen.blit(puzzleText2, (100, 485))

        screen.blit(boss, (400, 555))
        screen.blit(bossText, (100, 530))
        screen.blit(bossText2, (100, 560))

        pygame.draw.rect(screen, (0, 0, 0), backRect,3)
        screen.blit(backText, (backRect.x + 5, backRect.y))

        if backRect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (255, 255, 255), backRect,3)

        pygame.display.update()

while True:
    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if playRect.collidepoint(mouse_pos):
                import CPT
            elif instructionsRect.collidepoint(mouse_pos):
                instructions()
            elif quitRect.collidepoint(mouse_pos):
                sys.exit()

    screen.blit(background, (0, 0))
    for collider in overworld.colliders:
        screen.blit(collider.sprite, (collider.rect.x, collider.rect.y))

    screen.blit(bgTitle, (115, 95))
    screen.blit(bgTitle2, (195, 170))
    screen.blit(title, (120, 100))
    screen.blit(title2, (200, 175))


    if playRect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (50, 50, 255), playRect)
    elif instructionsRect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (50, 50, 255), instructionsRect)
    elif quitRect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (50, 50, 255), quitRect)

    pygame.draw.rect(screen, (0, 0, 0), playRect, 5)
    pygame.draw.rect(screen, (0, 0, 0), instructionsRect, 5)
    pygame.draw.rect(screen, (0, 0, 0), quitRect, 5)

    screen.blit(playText, (305, 310))
    screen.blit(instructionsText, (202, 445))
    screen.blit(quitText, (310, 560))

    pygame.display.update()