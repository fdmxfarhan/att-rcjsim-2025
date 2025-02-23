from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
from math import *
from utils import *

class MyRobot2(RCJSoccerRobot):
    def run(self):
        initvars(self)
        gkn = False
        cnt = 0
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                readData(self)
                if self.is_ball: # اگر توپ دیده شد
                    # الگوریتم گل به خودی نزدن
                    if self.yr > self.yb: # اگر روبات بالاتر از توپ بود
                        gkn = True
                        cnt=0
                        if self.xr < self.xb: # اگر روبات سمت چپ توپ بود
                            move(self, self.xb-0.2, self.yb) # از کنار توپ رد بشه (از چپ)
                        else:                 # اگر روبات سمت راست توپ بود
                            move(self, self.xb+0.2, self.yb) # از کنار توپ رد بشه (از راست)
                    # الگوریتم مهاجم
                    elif gkn:
                        if self.xb < -0.3:
                            move(self, self.xb-0.1, self.yb-0.2) 
                        elif self.xb < 0.3:
                            move(self, self.xb, self.yb-0.2) 
                        else:
                            move(self, self.xb+0.1, self.yb-0.2) 
                        cnt+=1
                        if cnt > 50:
                            gkn = False
                    elif self.xb > 0: # اگر توپ سمت راست زمین بود
                        move(self, self.xb, self.yb)
                    else:
                        if self.xb < 0.2 and self.xb > -0.2:
                            move(self, 0, self.yb)
                        else:
                            move(self, 0, self.yb-0.1)
                else:
                    moveAndLook(self, 0.4, -0.1, 0, 0.8)