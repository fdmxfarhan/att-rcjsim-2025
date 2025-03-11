import math

def move(robot, xp, yp):
    heading = math.degrees(robot.get_compass_heading())  # noqa: F841

    a = math.degrees(math.atan2(robot.xr - xp, yp - robot.yr))
    e = heading - a
    if e > 180: e -= 360
    if e <-180: e += 360
    m = math.sqrt((robot.xr - xp)**2 + (robot.yr - yp)**2)
    if e < -45:
        robot.right_motor.setVelocity(-10)
        robot.left_motor.setVelocity(10)
    elif e > 45:
        robot.right_motor.setVelocity(10)
        robot.left_motor.setVelocity(-10)
    else:
        rv = 10 + e * 0.3
        lv = 10 - e * 0.3
        if rv > 10: rv = 10
        if rv < -10: rv = -10
        if lv > 10: lv = 10
        if lv < -10: lv = -10
        robot.right_motor.setVelocity(rv)
        robot.left_motor.setVelocity(lv)
def moveAndLook(robot, xp, yp, xl, yl):
    heading = math.degrees(robot.get_compass_heading())  # noqa: F841

    a = math.degrees(math.atan2(robot.xr - xp, yp - robot.yr))
    e = heading - a
    if e > 180: e -= 360
    if e <-180: e += 360
    m = math.sqrt((robot.xr - xp)**2 + (robot.yr - yp)**2)
    if m < 0.05:
        a = math.degrees(math.atan2(robot.xr - xl, yl - robot.yr))
        e = heading - a
        if e > 180: e -= 360
        if e <-180: e += 360
        rv =  e * 0.3
        lv = -e * 0.3
        if rv > 10: rv = 10
        if rv < -10: rv = -10
        if lv > 10: lv = 10
        if lv < -10: lv = -10
        robot.right_motor.setVelocity(rv)
        robot.left_motor.setVelocity(lv)
    elif e < -45:
        robot.right_motor.setVelocity(-10)
        robot.left_motor.setVelocity(10)
    elif e > 45:
        robot.right_motor.setVelocity(10)
        robot.left_motor.setVelocity(-10)
    else:
        rv = 10 + e * 0.3
        lv = 10 - e * 0.3
        if rv > 10: rv = 10
        if rv < -10: rv = -10
        if lv > 10: lv = 10
        if lv < -10: lv = -10
        robot.right_motor.setVelocity(rv)
        robot.left_motor.setVelocity(lv)
def readData(robot):
    robot_pos = robot.get_gps_coordinates()
    heading = math.degrees(robot.get_compass_heading())
    robot.xr = robot_pos[0]
    robot.yr = robot_pos[1]
    if robot.robot.getName()[0] == 'B':
        robot.xr *= -1
        robot.yr *= -1
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
    while robot.is_new_team_data():
        team_data = robot.get_new_team_data()['robot_id']
        if not robot.is_ball and team_data['is_ball']:
            robot.xb = team_data['xb']
            robot.yb = team_data['yb']
            robot.is_ball = True
    if robot.xb > 0.58: robot.xb = 0.58
    if robot.xb <-0.58: robot.xb =-0.58
def stop(robot):
    robot.left_motor.setVelocity(0)
    robot.right_motor.setVelocity(0)
def initvars(robot):
    robot.xb = 0
    robot.yb = 0
    robot.is_ball = False
    robot.xr = 0
    robot.yr = 0

## https://github.com/fdmxfarhan/att-rcjsim-2025