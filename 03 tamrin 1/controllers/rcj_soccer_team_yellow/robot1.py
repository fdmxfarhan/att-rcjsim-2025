from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
from math import *
from utils import *

class MyRobot1(RCJSoccerRobot):
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                readData(self)
                # print(self.xr, self.yr)  # مختصات ربات
                # print(self.xb, self.yb)  # مختصات توپ
                # print(self.is_ball) # وجود توپ
                # move(self, 0, 0) # حرکت به نقطه دلخواه

                move(self, -0.5, self.yb)