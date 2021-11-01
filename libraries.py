from pybricks.tools import wait
from options import option
from calculation import calc

class library:
    opt, ca = option(), calc()

    def __init__(self):
        self.colorLoop()
    
    def move(self, nextPos: list):
        self.ca.calcDeg(nextPos)
        self.opt.body.turn(-self.ca.nextDeg)
        self.opt.body.straight(self.ca.distance)

    def rotate(self, deg: int):
        self.ca.inDeg(deg)
        self.opt.body.turn(-self.ca.nextDeg)

    def back(self, dis: int):
        self.ca.inDis(dis)
        self.opt.body.straight(-self.ca.distance)
    
    def colorLoop(self):
        while 1:
            self.move(self.opt.containerPos[0])
            self.rotate(0)
            colorVal = self.opt.cSe.color()
            if colorVal in self.opt.harborPos:
                harbor = self.opt.harborPos[colorVal]
                factory = self.opt.factoryPos[colorVal]
            else:
                self.opt.containerPos.popleft()
                continue