import pygame
import time
import random

pygame.init()

tela_Altura= 600
tela_Largura=800
pygame.display.set_caption("Goku In The Space")
gameDisplay=pygame.display.set_mode((tela_Largura, tela_Altura))
fundo =pygame.image.load("assets/espaco.jpg")

clock=pygame.time.Clock()

nave=pygame.image.load("assets/GokuNave.gif")
padrao_X=340
padrao_Y=400

### funções ####
def mostrarNave(x,y):
    gameDisplay.blit( nave, (x,y))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameDisplay.blit(fundo, (0,0))
    mostrarNave(padrao_X,padrao_Y)
    pygame.display.update()
    clock.tick(60)
    