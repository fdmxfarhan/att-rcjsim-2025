from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
from math import *
from utils import *

class MyRobot2(RCJSoccerRobot):
    def run(self):
        self.xt = 0
        self.yt = 0
        self.arrived_to_target = False
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                readData(self)
                if self.xb != 0 and self.yb - 0.7 != 0:
                    m = (self.yb - 0.7) / self.xb
                    b = 0.7
                    self.yt = self.yb-0.13
                    self.xt = (self.yt - b) / m
                if self.is_ball:
                    if self.xb > 0: # mohajem
                        if self.yr > self.yb:
                            if self.xr < self.xb:
                                move(self, self.xb-0.2, self.yb)
                            else:
                                move(self, self.xb+0.2, self.yb)
                        else:
                            if not self.arrived_to_target:
                                move(self, self.xt, self.yt)
                                if sqrt((self.yr - self.yt)**2 + (self.xr - self.xt)**2) < 0.05:
                                    self.arrived_to_target = True
                            else:
                                move(self, self.xb, self.yb)
                                if sqrt((self.yr - self.yb)**2 + (self.xr - self.xb)**2) > 0.2:
                                    self.arrived_to_target = False
                    else: # pass
                        if self.xb < 0.2 and self.xb > -0.2:
                            move(self, 0, self.yb)
                        else:
                            move(self, 0, self.yb-0.2)
                else:
                    moveAndLook(self, 0.4, -0.1, 0, 0.8)

