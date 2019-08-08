from particle import Particle


class ParticleManager():
    def __init__(self, nbparticle):
        self.nbparticle = nbparticle
        self.particles = []
    
    def generate_particles(self, start_pos, end_pos):
        vector = (end_pos[0]-start_pos[0],end_pos[1]-start_pos[1])
        for i in range(0,self.nbparticle):
            self.particles.append(Particle(end_pos,vector,[0,9.81],[-120,120],[-180,80],[0,255,0]))    


    def delete_particles(self):
        for p in self.particles:
            if p.out:
                self.particles.remove(p)

    def update(self, xmax, ymax, delta):
        self.delete_particles()
        for p in self.particles:
            p.update(delta,xmax, ymax)
        
    
    def draw(self, screen, pygame):   
        for p in self.particles:     
            pygame.draw.circle(screen, p.col, (int(p.pos[0]), int(p.pos[1])), 2)