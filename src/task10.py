from raytracing import ImagingPath, Lens, Space, ObjectRays, Aperture
import matplotlib.pyplot as plt

def run():
    # Constants for the myopic human eye model
    axial_length = 2.0  # Increased axial length to represent myopia in cm (eyeball is elongated)
    object_distance = 20  # Object distance set to infinity to represent a far object (simulate myopia)
    
    # Step 1: Set the focal length of the eye's natural lens system to simulate myopia
    # Myopic eyes have a focal length that is too short, causing excessive convergence
    myopic_focal_length = 1.7  # Shorter focal length in cm to simulate myopia

    # Create the myopic eye model without corrective glasses
    eye = ImagingPath()
    eye.label = "Myopic Human Eye Model - Elongated Eyeball"
    eye.append(Space(object_distance))  # Space before the lens
    eye.append(Lens(f=myopic_focal_length, label="Effective Cornea and Lens (Myopic)"))  # Myopic cornea and lens
    eye.append(Space(d=axial_length, label="Vitreous Humor"))  # Increased distance from lens to retina
    eye.append(Aperture(diameter=5.0, label="Retina Aperture"))  # Retina aperture for final imaging

    # Define object rays for a distant object (parallel rays to represent distant light sources)
    rays = ObjectRays(
        diameter=2.0,    # Object's diameter in cm
        halfAngle=0.0,   # Parallel rays representing a far object
        H=3,             # Number of point sources (ray fans)
        T=3,             # Rays per point source
        z=0  # Object position
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