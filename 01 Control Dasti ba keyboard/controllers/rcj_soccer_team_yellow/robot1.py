from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import math, utils, keyboard

class MyRobot1(RCJSoccerRobot):
    def run(self):
        self.xb = 0
        self.yb = 0
        self.xr = 0
        self.yr = 0
        self.is_ball = True
        step = 1
        while self.robot.step(TIME_STEP) != -1: # تا زمانی که بازی در حال اجرا است:
            if self.is_new_data(): # اگر دیتا موجود بود
                utils.readData(self) # خواندن سنسورها
                if keyboard.is_pressed('w'):
                    self.right_motor.setVelocity(10)
                    self.left_motor.setVelocity(10)
                if keyboard.is_pressed('s'):
                    self.right_motor.setVelocity(-10)
                    self.left_motor.setVelocity(-10)
                if keyboard.is_pressed('d'):
                    self.right_motor.setVelocity(10)
                    self.left_motor.setVelocity(-10)
                if keyboard.is_pressed('a'):
                    self.right_motor.setVelocity(-10)
                    self.left_motor.setVelocity(10)
                if keyboard.is_pressed('e'):
                    self.right_motor.setVelocity(0)
                    self.left_motor.setVelocity(0)
                