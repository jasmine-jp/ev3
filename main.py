#!/usr/bin/env pybricks-micropython
from libraries import library
from options import option
from calculation import calc

class main:
    lib, opt, ca = library(), option(), calc()

    def __init__(self):
        while 1:
            if len(self.opt.containerPos) == 0:
                break
            self.lib.move(self.opt.centerPos)
            self.lib.move(self.opt.containerPos[0])
            self.lib.rotate(self.ca.adjustDeg())
            self.lib.direct(100)
            colorVal = self.opt.cSe.color()
            if colorVal in self.opt.factoryPos:
                factory, harbor = self.opt.factoryPos[colorVal], self.opt.harborPos[colorVal]
                self.lib.move(self.opt.nextFactoryPos)
                self.lib.move(factory)
                self.lib.rotate(self.ca.adjustDeg())
                self.lib.arm(0)
                self.lib.direct(100)
                self.lib.arm(45)
                self.lib.direct(-100)
                self.lib.move(self.opt.nextHarborPos)
                self.lib.move(harbor)
                self.lib.rotate(0)
                self.lib.direct(100)
                self.lib.arm(0)
                self.lib.direct(-100)
                self.lib.arm(45)
            else:
                self.opt.containerPos.popleft()
                continue
        self.lib.move(self.opt.startPos)
        self.lib.rotate(0)

if __name__ == '__main__':
    main()