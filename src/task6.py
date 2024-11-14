from raytracing import ImagingPath, Lens, Space, Aperture, ObjectRays
import matplotlib.pyplot as plt

def run():
    # Focal lengths in cm
    f_cornea = 2.3       # Focal length of the cornea
    f_lens = 6.4         # Focal length of the eye lens
    axial_length = 1.691  # Axial length equal to the effective focal length

    # Create the eye model
    eye = ImagingPath()
    eye.label = "Simplified Human Eye Model"

    # Cornea and eye lens combined
    eye.append(Lens(f=f_cornea, label="Cornea"))
    eye.append(Lens(f=f_lens, label="Eye Lens"))

    # Space between lens and retina
    eye.append(Space(d=axial_length, label="Vitreous Humor"))

    # Retina
    eye.append(Aperture(diameter=2.0, label="Retina"))

    # Set the object at infinity
    eye.objectPosition = float('inf')
    eye.objectHeight = 2.0  # Set a finite object height

    # Define rays coming from infinity (parallel rays)
    rays = ObjectRays(
        diameter=2.0,    # Simulate rays entering the eye across the pupil
        halfAngle=0.0,   # Parallel rays
        z=0.0            # Start at z=0.0
    )

    # Check for sharp image formation
    imageDistance, conjugateMatrix = eye.forwardConjugate()
    opticalLength = eye.L

    if conjugateMatrix is not None and abs(-imageDistance - opticalLength) < 1e-3:
        print("Relaxed eye: Object at infinity forms a sharp image on the retina.")
        print(f"Image is formed at {imageDistance:.4f} cm, retina is at {opticalLength:.4f} cm.")
    else:
        print("Relaxed eye: No sharp image formed on the retina.")
        print(f"Image is formed at {imageDistance:.4f} cm, retina is at {opticalLength:.4f} cm.")

    # Display the model with the defined rays
    eye.display(
        raysList=[rays],
        onlyPrincipalAndAxialRays=False,
        limitObjectToFieldOfView=False
    )