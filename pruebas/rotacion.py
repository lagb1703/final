""" 
 Mostramos como usar un sprite respaldado por una gráfica
  
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
import pygame
import random
 
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
 
# Esta clase representa la pelota        
# Deriva de la clase "Sprite" en Pygame
class Bloque(pygame.sprite.Sprite):
     
    # LEER ANTES DE USAR:
    # Este constructor nos deja utilizar cualquier tipo de gráfica:
    # mi_sprite = Bloque("cualquier_grafica.png").convert_alpha()
    # Pero si NO quieres cualquier gráfica, puedes usar en su lugar lo siguiente:
    '''
    def __init__(self):
        super().__init__() 
 
        self.image = pygame.image.load("mi_grafica.png").convert_alpha().convert()
 
        # Establecemos el color de fondo como transparente. Ajustamos a BLANCO si tu
        # fondo es BLANCO.
        self.image.set_colorkey(BLANCO)
 
        self.rect = self.image.get_rect()
    '''
    def __init__(self, filename, colorkey):
        # Llama al constructor de la clase padre (Sprite) 
        super().__init__() 
 
        # Crea una imagen del bloque y lo rellena de color.
        # Esto podría ser también una imagen cargada desde el disco duro.
        self.imagen_original = pygame.image.load(filename).convert()
        self.image = self.imagen_original
 
        # Establecemos el color de fondo como transparente. Ajustamos a BLANCO si tu
        # fondo es BLANCO.
        self.image.set_colorkey(colorkey)
 
        # Obtenemos el objeto rectángulo que posee las dimensiones de la imagen
        # Actualizamos la posición de ese objeto estableciendo los valores para 
        # rect.x y rect.y
        self.rect = self.image.get_rect()
         
        self.angulo = 0
        self.cambio_angulo = 0
         
    def update(self):
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.angulo += self.cambio_angulo
        self.angulo = self.angulo % 360
 
# Inicializamos Pygame
pygame.init()
 
# Establecemos el alto y largo de la pantalla
pantalla_largo = 700
pantalla_alto = 400
pantalla = pygame.display.set_mode([pantalla_largo, pantalla_alto])
 
# Esta es una lista de 'sprites.' Cada bloque en el programa es
# añadido a la lista. La lista es gestionada por una clase llamada 'Group.'
listade_bloques = pygame.sprite.Group()
 
# Esta es una lista de cada uno de los sprites. Así como del resto de bloques y el bloque protagonista.
listade_todoslos_sprites = pygame.sprite.Group()
 
for i in range(50):
    # Esto representa un bloque
    bloque = Bloque("dino.png", NEGRO)
 
    # Establecemos una ubicación aleatoria para el bloque
    bloque.rect.x = random.randrange(pantalla_largo)
    bloque.rect.y = random.randrange(pantalla_alto)
    bloque.angulo = random.randrange(360)
    bloque.cambio_angulo = random.randrange(-1, 2)
    # Añadimos el  bloque a la lista de objetos
    listade_bloques.add(bloque)
    listade_todoslos_sprites.add(bloque)
     
# Creamos un bloque protagonista ROJO
protagonista = Bloque("star.png", NEGRO)
protagonista.cambio_angulo = 45
listade_todoslos_sprites.add(protagonista)
 
# Iteramos hasta que el usuario pulse el botón de salida
hecho = False
 
# Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
 
puntuacion = 0
 
# -------- Bucle principal del Programa -----------
while not hecho:
    for evento in pygame.event.get(): # User did something
        if evento.type == pygame.QUIT: # If user clicked close
            hecho = True # Flag that we are done so we exit this loop
 
    # Limpiamos la pantalla
    pantalla.fill(BLANCO)
 
    # Obtenemos la posición actual del ratón. Esto devuelve la posición
    # como una lista de dos números.
    pos = pygame.mouse.get_pos()
     
    # Extraemos la x e y de la lista, 
    # Tal como si extrajéramos letras de una cadena de texto.
    # Colocamos al objeto protagonista en la ubicación del ratón.
    protagonista.rect.x = pos[0]
    protagonista.rect.y = pos[1]
     
    listade_todoslos_sprites.update()
     
    # Observamos si el bloque protagonista ha colisionado con algo.
    lista_impacto_bloques = pygame.sprite.spritecollide(protagonista, listade_bloques, True)  
     
    # Comprobamos la lista de colisiones
    for bloque in lista_impacto_bloques:
        puntuacion += 1
        print( puntuacion )
         
    # Dibujamos todos los sprites
    listade_todoslos_sprites.draw(pantalla)
     
    # Limitamos a 60 fotogramas por segundo
    reloj.tick(60)
 
    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
 
pygame.quit()