from calculation import calc

class library:
    ca = calc()

    def move(self, nextPos: list):
        self.ca.calcDeg(nextPos)
        self.ca.opt.body.turn(-self.ca.nextDeg)
        self.ca.opt.body.straight(self.ca.distance)
        self.moveDiff()

    def rotate(self, deg: int):
        self.ca.inDeg(deg)
        self.ca.opt.body.turn(-self.ca.nextDeg)

    def direct(self, dis: int):
        self.ca.inDis(dis)
        self.ca.opt.body.straight(self.ca.distance)
        self.moveDiff()

    def arm(self, deg: int):
        self.ca.opt.mMo.run_target(200, deg)
        self.ca.opt.mMo.hold()

    def moveDiff(self):
        self.ca.calcDeg([self.ca.currentPos[0], self.ca.currentPos[1]+self.ca.diffDeg()])
        self.ca.opt.body.turn(-self.ca.nextDeg)
        self.ca.opt.body.straight(self.ca.distance)