from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import math,utils

class MyRobot3(RCJSoccerRobot):
    def run(self):
        self.xb = 0
        self.yb = 0
        self.xr = 0
        self.yr = 0
        self.is_ball = True
        step = 1
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                utils.readData(self)
                if self.is_ball:
                    if step == 1:
                        utils.move(self, self.xb, self.yb-0.1)
                        if abs(self.xr - self.xb) < 0.01 and abs(self.yr - (self.yb-0.1)) < 0.01:
                            step = 2
                    else: 
                        utils.move(self, self.xb, self.yb)
                        if abs(self.xr - self.xb) > 0.2 and abs(self.yr - self.yb) > 0.2:
                            step = 1
                else:
                    utils.move(self, 0, -0.6)
