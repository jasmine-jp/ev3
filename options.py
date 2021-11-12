from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color, Direction
from pybricks.robotics import DriveBase

class option:
    d = Direction.COUNTERCLOCKWISE
    mMo, lMo, rMo = Motor(Port.A, d), Motor(Port.B, d), Motor(Port.C, d)
    cSe = ColorSensor(Port.S1)

    diamater = 56
    track = 125
    body = DriveBase(lMo, rMo, diamater, track)
    body.settings(300, None, 150, None)

    startPos = [-1125, 0]
    centerPos = [0, 0]

    containerPos = [[270, 170], [-190, 130], [-270, -170], [190, -130]]
    harborPos = {Color.YELLOW: [590, 290], Color.RED: [590, 100], Color.GREEN: [590, -100], Color.BLUE: [590, -290]}
    factoryPos = {Color.YELLOW: [-530, -100], Color.RED: [-530, 100], Color.GREEN: [-850, 100], Color.BLUE: [-850, -100]}