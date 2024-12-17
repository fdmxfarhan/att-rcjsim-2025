from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import math,utils

class MyRobot2(RCJSoccerRobot):
    def run(self):
        self.xb = 0
        self.yb = 0
        self.is_ball = True
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                utils.readData(self)
                if self.is_ball:
                    utils.move(self, self.xb, self.yb)
                else:
                    utils.move(self, 0.3, -0.6)
