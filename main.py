from p5 import *
import numpy as np
from boids import Boid

# Parameters for visualization
bg = None
width = 800
height = 800

# Parameters regarding flocks for description look boids.py
horizon = 100
max_speed = 2
rule1W = 100
rule2W = 100
rule3W = 100
desired_seperation = 20
#desired_position = np.array([100,600]) #You can give static desired positions like this
desired_position = np.zeros(2,dtype=np.int32)
step_size = 10

# Create flocks
N = 40 #Total number of boids
flock = [None for _ in range(N)]
for i in range(N):
    initial_position = np.zeros(2, dtype=np.int32)
    initial_position[0] = np.random.randint(0,width-10) # x coordinate
    initial_position[1] = np.random.randint(0,height-10) # y coordinate
    flock[i] = Boid(width,height,initial_position,horizon,max_speed,rule1W,rule2W,rule3W, \
                    desired_seperation) 

def setup():
    global bg
    size(width,height) #Background image is width x height
    bg = load_image("images/UW_background.png")

def draw(): #This is the main loop for p5 library
    global flock
    background(bg)

    for boid in flock:
        boid.tend_to_place(desired_position,step_size)
        boid.main_boid(flock)    

# When you click the mouse on the output, desired position
# becomes the cursor position
def mouse_pressed():
    print("Desired location: %d,%d " %(mouse_x,mouse_y) )
    desired_position = np.array([mouse_x,mouse_y])

run() #This is the main function of p5 library that calls setup once and draw in loop
