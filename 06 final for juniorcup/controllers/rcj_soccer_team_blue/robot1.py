from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
from math import *
from utils import *

class MyRobot1(RCJSoccerRobot):
    def run(self):
        initvars(self)
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                readData(self)
                if self.is_ball:
                    goalkeeper_x = self.xb
                    if goalkeeper_x > 0.4: goalkeeper_x = 0.4
                    if goalkeeper_x <-0.4: goalkeeper_x =-0.4
                    if self.yb < -0.4 and (self.xb > 0.4 or self.xb < -0.4):
                        move(self, self.xr, self.yb)
                    else:
                        move(self, goalkeeper_x, -0.5)
                else:
                    moveAndLook(self, 0, -0.5, 0, 0.8)