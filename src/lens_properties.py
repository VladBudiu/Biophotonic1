from raytracing import *
import matplotlib.pyplot as plt
import numpy as np

def show_lens_properties():
    focal_length = 10
    magnifying_glass_lens = Lens(f=focal_length, diameter=20)
    object_distance = focal_length / 2

    v = 2*object_distance
    magnification = (2*object_distance)/(object_distance)

    print("Lens Properties:")
    print(f"Focal length: {magnifying_glass_lens.f} cm")
    print(f"Diameter: {magnifying_glass_lens.apertureDiameter} cm")
    print(f"Object distance: {object_distance} cm (for achieving magnification of 2)")
    print(f"Image distance: {v} cm (where the virtual image is formed)")
    print(f"Expected Magnification: {magnification}")

if __name__ == "__main__":
    show_lens_properties()