import pygame 

pygame.init()

tela = pygame.display.set_mode([840, 420])
gameLoop = True
nome = pygame.display.set_caption('Run')


def jogo():
    tela.fill([19, 173, 235])

while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

   

    jogo()
    pygame.display.update()

# logica para verificar se esta segurando uma tecla

    # press = pygame.key.get_pressed()
    # if press[pygame.K_w]:
    #     print('segurando w')


# logica para verificar se uma tecla foi pressionada ou souta 

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w:
        #         print('funciona')
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_w:
        #         print('soutou o w')

    