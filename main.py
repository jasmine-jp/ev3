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
            self.lib.move(self.lib.ca.opt.containerPos[0])
            wait(500)
            colorVal = self.lib.ca.opt.cSe.color()
            if colorVal in self.lib.ca.opt.factoryPos:
                factory, harbor = self.lib.ca.opt.factoryPos[colorVal], self.lib.ca.opt.harborPos[colorVal]
                self.lib.move(factory)
                self.lib.arm(0)
                self.lib.direct(100)
                self.lib.arm(-270)
                self.lib.direct(-100)
                self.lib.move(harbor)
                self.lib.rotate(0)
                self.lib.direct(50)
                self.lib.arm(0)
                self.lib.direct(250)
                self.lib.direct(-300)
                self.lib.arm(-270)
            self.lib.ca.opt.containerPos.pop(0)
        self.lib.move(self.lib.ca.opt.startPos)
        self.lib.rotate(0)
        self.lib.arm(0)

if __name__ == '__main__':
    main()