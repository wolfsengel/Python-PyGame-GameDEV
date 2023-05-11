import pygame
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
 
dis = pygame.display.set_mode((800, 600))
#BORDES DE COLOR ROJO
pygame.draw.rect(dis, red, [0, 0, 800, 10])
pygame.draw.rect(dis, red, [0, 0, 10, 600])
pygame.draw.rect(dis, red, [0, 590, 800, 10])
pygame.draw.rect(dis, red, [790, 0, 10, 600])

game_over = False
 
x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    #SISTEMA DE COLISION CONTRA LOS BORDES
    if x1 > 800 or x1 < 0 or y1 > 600 or y1 < 0:
        game_over = True

    pygame.display.update()
 
    clock.tick(30)
#TEXTO EN PANTALLA
font_style = pygame.font.SysFont(None, 50)
message = font_style.render("Game Over", True, red)
#ESPERAR 10S PARA CERRAR
dis.blit(message, [250, 250])
pygame.display.update()
pygame.time.wait(10000)

pygame.quit()
quit()