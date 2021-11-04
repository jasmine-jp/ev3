#!/usr/bin/env pybricks-micropython
from libraries import library
from pybricks.tools import wait

class main:
    lib = library()

    def __init__(self):
        self.lib.arm(-270)
        while 1:
            if len(self.lib.ca.opt.containerPos) == 0:
                break
            self.lib.move(self.lib.ca.opt.centerPos)
            self.lib.move(self.lib.ca.opt.containerPos[0])
            self.lib.rotate(self.lib.adjustDeg())
            self.lib.direct(100)
            wait(1000)
            colorVal = self.lib.ca.opt.cSe.color()
            if colorVal in self.lib.ca.opt.factoryPos:
                factory, harbor = self.lib.ca.opt.factoryPos[colorVal], self.lib.ca.opt.harborPos[colorVal]
                self.lib.move(self.lib.ca.opt.nextFactoryPos)
                self.lib.move(factory)
                self.lib.rotate(self.lib.adjustDeg())
                self.lib.arm(0)
                self.lib.direct(150)
                self.lib.arm(-270)
                self.lib.direct(-150)
                self.lib.move(self.lib.ca.opt.nextFactoryPos)
                self.lib.move(self.lib.ca.opt.centerPos)
                self.lib.move(self.lib.ca.opt.nextHarborPos)
                self.lib.move(harbor)
                self.lib.rotate(0)
                self.lib.direct(210)
                self.lib.arm(0)
                self.lib.direct(-210)
                self.lib.arm(-270)
                self.lib.move(self.lib.ca.opt.nextHarborPos)
            else:
                self.lib.ca.opt.containerPos.pop(0)
                continue
        self.lib.move(self.lib.ca.opt.startPos)
        self.lib.rotate(0)

if __name__ == '__main__':
    main()