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

nave_Largura=142
nave_Altura=170

moveX= 0

planeta2=pygame.image.load("assets/planeta2.gif")
planeta2_Largura=110
planeta2_Altura=107
planeta2_X= 300
planeta2_Y= -250
planeta2_Fall= + 1

### funções ####
def mostrarNave(x,y):
    gameDisplay.blit( nave, (x,y))

def mostrar_Planeta(x,y):
    gameDisplay.blit(planeta2, (x,y))


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                moveX = -7
            elif evento.key == pygame.K_RIGHT:
                moveX = + 7
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                moveX = 0

    

    if padrao_X > tela_Largura - nave_Largura:
        padrao_X = tela_Largura - nave_Largura
    elif padrao_X < 0:
        padrao_X = 0

    padrao_X= padrao_X + moveX

    gameDisplay.blit(fundo, (0,0))
    
    mostrarNave(padrao_X,padrao_Y)
    mostrar_Planeta(planeta2_X,planeta2_Y)
    planeta2_Y = planeta2_Fall + planeta2_Y
    if planeta2_Y > tela_Altura:
        planeta2_Y = 0 - planeta2_Altura
        planeta2_Fall += 1
        planeta2_X = random.randrange(0, tela_Largura)

    pygame.display.update()
    clock.tick(60)
    