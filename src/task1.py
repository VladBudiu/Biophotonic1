from raytracing import *
import matplotlib.pyplot as plt
import numpy as np

def simulate_magnifying_glass():
    focal_length = 10
    magnifying_glass_lens = Lens(f=focal_length, diameter=20)
    object_distance = focal_length / 2

    system = ImagingPath()
    system.append(Space(d=object_distance))
    system.append(magnifying_glass_lens)
    system.append(Space(d=2 * focal_length))

    system.display()

if __name__ == "__main__":
    simulate_magnifying_glass()