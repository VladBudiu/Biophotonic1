from raytracing import ImagingPath, Lens, Space, Aperture, ObjectRays
import matplotlib.pyplot as plt

def run():
    # Realistic focal length in cm
    f_combined = 1.7      # Combined focal length of cornea and eye lens
    axial_length = 1.7    # Distance between lens and retina (realistic axial length)

    # Create the eye model
    eye = ImagingPath()
    eye.label = "Realistic Human Eye Model with Object at 300 cm"

  
    eye.append(Space(d=300, label="Space Before Lens"))
    eye.append(Lens(f=f_combined, label="Combined Cornea and Lens"))
    eye.append(Space(d=axial_length, label="Vitreous Humor"))
    eye.append(Aperture(diameter=2.0, label="Retina"))

    eye.objectPosition = 300.0  # Object distance in cm
    eye.objectHeight = 2      # Object height in cm

    # Define parallel rays from the object
    rays = ObjectRays(
        diameter=2.0,    
        halfAngle=0.0,   
        T=4,             
        z=0            
    )

 
    imageDistance, conjugateMatrix = eye.forwardConjugate()
    opticalLength = eye.L

    if conjugateMatrix is not None and abs(-imageDistance - opticalLength) < 1e-3:
        print(f"Image is formed at {imageDistance:.4f} cm, retina is at {opticalLength:.4f} cm.")
    else:
        
        print(f"Image is formed at {imageDistance:.4f} cm, retina is at {opticalLength:.4f} cm.")

    # Display the optical model and rays
    eye.display(
        raysList=[rays],
        onlyPrincipalAndAxialRays=False,
        limitObjectToFieldOfView=False
    )
