from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import keyboard

class MyRobot3(RCJSoccerRobot):
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if keyboard.is_pressed('up'):
                self.right_motor.setVelocity(10)
                self.left_motor.setVelocity(10)
            if keyboard.is_pressed('down'):
                self.right_motor.setVelocity(-10)
                self.left_motor.setVelocity(-10)
            if keyboard.is_pressed('left'):
                self.right_motor.setVelocity(-10)
                self.left_motor.setVelocity(10)
            if keyboard.is_pressed('right'):
                self.right_motor.setVelocity(10)
                self.left_motor.setVelocity(-10)
            if keyboard.is_pressed('/'):
                self.right_motor.setVelocity(0)
                self.left_motor.setVelocity(0)
            
            