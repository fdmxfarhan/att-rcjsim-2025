from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import math,utils

class MyRobot3(RCJSoccerRobot):
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                utils.move(self,0.3,0.3)
    
