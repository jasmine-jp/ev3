from calculation import calc

class library:
    ca = calc()

    def move(self, nextPos: list):
        self.moveVertical([self.ca.currentPos[0], 0])
        self.moveVertical([nextPos[0], 0])
        self.moveVertical([nextPos[0], nextPos[1]])

    def moveVertical(self, nextPos: list):
        self.ca.calcDeg(nextPos)
        self.ca.opt.body.turn(-self.ca.nextDeg)
        self.ca.opt.body.straight(self.ca.distance)

    def rotate(self, deg: int):
        self.ca.inDeg(deg)
        self.ca.opt.body.turn(-self.ca.nextDeg)

    def direct(self, dis: int):
        self.ca.inDis(dis)
        self.ca.opt.body.straight(self.ca.distance)

    def arm(self, deg: int):
        self.ca.opt.mMo.run_target(250, deg)
        self.ca.opt.mMo.hold()