"""
main.py
N-Body Simulator 
Features:
- Multiple orbiting bodies with mutual gravity
- Trails showing orbital paths (different colors)
- Mass labels on bodies
- Pause/Play (SPACEBAR)
- Reset (R)
- Adjustable speed (UP/DOWN arrows)
- Smooth 60 FPS rendering
"""

import pygame
import numpy as np
from core.body import Body  # ensure your Body class is in core/body.py

# ---------- Pygame setup ----------
pygame.init()  # Initialize all pygame modules, including fonts
WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-Body Simulator")
CLOCK = pygame.time.Clock()

# ---------- Pygame setup ----------
WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-Body Simulator")
CLOCK = pygame.time.Clock()

# ---------- Simulation constants ----------
G = 1.0
dt = 0.05
MAX_TRAIL = 200

# ---------- Body colors ----------
TRAIL_COLORS = [
    (0, 255, 0),     # green
    (0, 200, 255),   # cyan
    (255, 100, 0),   # orange
    (255, 0, 255),   # magenta
    (255, 255, 0)    # yellow (Sun)
]

# ---------- Setup bodies ----------
def setup_bodies():
    central = Body("Sun", mass=1000, pos=[WIDTH//2, HEIGHT//2], vel=[0,0])
    central.trail = []
    
    orbit_data = [
        {"name":"Planet1", "mass":5, "pos":[WIDTH//2 + 100, HEIGHT//2], "vel":[0, 2]},
        {"name":"Planet2", "mass":8, "pos":[WIDTH//2, HEIGHT//2 + 150], "vel":[-1.5, 0]},
        {"name":"Planet3", "mass":3, "pos":[WIDTH//2 - 200, HEIGHT//2], "vel":[0, -1.8]},
    ]

    bodies = [central]
    for data in orbit_data:
        planet = Body(data["name"], data["mass"], data["pos"], data["vel"])
        planet.trail = []
        bodies.append(planet)
    return bodies

# ---------- Physics update ----------
def update_bodies(bodies, speed_multiplier=1.0):
    for body in bodies:
        body.acc = np.zeros_like(body.pos)

    # Mutual gravity
    for i, body1 in enumerate(bodies):
        for j, body2 in enumerate(bodies):
            if i != j:
                r_vec = body2.pos - body1.pos
                dist = np.linalg.norm(r_vec)
                if dist == 0:
                    continue
                body1.acc += G * body2.mass / dist**2 * (r_vec / dist)

    # Update position/velocity
    for body in bodies:
        body.vel += body.acc * dt * speed_multiplier
        body.pos += body.vel * dt * speed_multiplier

        # Update trail
        body.trail.append(body.pos.copy())
        if len(body.trail) > MAX_TRAIL:
            body.trail.pop(0)

# ---------- Drawing ----------
def draw_instructions():
    font = pygame.font.SysFont("Arial", 20)
    instructions = "SPACE: Pause/Play   R: Reset   UP/DOWN: Speed"
    text_surface = font.render(instructions, True, (200, 200, 200))
    WIN.blit(text_surface, (10, 10))

def draw_gui_info(speed_multiplier, fps, num_bodies):
    font = pygame.font.SysFont("Arial", 20)
    info = f"Speed: x{speed_multiplier:.2f}   FPS: {fps:.0f}   Bodies: {num_bodies}"
    text_surface = font.render(info, True, (180, 180, 255))
    WIN.blit(text_surface, (10, 40))

def draw_bodies(bodies):
    WIN.fill((0,0,0))

    for idx, body in enumerate(bodies):
        color = TRAIL_COLORS[idx % len(TRAIL_COLORS)]
        
        # Draw trail
        if len(body.trail) > 1:
            pygame.draw.lines(WIN, color, False, [pos.astype(int) for pos in body.trail], 2)

        # Draw body
        size = 10 if body.name=="Sun" else 6
        pygame.draw.circle(WIN, color, body.pos.astype(int), size)

        # Draw mass label
        font = pygame.font.SysFont("Arial", 16)
        mass_text = font.render(f"{body.mass}", True, (255, 255, 255))
        WIN.blit(mass_text, (body.pos[0] + 8, body.pos[1] - 8))

    # Draw instructions
    draw_instructions()

# ---------- Main loop ----------
def main():
    bodies = setup_bodies()
    running = True
    paused = False
    speed_multiplier = 1.0

    while running:
        fps = CLOCK.get_fps()
        CLOCK.tick(60)  # 60 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    bodies = setup_bodies()
                elif event.key == pygame.K_UP:
                    speed_multiplier *= 1.5
                elif event.key == pygame.K_DOWN:
                    speed_multiplier /= 1.5

        if not paused:
            update_bodies(bodies, speed_multiplier)

        draw_bodies(bodies)
        draw_gui_info(speed_multiplier, fps, len(bodies))

        # Draw PAUSED text
        if paused:
            font = pygame.font.SysFont("Arial", 40)
            text = font.render("PAUSED", True, (255, 0, 0))
            WIN.blit(text, (WIDTH - 150, 20))
            pygame.display.flip()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
