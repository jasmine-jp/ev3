from calculation import calc

class library:
    ca = calc()

    def move(self, nextPos: list):
        self.ca.calcDeg(nextPos)
        self.ca.opt.body.turn(-self.ca.nextDeg)
        self.ca.opt.body.straight(self.ca.distance)

    def rotate(self, deg: int):
        self.ca.inDeg(deg)
        self.ca.opt.body.turn(-self.ca.nextDeg)

    def adjustDeg(self) -> int:
        return 90 * self.ca.currentDeg/abs(self.ca.currentDeg)

    def direct(self, dis: int):
        self.ca.inDis(dis)
        self.ca.opt.body.straight(self.ca.distance)

    def arm(self, deg: int):
        self.ca.opt.mMo.run_target(200, deg)
        self.ca.opt.mMo.hold()