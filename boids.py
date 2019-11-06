from p5 import circle, stroke, fill
import numpy as np
class Boid(object):
    def __init__(self,width,height,position,horizon, max_speed, rule1W, rule2W, rule3W 
                ,desired_seperation):
        # Width, height = Screen Output Dimensions
        # x,y = boids positions
        # horizon = It describes how far boid can detect the others
        # max_speed = Max speed of each individual in the group
        # Rule1 = Cohesion , Rule2 = Seperation, Rule3= Alignment
        # rule1W = Weight for the rule1 (as a percentage), i.e. rule1W = 5 --> 5%
        # desired_seperation = Minimum distance between each boid
        self.width = width
        self.height = height
        self.position = position
        self.max_speed = max_speed
        initial_random_velocity = (np.random.rand(2)-0.5) * self.max_speed * 2
        self.velocity = initial_random_velocity
        self.horizon = horizon
        self.rule1W = rule1W
        self.rule2W = rule2W 
        self.rule3W = rule3W 
        self.desired_seperation = desired_seperation
        

    def show_boid(self):
        stroke(255) #white contour colors
        fill(0,0,255) #fill with blue
        circle( (self.position[0],self.position[1]) ,radius=10) 

    def update_boid(self):
        # Limiting the speed
        if np.linalg.norm(self.velocity) > self.max_speed:
            self.velocity = (self.velocity/np.linalg.norm(self.velocity)) * self.max_speed 
        # Then update the position
        self.position = np.add(self.position, self.velocity)

    def bound_position(self):
        # If boids reach the edges, it should come back from other side
        if self.position[0] > self.width-1:
            self.position[0] = 0
        elif self.position[1] > self.height-1:
            self.position[1] = 0
        elif self.position[0] < 0:
            self.position[0] = self.width-1
        elif self.position[1] < 0:
            self.position[1] = self.height-1


    def main_boid(self, boids):
        v1 = self.rule1(boids)
        v2 = self.rule2(boids)
        v3 = self.rule3(boids)

        self.bound_position()
        self.show_boid()
        self.velocity += v1 + v2 + v3        
        self.update_boid()

    # This function is used to move flock to a desired position
    # desired_position = Desired target position to move boids
    # step_size = determines how much boids will move towards to desired position
    # in each iteration as a percent --> step_size = 1 means 1% at each step 
    def tend_to_place(self,desired_position,step_size):
        self.velocity = (desired_position - self.position) * (step_size / 100)

    def rule1(self,boids): #Cohesion
        center_of_mass = np.zeros(2)
        N = 0 #Total boid number

        for b in boids:
            # self is the boid we are currently looking for. We don't want to take its position
            # into account for center of mass that's why we have the expression right of &
            if (np.linalg.norm(b.position - self.position) < self.horizon) & (b != self):
                center_of_mass += b.position
            N += 1
                
        center_of_mass = center_of_mass / (N-1)
        target_position = (center_of_mass * self.rule1W) / 100
        
        return target_position

    def rule2(self,boids): #Seperation
        c = np.zeros(2)
        for b in boids:
            if ( (np.linalg.norm(b.position - self.position) < self.horizon)    
                    & (np.linalg.norm(b.position - self.position) < self.desired_seperation)  
                    & (b != self) ): #end of condition
                c -= (b.position - self.position)*(self.rule2W/100) #end of if
        
        return c

    def rule3(self,boids): #Alignment
        perceived_velocity = np.zeros(2)
        N = 0 #Total boid number

        for b in boids:
            if (np.linalg.norm(b.position - self.position) < self.horizon) & (b != self):
                perceived_velocity += b.velocity        
            N += 1

        perceived_velocity = perceived_velocity / (N-1)
        pv = (perceived_velocity * self.rule3W) / 100

        return pv

    











