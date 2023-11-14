from GUI import GUI
from Level import Level
from Control import Control
from Camera import Camera
from Object import Object
from Players import kirby

from physicalObject import physicalObject
import pygame as pg

class sueloDecorativo(Object):

    def __init__(self, id, posicion:tuple, medidas:tuple):
        imagen = pg.image.load("./sprites/Background/piso.png")
        #imagen = pg.surface.Surface((100, 100))
        #imagen.fill((255, 0, 0))
        super().__init__(id, medidas, {"initial":[[imagen], 0]}, initialPosition=posicion)

class paredInvisible(physicalObject):

    def __init__(self, id, posicion:tuple, medidas:tuple):
        imagen = pg.surface.Surface(medidas)
        imagen.fill((0,0,0,0))
        super().__init__(id, medidas, {"initial":[[imagen], 0]}, initialPosition=posicion)


class inicio(GUI):

    def __init__(self, display:pg.surface.Surface, resolution:tuple):
        image = pg.image.load("./sprites/Background/main menu.jpg")
        super().__init__(display, image, resolution)
        self.init()

    def init(self):
        pass

    def logic(self, nextGui=None):
        super().logic()
        if Control.control:
            self.exit()
            if nextGui:
                pass
            return
        Control.create()
        
class entryLevel(Level):

    def __init__(self, display:pg.surface.Surface, resolution:tuple, screenResolution:tuple):
        image = pg.image.load("./sprites/Background/background.jpg")
        camera = Camera(0, 0, resolution)
        super().__init__(display, image, camera, resolution=resolution, screenResolution=screenResolution)
        self.init()

    def init(self):
        decoracion = sueloDecorativo(0, (0, self.resolution[1]-30), (self.resolution[0], 30))
        sueloReal = paredInvisible(1, (0, self.resolution[1]-20), (self.resolution[0], 20))
        self.getObjectsGroup("decoracion").add(decoracion)
        self.getObjectsGroup("collition").add(sueloReal)
        jugador = kirby((100, 300), {"suelo":self.getObjectsGroup("collition")})
        self.getObjectsGroup("player").add(jugador)
        self.addObjectInLayer(decoracion, z=1)
        self.addObjectInLayer(jugador, z=2)
        #self.addObjectInLayer(paredInvisible)

    def logic(self, nextGui=None):
        super().logic(nextGui=nextGui)