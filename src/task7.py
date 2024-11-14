from raytracing import ImagingPath, Lens, Space, ObjectRays, Aperture
import matplotlib.pyplot as plt

def run():
    # Constants for the human eye model
    f_cornea = 2.3       # Original cornea focal length
    f_lens = 6.4         # Original eye lens focal length
    axial_length = 1.691  # Original axial length

    # Create the eye model
    eye = ImagingPath()
    eye.label = "Simplified Human Eye Model - Object at 3m"

    # Add components step-by-step
    print("Adding Space to Object...")
    eye.append(Space(d=300.0, label="Space to Object"))  # Space for 3 meters to object
    print(eye)

    print("Adding Cornea...")
    eye.append(Lens(f=f_cornea, label="Cornea"))  # Cornea
    print(eye)

    print("Adding Eye Lens...")
    eye.append(Lens(f=f_lens, label="Eye Lens"))  # Eye Lens
    print(eye)

    print("Adding Vitreous Humor...")
    eye.append(Space(d=axial_length, label="Vitreous Humor"))  # Space to retina
    print(eye)

    print("Adding Retina...")
    eye.append(Aperture(diameter=2.0, label="Retina"))  # Retina
    print(eye)

    # Set the object position and height
    eye.objectPosition = 300.0  # Changed to positive value
    eye.objectHeight = 1.0  # Smaller height for better visualization

    # Define rays with better parameters for visualization
    rays = ObjectRays(
        diameter=2.0,    # Match pupil diameter
        halfAngle=0.01,  # Small angle for parallel rays from distance
        z=0.0            
    )

    # Debugging: Explicitly calculate transfer matrix after all elements
    print("Final System Matrix:")
    print(eye)

    # Check for sharp image formation
    try:
        imageDistance, conjugateMatrix = eye.forwardConjugate()
    except Exception as e:
        print(f"Error during forward conjugate calculation: {e}")
        return

    opticalLength = eye.L

    if conjugateMatrix is not None and abs(-imageDistance - opticalLength) < 1e-3:
        print("Relaxed eye: Object at 3 meters forms a sharp image on the retina.")
        print(f"Image is formed at {imageDistance:.4f} cm, retina is at {opticalLength:.4f} cm.")
    else:
        print("Relaxed eye: No sharp image formed on the retina.")
        print(f"Image is formed at {imageDistance:.4f} cm, retina is at {opticalLength:.4f} cm.")

    # Display the model including the object space
    eye.display(
        raysList=[rays],
        onlyPrincipalAndAxialRays=False,
        limitObjectToFieldOfView=False,
        removeBlocks=True
    )

if __name__ == "__main__":
    run()

