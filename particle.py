import random


class Particle():
    def __init__(self, startpos, initspeed, gravity, scatter, col):
        self.pos = [startpos[0],startpos[1]]
        self.speed = [initspeed[0]*2 + random.uniform(scatter[0],scatter[1]),initspeed[1]*2 + random.uniform(scatter[0],scatter[1])]
        self.gravity = gravity
        self.col = [0,0,255]
        self.out = False

    def update(self,delta, xmax, ymax):
        if self.pos[1] < 0 or self.pos[1] > ymax or self.pos[0] < 0 or self.pos[0] > xmax:
            self.out = True


        ratio_color = (self.pos[1] / ymax) * 255
        if ratio_color < 0:
            ratio_color = 0
        if ratio_color > 255:
            ratio_color = 255
        self.col[0] = ratio_color
        self.col[2] = 255-ratio_color


        self.pos[0] += self.speed[0]*delta
        self.pos[1] += self.speed[1]*delta
        self.speed[0] += self.gravity[0]
        self.speed[1] += self.gravity[1]