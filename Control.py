import pygame as pg


class MagicWords:
    INPUTSTYPE = ["keyboard", "joystick"]

    BT_ONE = 0
    BT_TWO = 1
    BT_THREE = 2
    BT_FOUR = 3
    BT_L1 = 4
    BT_R1 = 5
    BT_L2 = 6
    BT_R2 = 7
    BT_SELECT = 8
    BT_START = 9
    BT_L3 = 10
    BT_R3 = 11

    LEFT_RIGTH = 0
    UP_DOWN = 1

    LEFT = -1
    RIGTH = 1
    UP = 1
    DOWN = -1

class Input:

    def __init__(self, UP:bool, DOWN:bool, LEFT:bool, RIGTH:bool, ONE:bool, TWO:bool, THREE:bool, FOUR:bool, L1:bool, R1:bool, START:bool, SELECT):
        self.UP:bool = UP
        self.DOWN:bool = DOWN
        self.LEFT:bool = LEFT
        self.RIGTH:bool = RIGTH
        self.ONE:bool = ONE
        self.TWO:bool = TWO
        self.THREE:bool = THREE
        self.FOUR:bool = FOUR
        self.R1:bool = R1
        self.L1:bool = L1
        self.START:bool = START
        self.SELECT:bool = SELECT

class Control:

    control = None

    @staticmethod
    def create():
        if Control.control:
            return Control.control
        Control.control = Control()
        return Control.control

    def __init__(self):
        pg.joystick.init()
        self.joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
        presionado = False
        indice = -1
        while not(presionado):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN or event.type == pg.JOYBUTTONDOWN:
                    presionado = True
                if event.type == pg.JOYBUTTONDOWN:
                    indice = event.joy
        self.index = indice
        self.inputType = MagicWords.INPUTSTYPE[0 if indice == -1 else 1]

    def getInput(self):
        input = None
        mg = MagicWords
        if self.index == -1:
            key = pg.key.get_pressed()
            input = Input(key[pg.K_UP], key[pg.K_DOWN], key[pg.K_LEFT], key[pg.K_RIGHT],
                key[pg.K_d], key[pg.K_w], key[pg.K_a], key[pg.K_s], key[pg.K_q], key[pg.K_e], 
                key[pg.K_KP_ENTER], key[pg.K_SPACE])
        else:
            jk:pg.joystick.JoystickType = self.joysticks[self.index]
            hat = jk.get_hat(0)
            input = Input(hat[mg.UP_DOWN] == mg.UP, hat[mg.UP_DOWN] == mg.DOWN, 
            hat[mg.LEFT_RIGTH] == mg.LEFT, hat[mg.LEFT_RIGTH] == mg.RIGTH,
            jk.get_button(mg.BT_ONE), jk.get_button(mg.BT_TWO), jk.get_button(mg.BT_THREE),
            jk.get_button(mg.BT_FOUR), jk.get_button(mg.BT_L1), jk.get_button(mg.BT_R1),
            jk.get_button(mg.BT_START), jk.get_button(mg.BT_SELECT))
        return input