import pygame
import time
import random
pygame.init()

tela_Altura=600
tela_Largura=800
pygame.display.set_caption("Sonic Run")
gameDisplay=pygame.display.set_mode((tela_Largura, tela_Altura))
icone=pygame.image.load("assets/icone.png")
pygame.display.set_icon(icone)
white=(255,255,255)
clock=pygame.time.Clock()
gameDisplay.fill(white)