from collections import deque
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase

class option:
    ev3 = EV3Brick()
    mMo, lMo, rMo = Motor(Port.A), Motor(Port.B), Motor(Port.C)
    cSe = ColorSensor(Port.S1)

    diamater = 56
    track = 128.5
    body = DriveBase(lMo, rMo, diamater, track)

    startPos = []
    centerPos = [0, 0]

    containerPos = deque([[], [], [], []])
    nextHarborPos, nextFactoryPos = [], []
    harborPos = {Color.YELLOW: [], Color.RED: [], Color.GREEN: [], Color.BLUE: []}
    factoryPos = {Color.YELLOW: [], Color.RED: [], Color.GREEN: [], Color.BLUE: []}