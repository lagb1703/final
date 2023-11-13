from GUI import GUI
from Control import Control
import pygame as pg

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
                nextGui.append("nada")
            return
        Control.create()
        
# class entryLavel()