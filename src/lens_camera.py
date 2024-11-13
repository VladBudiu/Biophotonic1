from raytracing import *
import matplotlib.pyplot as plt
import numpy as np

def simulate_lens_camera():
    path = ImagingPath()
    path.label = "Aperture acting as Field Stop"
    path.append(Space(d=100))
    path.append(Lens(f=50, diameter=30))
    path.append(Space(d=30))
    path.append(Aperture(diameter=10))
    path.append(Space(d=170))
    
    max_possible_diameter = 30
    limiting_diameter = 10
    utilization_percent = (limiting_diameter/max_possible_diameter) * 100
    
    print(f"Maximum possible diameter: {max_possible_diameter} units")
    print(f"Limiting diameter (aperture): {limiting_diameter} units")
    print(f"System utilization: {utilization_percent:.2f}%")
    
    path.display()
