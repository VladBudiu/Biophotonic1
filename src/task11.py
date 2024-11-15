from raytracing import ImagingPath, Lens, Space, ObjectRays, Aperture
import matplotlib.pyplot as plt

def run():
    # Constants for the myopic human eye model
    f_eye = 1.7  # Myopic eye focal length in cm
    lens_to_retina = 2.0  # Distance from lens to retina in cm (elongated axial length)
    object_distance = 20.0  # Object distance to correct in cm

    # Adjust the glasses' focal length for proper correction
    far_point = 11.33  # Far point of the myopic eye in cm
    # Recalculate glasses focal length for better correction
    f_glasses = -26.155
    #print(f"Adjusted glasses focal length: {f_glasses:.2f} cm")

    # f_glasses = 1 / ((1 / object_distance) - (1 / far_point))
    # print(f"Adjusted glasses focal length: {f_glasses:.10f} cm")

    # Create the corrected eye model
    corrected_eye = ImagingPath()
    corrected_eye.label = "Corrected Myopic Eye Model"

    # Add components step-by-step
    print("Adding Space to Object...")
    corrected_eye.append(Space(d=object_distance, label="Space to Object"))  # Space to object
    print(corrected_eye)

    print("Adding Glasses Lens...")
    corrected_eye.append(Lens(f=f_glasses, label="Glasses"))  # Corrective glasses lens
    print(corrected_eye)

    print("Adding Myopic Eye Lens...")
    corrected_eye.append(Lens(f=f_eye, label="Myopic Eye Lens"))  # Eye's natural lens
    print(corrected_eye)

    print("Adding Space to Retina...")
    corrected_eye.append(Space(d=lens_to_retina, label="Space to Retina"))  # Space to retina
    print(corrected_eye)

    print("Adding Retina...")
    corrected_eye.append(Aperture(diameter=2.0, label="Retina"))  # Retina
    print(corrected_eye)

    # Define rays for visualization
    rays = ObjectRays(
        diameter=2.0,    # Match pupil diameter
        halfAngle=0.01,  # Small angle for parallel rays
        z=0.0
    )

    # Debugging: Explicitly calculate transfer matrix after all elements
    print("Final System Matrix:")
    print(corrected_eye)

    # Check for sharp image formation
    try:
        imageDistance, conjugateMatrix = corrected_eye.forwardConjugate()
    except Exception as e:
        print(f"Error during forward conjugate calculation: {e}")
        return

    opticalLength = corrected_eye.L

    if conjugateMatrix is not None and abs(-imageDistance - opticalLength) < 0.5:
        print("Corrected eye: Object at 20 cm forms a sharp image on the retina.")
        print(f"Image is formed at {imageDistance:.4f} cm, retina is at {opticalLength:.4f} cm.")
    else:
        print("Corrected eye: No sharp image formed on the retina.")
        print(f"Image is formed at {imageDistance:.4f} cm, retina is at {opticalLength:.4f} cm.")

    # Display the corrected eye model
    corrected_eye.display(
        raysList=[rays],
        onlyPrincipalAndAxialRays=False,
        limitObjectToFieldOfView=False,
    )


run()
