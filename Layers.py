import pygame as pg
class Layer(pg.sprite.Group):

    def __init__(self, z):
        super().__init__()
        self.z = z

    def draw(self, surface:pg.surface.Surface, time):
        # super().draw(surface)
        for i in self.sprites():
            if i.getAnimationFrameMax() != 0:
                if time%i.getAnimationFrameMax() == 0:
                    i.animar()
            i.draw(surface)
            # image = pg.image.load("./sprites/Kirby/Default.png").convert_alpha()
            # print(i.image.get_alpha())
            # surface.blit(i.image, (0,0))
            #surface.blit(i.image, (0,0))

    def moveAllDistance(self, distancia:tuple):
        for sprite in self.sprites():
            sprite.rect.x += distancia[0]
            sprite.rect.y += distancia[1]