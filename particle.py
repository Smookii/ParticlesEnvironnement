import random


class Particle():
    def __init__(self, startpos, initspeed, col):
        self.startpos = [startpos[0],startpos[1]]
        self.pos = [startpos[0],startpos[1]]
        scatterx = [-20,20]
        scattery = [-18,8]
        self.start_speed = [initspeed[0]*2 + random.uniform(scatterx[0],scatterx[1]),initspeed[1]*2 + random.uniform(scattery[0],scattery[1])]        
        self.actual_speed = list(self.start_speed)
        self.gravity = [0,180]
        self.col = col
        self.time = [0,0]
        self.bounce_ratio = [1,1.5]
        self.out = False
        
    
    def update_speed(self):      
        for i in range(0,2):
            self.actual_speed[i] = self.start_speed[i] + self.gravity[i]*self.time[i]
        
        
    def rebounce(self, max):        
        for i in range(0,2):
            if self.pos[i] < 0:                
                self.startpos[i] = 0
                self.start_speed[i] = -self.actual_speed[i]/2 * random.uniform(self.bounce_ratio[0],self.bounce_ratio[1])  
                self.time[i] = 0
            if self.pos[i] > max[i]:
                self.startpos[i] = max[i]
                self.start_speed[i] = -self.actual_speed[i]/2 * random.uniform(self.bounce_ratio[0],self.bounce_ratio[1])
                self.time[i] = 0

    def color_by_y(self,ymax):
        ratio_color = (self.pos[1] / ymax) * 255
        if ratio_color < 0:
            ratio_color = 0
        if ratio_color > 255:
            ratio_color = 255
        self.col[0] = ratio_color
        self.col[1] = 255-ratio_color

    def movement(self):
        for i in range(0,2):
            self.pos[i] = self.startpos[i] + self.start_speed[i]*self.time[i]+(self.gravity[i]*self.time[i]*self.time[i]/2)

    def update_time(self, delta):
        for i in range(0,2):
            self.time[i] += delta

    def check_speed(self, ymax):
        for i in range(0,2):
            if self.actual_speed[i] > -3 and self.actual_speed[i] < 3 and self.pos[1] > ymax -5:
                self.out = True

        
    def update(self,delta, xmax, ymax):
        self.update_time(delta)
        self.update_speed()
        self.rebounce(max=[xmax,ymax])
        self.color_by_y(ymax)
        self.movement()
        self.check_speed(ymax)

        