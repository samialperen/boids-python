from p5 import circle, stroke, fill
import numpy as np
class Boid:
    def __init__(self,width,height,position,range, max_speed, rule1W, rule2W, rule3W 
                ,desired_seperation):
        # Width, height = Screen Output Dimensions
        # x,y = boids positions
        # range = It describes how far boid can detect the others
        # max_speed = Max speed of each individual in the group
        # Rule1 = Cohesion , Rule2 = Seperation, Rule3= Alignment
        # rule1W = Weight for the rule1 (as a percentage), i.e. rule1W = 5 --> 5%
        # desired_seperation = Minimum distance between each boid
        self.width = width
        self.height = height
        self.position = position
        initial_random_velocity = (np.random.rand(2)-0.5) * 10
        self.velocity = initial_random_velocity
        self.range = range
        self.max_speed = max_speed
        self.rule1W = rule1W
        self.rule2W = rule2W 
        self.rule3W = rule3W 
        self.desired_seperation = desired_seperation

    def show_boid(self):
        stroke(255) #white contour colors
        fill(0,0,255) #fill with blue
        circle( (self.position[0],self.position[1]) ,radius=10) 

    def rule1(self,boids): #Cohesion
        center_of_mass = np.zeros(2)
        N = 0 #Total boid number

        for b in boids:
            # self is the boid we are currently looking for. We don't want to take its position
            # into account for center of mass that's why we have the expression right of &
            if (numpy.linalg.norm(b.position - self.position) < self.range) & (b != self):
                center_of_mass += b.position
            N += 1
                
        center_of_mass = center_of_mass // (N-1)
        target_position = (center_of_mass * self.rule1W) // 100
        
        return target_position

    def rule2(self,boids): #Seperation
        c = np.zeros(2)
        for b in boids:
            if ( (numpy.linalg.norm(b.position - self.position) < self.range)    
                    & (numpy.linalg.norm(b.position - self.position) < self.desired_seperation)  
                    & (b != self) ): #end of condition
                c = c - (b.position - self.position) #end of if
        
        return c

    def rule3(self,boids): #Alignment
        perceived_velocity = np.zeros(2)
        N = 0 #Total boid number

        for b in boids:
            if (numpy.linalg.norm(b.position - self.position) < self.range) & (b != self):
                perceived_velocity += b.velocity        
        N += 1

        perceived_velocity = perceived_velocity / (N-1)
        pv = (perceived_velocity * rule3W) / 100

        return pv

    











