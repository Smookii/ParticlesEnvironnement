import pygame,random
from pygame.locals import *
from particlemanager import ParticleManager
from colors import Colors
pygame.init()
xmax = 1000    #width of window
ymax = 600     #height of window



        
class MouseString():
    def __init__(self, startpos, col):
        self.startpos = startpos
        self.col = col



class Main(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((xmax,ymax))

        self.mouse_string = None
        self.clock=pygame.time.Clock()
        self.left_mouse_pressed = False
        self.mouse_pos = None

        self.particle_number = 500
        self.particle_manager = ParticleManager(self.particle_number)

        self.delta = None
        self.exitflag = False

        self.main()


    def main(self):
        while not self.exitflag:        
            self.update()
            self.draw()        
        pygame.quit() 
                
            

    def update(self):
        delta = self.clock.tick(60)
        self.delta = delta/1000
        self.mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP and event.button == 1 and self.left_mouse_pressed:        
                self.left_mouse_pressed = False
                self.particle_manager.generate_particles(self.mouse_string.startpos, self.mouse_pos)
                self.mouse_string = None
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_string = MouseString(self.mouse_pos,Colors.white())
                self.left_mouse_pressed = True
            if event.type == QUIT:
                self.exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.exitflag = True  
        self.particle_manager.update(xmax,ymax,self.delta)
                
    def draw(self):
        self.screen.fill(Colors.black())

        if self.mouse_string is not None:      
            pygame.draw.line(self.screen, self.mouse_string.col, self.mouse_string.startpos,self.mouse_pos,1)
            
        self.particle_manager.draw(self.screen,pygame)
        
        pygame.display.update()

if __name__ == "__main__":
    Main()