from raytracing import ImagingPath, Lens, Space, ObjectRays, Aperture
import matplotlib.pyplot as plt

def run():
    # Constants for the simplified human eye model
    axial_length = 1.7  # Distance from lens to retina in cm
    object_distance = 20.0  # Object moved closer

    # Use the thin lens equation to find the correct focal length
    required_f_combined = 1 / (1 / object_distance + 1 / axial_length)

    # Create the eye model with the newly calculated focal length
    eye = ImagingPath()
    eye.label = "Refined Human Eye Model - Adjusted for Closer Object"
    eye.append(Space(object_distance,label="Space before lens"))  
    eye.append(Lens(f=required_f_combined, label="Accommodated Effective Lens"))  
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
    if image_distance is not None:
        print(f"Adjusted focal length: ", required_f_combined)
        print(f"Lens adjusted to focus the image at {image_distance:.2f} cm for an object at {object_distance} cm.")
    else:
        print("Unable to form a sharp image on the retina after lens adjustment.")

    # Display the model with the defined rays
    try:
        eye.display(raysList=[rays], onlyPrincipalAndAxialRays=False)
    except ValueError as e:
        print(f"Error during display: {e}")
