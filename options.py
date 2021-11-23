from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase

class option:
    mMo, lMo, rMo = Motor(Port.A), Motor(Port.B), Motor(Port.C)
    cSe= ColorSensor(Port.S1)

    diamater = 56
    track = 125
    body = DriveBase(lMo, rMo, diamater, track)
    body.settings(300, None, 150, None)

    startPos = [-1125, 0]
    centerPos = [0, 0]

    containerPos = [[270, 200], [-190, 150], [190, -150], [-270, -200]]
    harborPos = {Color.YELLOW: [590, 290], Color.RED: [590, 95], Color.GREEN: [590, -95], Color.BLUE: [590, -290]}
    factoryPos = {Color.YELLOW: [-530, -100], Color.RED: [-530, 100], Color.GREEN: [-850, 100], Color.BLUE: [-850, -100]}