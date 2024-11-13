from raytracing import *
import matplotlib.pyplot as plt
import numpy as np

def show_lens_properties():
    focal_length = 50  # mm
    lens = Lens(f=focal_length)

    properties = {
        "Focal Length": lens.f,
        "Optical Power": 1 / lens.f  # Diopters, if needed
    }

    for prop, value in properties.items():
        print(f"{prop}: {value}")

if __name__ == "__main__":
    show_lens_properties()
