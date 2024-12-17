from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import math,utils

class MyRobot1(RCJSoccerRobot):
    def run(self):
        xb = 0
        yb = 0
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                robot_pos = self.get_gps_coordinates()
                heading = math.degrees(self.get_compass_heading())
                if self.is_new_ball_data():
                    ball_data = self.get_new_ball_data()
                    ball_angle = math.degrees(math.atan2(ball_data['direction'][1], ball_data['direction'][0]))
                    ball_distance = abs(0.0166666666/abs(ball_data['direction'][2])/math.sqrt(1-ball_data['direction'][2]**2))
                    xb = -math.sin(math.radians(ball_angle + heading)) * ball_distance + robot_pos[0]
                    yb =  math.cos(math.radians(ball_angle + heading)) * ball_distance + robot_pos[1]
                    
                utils.move(self, xb, yb)
    
