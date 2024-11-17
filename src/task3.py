from raytracing import *
import matplotlib.pyplot as plt
import numpy as np

def simulate_projection():
    
    focal_length = 10  
    magnifying_glass_lens = Lens(f=focal_length, diameter=20)
    object_distance = focal_length / 2  # Place object closer than the focal length for virtual image


    object_distance_for_projection = 3 * magnifying_glass_lens.f  
    projection_system = ImagingPath()
    projection_system.append(Space(d=object_distance_for_projection))  # Distance to lens
    projection_system.append(magnifying_glass_lens)
    projection_system.append(Space(d=object_distance_for_projection))  # Space for image formation

    projection_system.display()



if __name__ == "__main__":
    simulate_projection()