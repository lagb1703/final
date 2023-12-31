from noControllablePlayerObject import noControllablePlayerObject as ncpo
import pygame as pg
from Object import Objects
from Bullets import zanahoriaBullet
from Alarm import Alarm

load = pg.image.load

class magoDeLaVerdura(ncpo):

    def __init__(self, id, LevelResolution):
        imagen = pg.surface.Surface((100, 100))
        super().__init__(id, (1,1), {"initial":[[imagen], 0]}, initialPosition=LevelResolution,puntoVida=500)

class Cebolla(ncpo):

    def __init__(self, id, resolution):
        jefeCebolla = "./sprites/Cebolla/"
        cebolla = [[load(f"{jefeCebolla}/normal.png").convert_alpha()], 1]
        cebollaAtacando = [[load(f"{jefeCebolla}move {i}.png" for i in range(1, 5))],
        30]
        animaciones = {
            "initial":cebolla,
            "atacando":cebollaAtacando
        }
        super().__init__(id, (300, 300), animaciones
            , initialPosition=(resolution[0]-300, resolution[1]-50), puntoVida=500)

    def init(self):
        pass

class Zanahoria(ncpo):

    def __init__(self, id, grupos:Objects, resolution, ends=None):
        jefeZanahoria = "./sprites/Zanahoria/"
        zanahoriaNormal = [[load(f"{jefeZanahoria}normal.png").convert_alpha()], 1]
        zanahoriaLanzando = [[load(f"{jefeZanahoria}zanahoria {i}.png").convert_alpha() for i in range(2, 6)],
        60]
        animaciones = {
            "initial":zanahoriaNormal,
            "atacando":zanahoriaLanzando
        }
        self.screanResolution = resolution
        self.grupos = grupos
        self.__atacando = True
        self.__ends = ends
        self.__initial = False
        self.__animation = False
        super().__init__(id, (250, 400), animaciones
            , initialPosition=(0, 50), puntoVida=500)

    def init(self):
        pass

    def __inpactFunction(self, enemigo):
        enemigo.livePoints -= 10

    def __setNormal(self):
        self.setAnimationName("initial")

    def __atack(self):
        self.__atacando = True

    def update(self, colector=None):
        super().update(colector=colector)
        if self.__atacando:
            colector[0].append(
                Alarm(colector[2], 4, False, self.__setNormal)
            )
            colector[0].append(
                Alarm(colector[2], 40, False, self.__atack)
            )
            colector[1].append(
                (zanahoriaBullet(colector[2], self.grupos, self.__inpactFunction, self.screanResolution, 
                initialPosition=(self.rect.x + self.resolution[0]/2, self.rect.y + self.resolution[1]/2 + 40)),
                "bullets", 4)
                )
            self.setAnimationName("atacando")
            self.__atacando = False

    def dead(self):
        if self.__ends:
            self.__ends()
        super().dead()


class Papa(ncpo):
    
    def __init__(self, resolution):
        jefePapa = "./sprites/La papa/"
        papa = [[load(f"{jefePapa}la papa emergio.png").convert_alpha()], 60]
        papaEmergiendo = [[load(f"{jefePapa}emerge {i}.png" for i in range(1, 7))],
        30]

class Factory:
    
    def __init__(self):
        pass

    def createBoss(self):
        pass


class aparicionNormal(Factory):

    def __init__(self, resolution):
        self.__pila = [Papa(resolution), Cebolla(resolution), Zanahoria(resolution)]
        self.__currentInitial = self.__pila[0]

    def createBoss(self):
        if len(self.__pila) > 0:
            if(self.__currentInitial != self.__pila[0]):
                self.__currentInitial = self.__pila[0]
                self.__currentInitial.init()
                return self.__pila[0]