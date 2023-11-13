import pygame as pg
from Object import Objects

class GUI:

    def __init__(self, display:pg.surface.Surface, backgroud:pg.surface.Surface, resolution=(720, 460), layers=7):
        self.__exit = False
        self._display:pg.surface.Surface = display
        self._backgroud:pg.surface.Surface = pg.transform.scale(backgroud, resolution)
        self.resolution = resolution
        self.__layers = [None]*layers
        self._backgroudInitial:pg.surface.Surface = backgroud

    def init(self):
        pass

    def restar(self):
        self._display.fill((0,0,0,0))
        self.init()

    def resize(self, resolution:tuple):
        self.resolution = resolution
        self._display = pg.transform.scale()

    def logic(self, nextGui=None):
        self._display.blit(self._backgroud, (0,0))
        for i in self.__layers:
            if i:
                i.draw(self.display, self.time)
        pg.display.update()

    def exit(self):
        self.__exit = True

    def getExit(self):
        return self.__exit

    def addObjectInLayer(self, object:object, z=0):
        if self.__layers[z]:
            self.__layers[z].add(object)
            return
        self.__layers[z] = Layer(z)
        self.__layers[z].add(object)

    def addObjectsInLayer(self, objects:Objects, z=0):
        if self.__layers[z]:
            for i in objects.sprites():
                self.__layers[z].add(i)
            return
        self.__layers[z] = Layer(z)
        for i in objects.sprites():
                self.__layers[z].add(i)

    def pause(self):
        return False