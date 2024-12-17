import math 
def move(robot,xp,yp):
    robot_pos = robot.get_gps_coordinates()
    heading =math.degrees(robot.get_compass_heading() ) # noqa: F841

    a=math.degrees(math.atan2(robot_pos[0]-xp,yp-robot_pos[1]))
    e=heading-a
    m=math.sqrt((robot_pos[0]-xp)**2+(robot_pos[1]-yp)**2)
    if m<0.05:
        robot.right_motor.setVelocity(0)
        robot.left_motor.setVelocity(0)
    elif e<-10:
        robot.right_motor.setVelocity(-10)
        robot.left_motor.setVelocity(10)
    elif e>10:
        robot.right_motor.setVelocity(10)
        robot.left_motor.setVelocity(-10)
    else:
        robot.right_motor.setVelocity(10)
        robot.left_motor.setVelocity(10)

def readData(robot):
    robot_pos = robot.get_gps_coordinates()
    heading = math.degrees(robot.get_compass_heading())
    if robot.is_new_ball_data():
        ball_data = robot.get_new_ball_data()
        ball_angle = math.degrees(math.atan2(ball_data['direction'][1], ball_data['direction'][0]))
        ball_distance = abs(0.0166666666/abs(ball_data['direction'][2])/math.sqrt(1-ball_data['direction'][2]**2))
        robot.xb = -math.sin(math.radians(ball_angle + heading)) * ball_distance + robot_pos[0]
        robot.yb =  math.cos(math.radians(ball_angle + heading)) * ball_distance + robot_pos[1]
        robot.is_ball = True
    else:
        robot.is_ball = False