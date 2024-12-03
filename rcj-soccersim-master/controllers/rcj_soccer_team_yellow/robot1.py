from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import keyboard

class MyRobot1(RCJSoccerRobot):
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if keyboard.is_pressed('w'):
                self.right_motor.setVelocity(10)
                self.left_motor.setVelocity(10)
            if keyboard.is_pressed('s'):
                self.right_motor.setVelocity(-10)
                self.left_motor.setVelocity(-10)
            if keyboard.is_pressed('a'):
                self.right_motor.setVelocity(-10)
                self.left_motor.setVelocity(10)
            if keyboard.is_pressed('d'):
                self.right_motor.setVelocity(10)
                self.left_motor.setVelocity(-10)
            if keyboard.is_pressed(' '):
                self.right_motor.setVelocity(0)
                self.left_motor.setVelocity(0)
            
            