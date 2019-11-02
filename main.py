from p5 import *
import numpy as np
from boids import Boid

# Parameters for visualiation
bg = None
width = 800
height = 800

# Create flocks
N = 3 #Total number of boids

#flock = [None] * N
flock = [None for _ in range(N)]
for i in range(N):
    initial_position = np.zeros(2, dtype=np.int32)
    initial_position[0] = np.random.randint(0,width-10) # x coordinate
    initial_position[1] = np.random.randint(0,height-10) # y coordinate
    print(initial_position)
    flock[i] = Boid(width,height,initial_position,100,5,100,100,100,20) 

for idx in flock:
    print(idx.position)

# initial_position[0] = np.random.randint(0,width-10) # x coordinate
# initial_position[1] = np.random.randint(0,height-10) # y coordinate
# a1 = np.array([10,10])
# a2 = np.array([100,100])
# a3 = np.array([400,400])
# 
# print(initial_position)
# flock[0] = Boid(width,height,initial_position,100,5,100,100,100,20) 
# initial_position[0] = np.random.randint(0,width-10) # x coordinate
# initial_position[1] = np.random.randint(0,height-10) # y coordinate
# flock[1] = Boid(width,height,a2,100,5,100,100,100,20)
# initial_position[0] = np.random.randint(0,width-10) # x coordinate
# initial_position[1] = np.random.randint(0,height-10) # y coordinate
# flock[2] = Boid(width,height,a3,100,5,100,100,100,20) 



def setup():
    global bg
    size(width,height) #Background image is 1200x1200
    bg = load_image("images/UW_background.png")

def draw(): #This is the main loop
    global flock
    background(bg)

    for boid in flock:
        boid.show_boid()    

    

run()