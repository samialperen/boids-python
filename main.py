from p5 import *
import numpy as np
from boids import Boid

# Parameters for visualiation
bg = None
width = 800
height = 800

# Create flocks
N = 40 #Total number of boids
flock = [None for _ in range(N)]
for i in range(N):
    initial_position = np.zeros(2, dtype=np.int32)
    initial_position[0] = np.random.randint(0,width-10) # x coordinate
    initial_position[1] = np.random.randint(0,height-10) # y coordinate
    flock[i] = Boid(width,height,initial_position,100,2,100,100,100,20) 

def setup():
    global bg
    size(width,height) #Background image is width x height
    bg = load_image("images/UW_background.png")

def draw(): #This is the main loop for p5 library
    global flock
    background(bg)

    for boid in flock:
        boid.show_boid()
        boid.main_boid(flock)    
        
run() #This is the main function of p5 library that calls setup once and draw in loop
