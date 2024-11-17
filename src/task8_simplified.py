
from raytracing import ImagingPath, Lens, Space, ObjectRays, Aperture
import matplotlib.pyplot as plt

def run():
    # Constants for the simplified human eye model
    f_combined = 1.7  # Combined focal length of cornea and lens in cm
    axial_length = 1.7  # Distance from lens to retina in cm
    object_distance = 20.0  # Object distance in cm

    # Create the eye model
    eye = ImagingPath()
    eye.label = "Simplified Human Eye Model - Closer Object"
    eye.append(Space(d = object_distance, label="Space before the lens"))  
    eye.append(Lens(f=f_combined, label="Effective Cornea and Lens"))  
    eye.append(Space(d=axial_length, label="Vitreous Humor"))
    eye.append(Aperture(diameter=5.0, label="Retina Aperture"))

    

    rays = ObjectRays(
        diameter=2.0,    
        halfAngle=0.2,   
        H=3,             
        T=3,            
        z=0 
    )

    # Check where the image forms
    image_distance, _ = eye.forwardConjugate()
    print(f"Image is formed at {image_distance:.2f} cm for an object at {object_distance} cm.")

    # Display the model with the defined rays
    try:
        eye.display(raysList=[rays], onlyPrincipalAndAxialRays=False)
    except ValueError as e:
        print(f"Error during display: {e}")

