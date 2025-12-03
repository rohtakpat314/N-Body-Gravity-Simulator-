# Contains the Engine class, which does the physics calculations 
# Responsible for computing gravitational forces between bodies
# Implements a Euler integrator -- updates veocity and position each timestep

import numpy as np

G = 6.67430e-11  # Gravitational constant

class Engine:
    def __init__(self, bodies):
        self.bodies = bodies

    def compute_forces(self):
        # Reset accelerations
        for body in self.bodies:
            body.acc = np.zeros(2)

        # Compute pairwise gravitational forces
        for i, body1 in enumerate(self.bodies):
            for j, body2 in enumerate(self.bodies):
                if i == j:
                    continue
                r_vec = body2.pos - body1.pos
                r_mag = np.linalg.norm(r_vec)
                if r_mag == 0:
                    continue  # avoid division by zero
                force_mag = G * body1.mass * body2.mass / r_mag**2
                body1.acc += (force_mag / body1.mass) * (r_vec / r_mag)

    def euler_step(self, dt):
        self.compute_forces()
        for body in self.bodies:
            body.vel += body.acc * dt
            body.pos += body.vel * dt
