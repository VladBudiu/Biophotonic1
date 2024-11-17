
from raytracing import ImagingPath, Lens, Space, ObjectRays, Aperture
import matplotlib.pyplot as plt

def run():
    # Constants for the human eye model
    f_c = 2.3  # Focal length of the cornea in cm
    axial_length = 1.7  # Distance to retina from the lens system in cm
    object_distance = 20.0

    # Dynamically adjust lens focal length for closer object
    required_f_l = 1 / (1 / object_distance + 1 / axial_length - 1 / f_c)

    # Create the eye model
    eye = ImagingPath()
    eye.label = "Human Eye Model - Adjusted for Closer Object"
    eye.append(Space(d = object_distance)) 
    eye.append(Lens(f=f_c, label="Cornea"))  
    eye.append(Space(d=0.5, label="Aqueous Humor"))  
    eye.append(Lens(f=required_f_l, label="Accommodated Lens"))  # Dynamically adjusted lens
    eye.append(Space(d=axial_length, label="Vitreous Humor"))  
    eye.append(Aperture(diameter=5.0, label="Retina Aperture")) 

    # Define object rays for a closer object
    rays = ObjectRays(
        diameter=2.0,    
        halfAngle=0.3,  
        H=3,             
        T=3,           
        z=0  
    )

  
    image_distance, _ = eye.forwardConjugate()
    print(f"Adjusted focal length: ", required_f_l)
    print(f"Lens adjusted to focus the image at {image_distance:.2f} cm for an object at {object_distance} cm.")

    # Display the model with the defined rays
    try:
        eye.display(raysList=[rays], onlyPrincipalAndAxialRays=False)
    except ValueError as e:
        print(f"Error during display: {e}")
