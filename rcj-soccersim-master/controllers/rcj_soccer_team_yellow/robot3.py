from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import math,utils, keyboard

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
                if keyboard.is_pressed('up'):
                    self.right_motor.setVelocity(10)
                    self.left_motor.setVelocity(10)
                if keyboard.is_pressed('down'):
                    self.right_motor.setVelocity(-10)
                    self.left_motor.setVelocity(-10)
                if keyboard.is_pressed('right'):
                    self.right_motor.setVelocity(10)
                    self.left_motor.setVelocity(-10)
                if keyboard.is_pressed('left'):
                    self.right_motor.setVelocity(-10)
                    self.left_motor.setVelocity(10)
                if keyboard.is_pressed(' '):
                    self.right_motor.setVelocity(0)
                    self.left_motor.setVelocity(0)
                