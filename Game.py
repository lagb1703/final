import os
from Control import Control
from Object import Object, Objects
from Layers import Layer
from physicalObject import physicalObject
from Playes import kirby
from Alarm import Alarm
import pygame as pg
import sys

class Game(Observable):

    game = None

    def __init__(self, resolution:tuple):
        super().__init__()
        self.resolution = resolution
        self.FPS = 60
        self.__exit = False
        self.display = None
        self.__guis = []

    @staticmethod
    def create(resolution:tuple = (1024, 720)):
        if not(Game.game):
            Game.game = Game(resolution)
        return Game.game

    def exit(self):
        self.__exit = True

    def gameLoop(self):
        pg.init()
        self.display = pg.display.set_mode(self.resolution)
        os.environ["SDL_VIDEO_CENTERED"] = '1'
        clock = pg.time.Clock()
        control = Control.create()
        while not(self.__exit):
            for i in self.__guis:
                i.logic()
            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         sys.exit()
            # clock.tick(self.FPS)
            # self.notifyAll()
            # collector = [[], [], self.time/self.FPS]
            # for i in self.__objects:
            #     i.update(colector=collector)
            # for i in collector[0]:
            #     self.addObserver(i)
            # for i in collector[1]:
            #     self.getObjectsGroup(i[1]).add(i[0])
            #     self.addObjectInLayer(i[0], i[2])
            pg.display.update()

    def rescale(self, newResolution):
        self.resolution = newResolution
        self.display = pg.display.set_mode(newResolution)

g:Game = Game.create(resolution=(720, 460))



imagen1 = pg.surface.Surface((100, 100))
imagen1.fill("BLACK")

di = {"initial":[[imagen1], 0]}

suelo = Objects("suelo")
suelo.add(Object(1, (500, 100), di, (25, 300)))
#suelo.add(Object(2, (500, 100), di, (101, 100)))
g.addObjectInLayer(suelo, z=1)
g.addObjectsGroup(suelo)


playerObjects = Objects("Player")
player = kirby({"suelo":suelo})
playerObjects.add(player)
g.addObjectsGroup(playerObjects)
g.addObjectsInLayer(playerObjects)
g.addObjectsGroup(Objects("bullets"))


g.gameLoop()