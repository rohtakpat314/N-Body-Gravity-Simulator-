"""
main.py
--------
Entry point for the N-Body Gravity Simulator.

This script loads celestial bodies from a JSON configuration file,
initializes the physics engine and renderer, and runs the simulation loop.

Stack: Python, NumPy, Pygame, JSON
"""

import pygame
from core.engine import Engine
from render.renderer import Renderer
from examples.solar_system import load_bodies_from_json

def main():
    """
    Main simulation loop for the N-Body Gravity Simulator.

    Steps:
    1. Load celestial bodies from JSON configuration.
    2. Initialize the physics engine.
    3. Initialize the Pygame renderer.
    4. Run the simulation loop, updating physics and rendering each frame.
    5. Handle quitting the application gracefully.
    """

    # Load bodies from configuration file
    bodies = load_bodies_from_json("config/example_config.json")

    # Initialize the physics engine
    engine = Engine(bodies)

    # Initialize the renderer
    renderer = Renderer(width=800, height=600)

    # Simulation timestep (delta time)
    dt = 0.1  # seconds per frame (adjust for stability)

    # Main simulation loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Physics update: compute forces and move bodies
        engine.euler_step(dt)

        # Render current state of all bodies
        renderer.draw(bodies)

    # Quit Pygame gracefully
    pygame.quit()


if __name__ == "__main__":
    main()
