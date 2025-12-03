# Loads bodies from JSON config
# Prints initial conditions for debugging

import json
from core.body import Body

def load_bodies_from_json(file_path):
    bodies = []
    with open(file_path) as f:
        data = json.load(f)
        for item in data:
            bodies.append(Body(item["name"], item["mass"], item["pos"], item["vel"]))
    return bodies

if __name__ == "__main__":
    bodies = load_bodies_from_json("../config/example_config.json")
    for body in bodies:
        print(body.name, body.mass, body.pos, body.vel)
