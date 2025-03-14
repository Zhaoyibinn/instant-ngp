import json
import os
import numpy as np

def load_transforms(path):
    print(f"path = {path}")
    with open(path) as f:
        frames = json.load(f)
    return frames



transform_path = "transforms.json"
data = load_transforms(transform_path)

rotation = np.array(data["rotation"])
totp = np.array(data["totp"])
sf = data["scale_trans"]



