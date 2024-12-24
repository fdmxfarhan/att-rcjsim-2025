from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import math,utils

class MyRobot1(RCJSoccerRobot):
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
                    utils.move(self, self.xb, -0.6)
                else:
                    utils.stop(self)
