from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import math,utils, keyboard

class MyRobot2(RCJSoccerRobot):
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
                if keyboard.is_pressed('u'):
                    self.right_motor.setVelocity(10)
                    self.left_motor.setVelocity(10)
                if keyboard.is_pressed('j'):
                    self.right_motor.setVelocity(-10)
                    self.left_motor.setVelocity(-10)
                if keyboard.is_pressed('k'):
                    self.right_motor.setVelocity(10)
                    self.left_motor.setVelocity(-10)
                if keyboard.is_pressed('h'):
                    self.right_motor.setVelocity(-10)
                    self.left_motor.setVelocity(10)
                if keyboard.is_pressed('i'):
                    self.right_motor.setVelocity(0)
                    self.left_motor.setVelocity(0)
                