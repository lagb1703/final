from GUI import GUI
from Level import Level
from Control import Control
from Camera import Camera
from Object import Object, Objects
from Players import kirby
from Jefes import Zanahoria, Cebolla

from physicalObject import physicalObject
import pygame as pg
from pygame import mixer

class sueloDecorativo(Object):

    def __init__(self, id, posicion:tuple, medidas:tuple):
        imagen = pg.image.load("./sprites/Background/piso.png").convert_alpha()
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


class fin(GUI):

    def __init__(self, display:pg.surface.Surface, resolution:tuple):
        image = pg.image.load("./sprites/Background/good ending.jpg")
        mixer.music.load('./sprites/Background/WIN.mp3')
        mixer.music.play()
        super().__init__(display, image, resolution)
        self.init()

    def init(self):
        pass

    def logic(self, nextGui=None):
        super().logic()

class derrota(GUI):

    def __init__(self, display:pg.surface.Surface, resolution:tuple):
        image = pg.image.load("./sprites/Background/Death menu.jpg")
        mixer.music.load('./sprites/Background/GAME OVER.mp3')
        mixer.music.play()
        super().__init__(display, image, resolution)
        self.init()

    def init(self):
        pass

    def logic(self, nextGui=None):
        super().logic()
        
class entryLevel(Level):

    def __init__(self, display:pg.surface.Surface, resolution:tuple, screenResolution:tuple):
        image = pg.image.load("./sprites/Background/background.jpg")
        mixer.music.load('./sprites/Background/Music.mp3')
        mixer.music.play(-1)
        camera = Camera(0, 0, resolution)
        super().__init__(display, image, camera, resolution=resolution, screenResolution=screenResolution)
        self.init()
        self.__next = None

    def __loadVictorie(self):
        self.__next = fin(self._display, self.resolution)
        self.exit()

    def __loadDerrote(self):
        self.__next = derrota(self._display, self.resolution)
        self.exit()

    def init(self):
        decoracion = sueloDecorativo(0, (0, self.resolution[1]-30), (self.resolution[0], 30))
        sueloReal = paredInvisible(1, (0, self.resolution[1]-20), (self.resolution[0], 20))
        enemigos = Objects("enemigos")
        self.addObjectsGroup(enemigos)
        self.getObjectsGroup("decoracion").add(decoracion)
        self.getObjectsGroup("collition").add(sueloReal)
        jugador = kirby((500, 300), {
            "suelo":self.getObjectsGroup("collition"),
            "enemigos":enemigos
            }, ends=self.__loadDerrote)
        self.getObjectsGroup("player").add(jugador)
        zana = Zanahoria(2, self.getObjectsGroup("player"), self.resolution, ends=self.__loadVictorie)
        enemigos.add(zana)
        self.addObjectInLayer(decoracion, z=1)
        self.addObjectInLayer(jugador, z=2)
        self.addObjectsInLayer(self.getObjectsGroup("enemigos"), z=3)

    def logic(self, nextGui=None):
        super().logic(nextGui=nextGui)
        if self.__next:
            nextGui.append(self.__next)