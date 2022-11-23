'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
'''

import pygame
pygame.mixer.init()
pygame.mixer.music.load('021.mp3.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()