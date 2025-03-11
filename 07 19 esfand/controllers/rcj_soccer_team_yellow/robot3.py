from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
from math import *
from utils import *
import keyboard
import pandas as pd

class MyRobot3(RCJSoccerRobot):
    def run(self):
        vl = 0
        vr = 0
        initvars(self)
        gkn = False
        cnt = 0
        input_df = pd.DataFrame(columns=['xb', 'yb', 'xr', 'yr', 'heading', 'step'])
        output_df = pd.DataFrame(columns=['vl', 'vr'])
        step = 0
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                readData(self)
                if keyboard.is_pressed('w'):
                    vl = 10
                    vr = 10
                    self.right_motor.setVelocity(10)
                    self.left_motor.setVelocity(10)
                if keyboard.is_pressed('s'):
                    vl = -10
                    vr = -10
                    self.right_motor.setVelocity(-10)
                    self.left_motor.setVelocity(-10)
                if keyboard.is_pressed('a'):
                    vl = 10
                    vr = -10
                    self.right_motor.setVelocity(-10)
                    self.left_motor.setVelocity(10)
                if keyboard.is_pressed('d'):
                    vl = -10
                    vr = 10
                    self.right_motor.setVelocity(10)
                    self.left_motor.setVelocity(-10)
                if keyboard.is_pressed('space'):
                    vl = 0
                    vr = 0
                    self.right_motor.setVelocity(0)
                    self.left_motor.setVelocity(0)
                input_df.loc[len(input_df)] = [self.xb, self.yb, self.xr, self.yr, self.heading, step]
                output_df.loc[len(output_df)] = [vl, vr]
                if keyboard.is_pressed('p'):
                    input_df.to_csv('input_data.csv', index=False)
                    output_df.to_csv('output_data.csv', index=False)
                step+=1
