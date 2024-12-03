from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import keyboard

class MyRobot2(RCJSoccerRobot):
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if keyboard.is_pressed('i'):
                self.right_motor.setVelocity(10)
                self.left_motor.setVelocity(10)
            if keyboard.is_pressed('k'):
                self.right_motor.setVelocity(-10)
                self.left_motor.setVelocity(-10)
            if keyboard.is_pressed('j'):
                self.right_motor.setVelocity(-10)
                self.left_motor.setVelocity(10)
            if keyboard.is_pressed('l'):
                self.right_motor.setVelocity(10)
                self.left_motor.setVelocity(-10)
            if keyboard.is_pressed('o'):
                self.right_motor.setVelocity(0)
                self.left_motor.setVelocity(0)
            
            