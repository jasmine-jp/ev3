from pybricks.tools import wait
from options import option
from calculation import calc

class library:
    opt, ca = option(), calc()

    def move(self, nextPos: list):
        self.ca.calcDeg(nextPos)
        self.opt.body.turn(-self.ca.nextDeg)
        self.opt.body.straight(self.ca.distance)

    def rotate(self, deg: int):
        self.ca.inDeg(deg)
        self.opt.body.turn(-self.ca.nextDeg)

    def direct(self, dis: int):
        self.ca.inDis(dis)
        self.opt.body.straight(self.ca.distance)

    def arm(self, deg: int):
        self.opt.mMo.run_target(500, deg)
        self.opt.mMo.hold()