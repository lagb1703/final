import pygame

pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))

# Variable para controlar si se ha detectado un botón presionado
boton_presionado = False

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN or event.type == pygame.JOYBUTTONDOWN:
            boton_presionado = True

    if boton_presionado:
        running = False

pygame.quit()