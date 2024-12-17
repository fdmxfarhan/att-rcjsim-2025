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