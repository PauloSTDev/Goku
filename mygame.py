import pygame
import time
import random

pygame.init()

def game_loop():
    tela_Altura= 600
    tela_Largura=800
    pygame.display.set_caption("Goku In The Space")
    gameDisplay=pygame.display.set_mode((tela_Largura, tela_Altura))
    fundo =pygame.image.load("assets/espaco.jpg")
    icone = pygame.image.load("assets/icon.jpg")
    pygame.display.set_icon(icone)

    clock=pygame.time.Clock()

    nave=pygame.image.load("assets/GokuNave.gif")
    padrao_X=330
    padrao_Y=440

    nave_Largura=73
    nave_Altura=116

    moveX= 0
    planeta1=pygame.image.load("assets/planeta1.png")
    planeta1_Largura=118
    planeta1_Altura=118
    planeta1_X= 100
    planeta1_Y= -250
    planeta1_Fall= + 1

    planeta2=pygame.image.load("assets/planeta2.png")
    planeta2_Largura=110
    planeta2_Altura=107
    planeta2_X= 300
    planeta2_Y= -250
    planeta2_Fall= + 1

    black=(0,0,0)
    blue=(100,0,200)
    pygame.mixer.music.load("assets/song.mp3")
    pygame.mixer.music.play(-1)
    desvios=0
    explosao=pygame.mixer.Sound("assets/explosao.wav")
    ### funções ####
    def mostrarNave(x,y):
        gameDisplay.blit( nave, (x,y))

    def mostrar_Planeta(objeto,x,y):
        gameDisplay.blit(objeto, (x,y))

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def messageDisplay(text):
        largeText = pygame.font.Font("freesansbold.ttf",75)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center=((tela_Largura/2), (tela_Altura/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(3)
        game_loop()

    def dead():
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(explosao)
        messageDisplay("Planeta Errado!")
    
    def contador(Desviados):
        font = pygame.font.SysFont(None, 25)
        text = font.render ("Planetas Desviados: " + str(desvios), True, blue)
        gameDisplay.blit(text, (10,30))

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

        mostrar_Planeta(planeta2, planeta2_X,planeta2_Y)
        planeta2_Y = planeta2_Fall + planeta2_Y
        if planeta2_Y > tela_Altura:
            planeta2_Y = 0 - planeta2_Altura
            planeta2_Fall += 1
            desvios = desvios + 1
            planeta2_X = random.randrange(0, tela_Largura)
            if planeta2_Fall >=12:
                planeta2_Fall = 12
                
        
        mostrar_Planeta(planeta1, planeta1_X,planeta1_Y)
        planeta1_Y = planeta1_Fall + planeta1_Y
        if planeta1_Y > tela_Altura:
            planeta1_Y = 0 - planeta2_Altura
            planeta1_Fall += 2
            desvios = desvios + 1
            planeta1_X = random.randrange(0, tela_Largura)
            if planeta1_Fall >=12:
                planeta1_Fall = 12
                
        
        if padrao_Y < planeta2_Y + planeta2_Altura:
            if padrao_X < planeta2_X and padrao_X + nave_Largura > planeta2_X or planeta2_X + planeta2_Largura > padrao_X and planeta2_X + planeta2_Largura < padrao_X + nave_Largura:
                dead()
        if padrao_Y < planeta1_Y + planeta1_Altura:
            if padrao_X < planeta1_X and padrao_X + nave_Largura > planeta1_X or planeta1_X + planeta1_Largura > padrao_X and planeta1_X + planeta1_Largura < padrao_X + nave_Largura:
                dead()

        contador(desvios)
        pygame.display.update()
        clock.tick(60)
game_loop()
    