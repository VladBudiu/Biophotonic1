
from raytracing import ImagingPath, Lens, Space, ObjectRays, Aperture
import matplotlib.pyplot as plt

def run():
    # Constants for the human eye model
    f_c = 2.3  # Focal length of the cornea in cm
    f_l = 6.4  # Focal length of the lens in cm
    axial_length = 1.7  # Distance to retina from the lens system in cm
    object_distance = 20.0  # Object moved closer to 25 cm
    # Create the eye model
    eye = ImagingPath()
    eye.label = "Human Eye Model - Closer Object"
    eye.append(Space(d = object_distance))  # Distance between cornea and lens
    eye.append(Lens(f=f_c, label="Cornea"))  # Cornea lens
    eye.append(Space(d=0.5, label="Aqueous Humor"))  # Distance between cornea and lens
    eye.append(Lens(f=f_l, label="Crystalline Lens"))  # Eye lens
    eye.append(Space(d=axial_length, label="Vitreous Humor"))  # Distance from lens to retina
    eye.append(Aperture(diameter=5.0, label="Retina Aperture"))  # Retina aperture for final imaging

    # Define object rays for a closer object
  
    rays = ObjectRays(
        diameter=2.0,    # Object's diameter in cm
        halfAngle=0.2,   # Spread of rays in radians
        H=3,             # Number of point sources (ray fans)
        T=3,            # Rays per point source
        z=-0  # Object position
    )

    # Check where the image forms
    image_distance, _ = eye.forwardConjugate()
    print(f"Image is formed at {image_distance:.2f} cm for an object at {object_distance} cm.")

    # Display the model with the defined rays
    try:
        eye.display(raysList=[rays], onlyPrincipalAndAxialRays=False)
    except ValueError as e:
        print(f"Error during display: {e}")
