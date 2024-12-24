import math
def move(robot, xp, yp):
    robot_pos = robot.get_gps_coordinates()
    heading = math.degrees(robot.get_compass_heading())  # noqa: F841

    a = math.degrees(math.atan2(robot_pos[0] - xp, yp - robot_pos[1]))
    e = heading - a
    m = math.sqrt((robot_pos[0] - xp)**2 + (robot_pos[1] - yp)**2)
    if e < -10:
        robot.right_motor.setVelocity(-10)
        robot.left_motor.setVelocity(10)
    elif e > 10:
        robot.right_motor.setVelocity(10)
        robot.left_motor.setVelocity(-10)
    else:
        robot.right_motor.setVelocity(10)
        robot.left_motor.setVelocity(10)
def readData(robot):
    robot_pos = robot.get_gps_coordinates()
    heading = math.degrees(robot.get_compass_heading())
    robot.xr = robot_pos[0]
    robot.yr = robot_pos[1]
    if robot.is_new_ball_data():
        ball_data = robot.get_new_ball_data()
        ball_angle = math.degrees(math.atan2(
            ball_data['direction'][1], ball_data['direction'][0]))
        ball_distance = abs(
            0.0166666666 / abs(ball_data['direction'][2]) / math.sqrt(1 - ball_data['direction'][2]**2))
        robot.xb = -math.sin(math.radians(ball_angle + heading)
                             ) * ball_distance + robot.xr
        robot.yb = math.cos(math.radians(ball_angle + heading)
                            ) * ball_distance + robot.yr
        robot.is_ball = True
    else:
        robot.is_ball = False
    ###################################### Ersal Data be team
    robot.send_data_to_team({
        'is_ball': robot.is_ball,
        'xb': robot.xb,
        'yb': robot.yb,
        'xr': robot.xr,
        'yr': robot.yr,
        'id': int(robot.robot.getName()[1]) - 1
    })
    ###################################### Daryaft Data az team
    while robot.is_new_team_data():
        team_data = robot.get_new_team_data()['robot_id']
        if not robot.is_ball and team_data['is_ball']:
            robot.xb = team_data['xb']
            robot.yb = team_data['yb']
            robot.is_ball = True
def stop(robot):
    robot.left_motor.setVelocity(0)
    robot.right_motor.setVelocity(0)