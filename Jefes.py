from noControllablePlayerObject import noControllablePlayerObject as ncpo
import pygame as pg

load = pg.image.load

class magoDeLaVerdura(ncpo):

    def __init__(self, id, LevelResolution):
        jefeZanahoria = "./sprites/Zanahoria/"
        jefePapa = "./sprites/La papa/"
        jefeCebolla = "./sprites/Cebolla/"
        zanahoriaNormal = [[load(f"{jefeZanahoria}normal.png")], 1]
        zanahoriaLanzando = [[load(f"{jefeZanahoria}zanahoria{i}.png" for i in range(2, 6))],
        30]
        papa = [[load(f"{jefePapa}la papa emergio.png")], 60]
        papaEmergiendo = [[load(f"{jefePapa}emerge {i}.png" for i in range(1, 7))],
        30]
        cebolla = [[load(f"{jefeCebolla}/normal.png")], 1]
        cebollaAtacando = [[load(f"{jefeCebolla}move {i}.png" for i in range(1, 5))],
        30]
        animaciones ={
            "initial":zanahoriaNormal,
            "zanahoriaLanzando":zanahoriaLanzando,
            "papaInitial":papa,
            "papaEmergiendo":papaEmergiendo,
            "cebollaInitial":cebolla,
            "cebollaAtacando":cebollaAtacando
        }
        super().__init__(id, (1,1), animaciones, initialPosition=LevelResolution,puntoVida=500)

class cebolla(ncpo):

    def __init__():
        pass

class Zanahoria(ncpo):

    def __init__():
        pass

class Papa(ncpo):
    
    def __init__(self):
        pass

class factory:
    
    def __init__(self):
        pass