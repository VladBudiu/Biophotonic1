from raytracing import *
import matplotlib.pyplot as plt
import numpy as np

class ConcaveMirror:
    def __init__(self, focal_length, diameter):
       self.f=focal_length
       self.diameter = diameter

def simulate_concave_mirror():
    concave_mirror = ConcaveMirror(10,20)
    mirror = Lens(concave_mirror.f, concave_mirror.diameter)
    object_distance = 30

    projection_system = ImagingPath()
    projection_system.append(Space(d=object_distance))
    projection_system.append(mirror)
    projection_system.append(Space(d=object_distance))

    projection_system.display()

if __name__ == "__main__":
    simulate_concave_mirror()
