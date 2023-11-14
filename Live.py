from physicalObject import physicalObject

class Live(physicalObject):

    def __init__(self, id, resolution:tuple, animations,initialPosition = (0,0), initialSprite="initial", FPS = 60, puntoVida=100):
        super().__init__(id, resolution, animations, initialPosition=initialPosition, initialSprite=initialSprite, FPS=FPS)
        self.livePoints = puntoVida

    def dead(self):
        self.kill()

    def vida(self):
        pass

    def update(self):
        if self.livePoints < 0:
            self.dead()
        else:
            self.vida()