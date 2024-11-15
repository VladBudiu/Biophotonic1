from raytracing import ImagingPath, Lens, Space, Aperture, ObjectRays
import matplotlib.pyplot as plt

def run():
    # Realistic focal length in cm
    f_combined = 1.7      # Combined focal length of cornea and eye lens
    axial_length = 1.7    # Distance between lens and retina (realistic axial length)

    # Create the eye model
    eye = ImagingPath()
    eye.label = "Realistic Human Eye Model with Object at 300 cm"

    # Add space before the cornea
    eye.append(Space(d=300, label="Space Before Lens"))

    # Add combined cornea and lens
    eye.append(Lens(f=f_combined, label="Combined Cornea and Lens"))

    # Add space for vitreous humor
    eye.append(Space(d=axial_length, label="Vitreous Humor"))

    # Add retina as aperture
    eye.append(Aperture(diameter=2.0, label="Retina"))

    # Set object parameters
    eye.objectPosition = 300.0  # Object distance in cm
    eye.objectHeight = 2      # Object height in cm

    # Define parallel rays from the object
    rays = ObjectRays(
        diameter=2.0,    # Simulate rays entering the eye across the pupil
        halfAngle=0.0,   # Parallel rays at the object
        T=4,             # Number of rays
        z=0              # Start rays at the object position
    )

    # Check for sharp image formation
    imageDistance, conjugateMatrix = eye.forwardConjugate()
    opticalLength = eye.L

    if conjugateMatrix is not None and abs(-imageDistance - opticalLength) < 1e-3:
        print("Eye: Object at 300 cm forms a sharp image on the retina.")
        print(f"Image is formed at {imageDistance:.4f} cm, retina is at {opticalLength:.4f} cm.")
    else:
        print("Eye: No sharp image formed on the retina.")
        print(f"Image is formed at {imageDistance:.4f} cm, retina is at {opticalLength:.4f} cm.")

    # Display the optical model and rays
    eye.display(
        raysList=[rays],
        onlyPrincipalAndAxialRays=False,
        limitObjectToFieldOfView=False
    )
