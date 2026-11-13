# 05_transformations.py — Matrices that move shapes around!
# Draws a little house, then scales, rotates, reflects and shears it.
# Saves the picture as transformations.png next to this file.
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Each COLUMN is one corner (x, y) of the house. The last point repeats the first
# so the outline closes.
house = np.array([
    [0, 2, 2, 1, 0, 0],   # x values
    [0, 0, 2, 3, 2, 0],   # y values
])

angle = math.radians(45)

transforms = {
    "Original": np.eye(2),
    "Scale ×1.5": np.array([[1.5, 0],
                            [0, 1.5]]),
    "Stretch sideways": np.array([[2, 0],
                                  [0, 1]]),
    "Rotate 45°": np.array([[math.cos(angle), -math.sin(angle)],
                            [math.sin(angle),  math.cos(angle)]]),
    "Mirror (flip x)": np.array([[-1, 0],
                                 [0, 1]]),
    "Shear": np.array([[1, 0.8],
                       [0, 1]]),
}

fig, axes = plt.subplots(2, 3, figsize=(12, 8))

for ax, (title, M) in zip(axes.flat, transforms.items()):
    new_house = M @ house                      # <-- the magic line!
    ax.fill(*house, color="lightgray", alpha=0.5, label="before")
    ax.fill(*new_house, color="tab:orange", alpha=0.7, label="after")
    ax.plot(*new_house, color="tab:red")
    ax.set_title(f"{title}\n{np.round(M, 2).tolist()}")
    ax.set_xlim(-4, 5)
    ax.set_ylim(-1, 5)
    ax.set_aspect("equal")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.grid(True, alpha=0.3)

axes.flat[0].legend(loc="upper left")
plt.tight_layout()

out = Path(__file__).with_name("transformations.png")
plt.savefig(out, dpi=120)
print("Saved", out)
plt.show()
