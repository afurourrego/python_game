#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()
pygame.init()
# drop    = pygame.mixer.Sound('Sounds/drop.ogg')
# lines   = pygame.mixer.Sound('Sounds/lines.ogg')
# move    = pygame.mixer.Sound('Sounds/move.ogg')
# rotate  = pygame.mixer.Sound('Sounds/rotate.ogg')
# tetris  = pygame.mixer.Sound('Sounds/tetris.ogg')
# success  = pygame.mixer.Sound('Sounds/success.ogg')
drop    = pygame.mixer.Sound('D:\GtiHub\python_game\Sounds\drop.ogg')
lines   = pygame.mixer.Sound('D:\GtiHub\python_game\Sounds\lines.ogg')
move    = pygame.mixer.Sound('D:\GtiHub\python_game\Sounds\move.ogg')
rotate  = pygame.mixer.Sound('D:\GtiHub\python_game\Sounds\rotate.ogg')
tetris  = pygame.mixer.Sound('D:\GtiHub\python_game\Sounds\tetris.ogg')
success  = pygame.mixer.Sound('D:\GtiHub\python_game\Sounds\success.ogg')

def playMusic():
    pygame.mixer.music.load('D:\GtiHub\python_game\Sounds\music.ogg')
    pygame.mixer.music.play(-1)

def pauseMusic():
    pygame.mixer.music.pause()

def unpauseMusic():
    pygame.mixer.music.unpause()

def stopMusic():
    pygame.mixer.music.stop()

def playDrop():
    pygame.mixer.Sound.play(drop)

def playMove():
    pygame.mixer.Sound.play(move)

def playLines():
    pygame.mixer.Sound.play(lines)

def playRotate():
    pygame.mixer.Sound.play(rotate)

def playTetris():
    pygame.mixer.Sound.play(tetris)

def playSuccess():
    pygame.mixer.Sound.play(success)
