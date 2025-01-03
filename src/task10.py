from raytracing import ImagingPath, Lens, Space, ObjectRays, Aperture
import matplotlib.pyplot as plt

def run():
    # Constants for the myopic human eye model
    axial_length = 2.0  # Increased axial length to represent myopia in cm (eyeball is elongated)
    object_distance = 20  # Object distance set to infinity to represent a far object (simulate myopia)
    
    # Step 1: Set the focal length of the eye's natural lens system to simulate myopia
    myopic_focal_length = 1.7 

    # Create the myopic eye model without corrective glasses
    eye = ImagingPath()
    eye.label = "Myopic Human Eye Model - Elongated Eyeball"
    eye.append(Space(object_distance,label="Space before the lens")) 
    eye.append(Lens(f=myopic_focal_length, label="Effective Cornea and Lens (Myopic)"))  
    eye.append(Space(d=axial_length, label="Vitreous Humor"))  
    eye.append(Aperture(diameter=5.0, label="Retina Aperture")) 

    # Define object rays for a distant object (parallel rays to represent distant light sources)
    rays = ObjectRays(
        diameter=10.0,   
        halfAngle=0.0,  
        H=3,             
        T=3,          
        z=0  
    )

    # Check where the image forms
    image_distance, _ = eye.forwardConjugate()
    if image_distance is not None:
        print(f"Myopic eye focal length: {myopic_focal_length:.2f} cm")
        print(f"Image formed at {image_distance:.2f} cm for an object at a far distance.")
    else:
        print("Unable to form a sharp image on the retina.")

    # Display the myopic eye model
    try:
        eye.display(raysList=[rays], onlyPrincipalAndAxialRays=False)
    except ValueError as e:
        print(f"Error during display: {e}")