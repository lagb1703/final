import os
import pygame as pg
import sys


from GUI import GUI
from Level import Level
from guisEntitys import inicio

class Game:

    game = None

    def __init__(self, resolution:tuple):
        self.resolution = resolution
        self.FPS = 60
        self.__exit = False
        self.display = None
        self.__guis = None

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
        self.__guis = [inicio(self.display, self.resolution)]
        os.environ["SDL_VIDEO_CENTERED"] = '1'
        clock = pg.time.Clock()
        while not(self.__exit) and len(self.__guis) > 0:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            nextGui = []
            currentGui:GUI = self.__guis[0]
            if not(currentGui):
                return
            currentGui.logic(nextGui=nextGui)
            if currentGui.getExit():
                del self.__guis[0]
            if len(nextGui) > 0:
                self.__guis.insert(0, nextGui[0])

    def rescale(self, newResolution):
        self.resolution = newResolution
        self.display = pg.display.set_mode(newResolution)

g:Game = Game.create(resolution=(720, 460))



# imagen1 = pg.surface.Surface((100, 100))
# imagen1.fill("BLACK")

# di = {"initial":[[imagen1], 0]}

# suelo = Objects("suelo")
# suelo.add(Object(1, (500, 100), di, (25, 300)))
# #suelo.add(Object(2, (500, 100), di, (101, 100)))
# g.addObjectInLayer(suelo, z=1)
# g.addObjectsGroup(suelo)


# playerObjects = Objects("Player")
# player = kirby({"suelo":suelo})
# playerObjects.add(player)
# g.addObjectsGroup(playerObjects)
# g.addObjectsInLayer(playerObjects)
# g.addObjectsGroup(Objects("bullets"))


g.gameLoop()