import math
from options import option

class calc:
    opt = option()
    currentPos, nextDeg, currentDeg, distance = opt.startPos, 0, 0, 0

    def calcDeg(self, nextPos: list):
        run, rise = nextPos[0]-self.currentPos[0], nextPos[1]-self.currentPos[1]
        slope = math.degrees(math.atan2(rise, run))

        hoge = slope - self.currentDeg

        if abs(hoge) <= 180:
            self.nextDeg = hoge
        else:
            self.nextDeg = hoge - 360*hoge/abs(hoge)
        self.currentDeg = slope
        self.currentPos = nextPos

        self.distance = (run**2 + rise**2)**0.5

    def inDeg(self, deg: int):
        slope = deg

        hoge = slope - self.currentDeg

        if abs(hoge) <= 180:
            self.nextDeg = hoge
        else:
            self.nextDeg = hoge - 360*hoge/abs(hoge)
        self.currentDeg = slope

    def inDis(self, dis: int):
        divideDis = [dis*math.cos(math.radians(self.currentDeg)), dis*math.sin(math.radians(self.currentDeg))]
        run, rise = self.currentPos[0]+divideDis[0], self.currentPos[1]+divideDis[1]
        self.currentPos = [run, rise]

        self.distance = dis