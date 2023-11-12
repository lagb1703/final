import pygame as pg
class Layer(pg.sprite.Group):

    def __init__(self, z):
        super().__init__()
        self.z = z

    def draw(self, surface, time):
        super().draw(surface)
        for i in self.sprites():
            if i.getAnimationFrameMax() == 0:
                return
            if time%i.getAnimationFrameMax() == 0:
                i.animar()