from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase

class option:
    mMo, lMo, rMo = Motor(Port.A), Motor(Port.B), Motor(Port.C)
    cSe = ColorSensor(Port.S1)

    diamater = 56
    track = 128.5
    body = DriveBase(lMo, rMo, diamater, track)
    body.settings(300, None, 150, None)

    startPos = [-1050, 0]
    startPos = [0, 0]
    centerPos = [0, 0]

    containerPos = [[250, 65], [-170, -(+10)], [-250, -65], [170, -(-10)]]
    nextHarborPos, nextFactoryPos = [250, 0], [-250, 0]
    harborPos = {Color.YELLOW: [630, 270], Color.RED: [630, 90], Color.GREEN: [630, -90], Color.BLUE: [630, -270]}
    factoryPos = {Color.YELLOW: [-520, -40], Color.RED: [-520, 40], Color.GREEN: [-850, 40], Color.BLUE: [-850, -40]}