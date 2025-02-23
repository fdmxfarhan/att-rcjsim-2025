from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
from math import *
from utils import *

class MyRobot2(RCJSoccerRobot):
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                readData(self)
                if self.is_ball:
                    if self.xb > 0:
                        if self.yr > self.yb:
                            if self.xr < self.xb:
                                move(self, self.xb-0.2, self.yb)
                            else:
                                move(self, self.xb+0.2, self.yb)
                        else:
                            move(self, self.xb, self.yb)
                    else:
                        if self.xb < 0.2 and self.xb > -0.2:
                            move(self, 0, self.yb)
                        else:
                            move(self, 0, self.yb-0.2)
                else:
                    moveAndLook(self, 0.4, -0.1, 0, 0.8)

