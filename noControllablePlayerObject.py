from Live import Live

class noControllablePlayerObject:

    def __init__(self, id, resolution:tuple, animations,initialPosition = (0,0), initialSprite="initial", FPS = 60, puntoVida=60):
        super().__init__(id, resolution, animations, initialPosition=initialPosition, initialSprite=initialSprite, FPS=FPS, puntoVida=puntoVida)