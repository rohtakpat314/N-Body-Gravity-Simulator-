# Defines a single body class
# Stores mass, position, velocity, acceleration for each body

import numpy as np

class Body:
    def __init__(self, name, mass, pos, vel):
        self.name = name
        self.mass = mass
        self.pos = np.array(pos, dtype=float)  # Position vector [x, y]
        self.vel = np.array(vel, dtype=float)  # Velocity vector [vx, vy]
        self.acc = np.zeros(2, dtype=float)    # Acceleration vector
