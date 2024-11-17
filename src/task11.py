from raytracing import ImagingPath, Lens, Space, ObjectRays, Aperture
import matplotlib.pyplot as plt

def run():
    # Constants for the myopic human eye model
    f_eye = 1.7  # Myopic eye focal length in cm
    lens_to_retina = 2.0  # Distance from lens to retina in cm (elongated axial length)
    object_distance = 20.0  # Object distance to correct in cm
    far_point = 11.33  # Far point of the myopic eye in cm
   
    # Adjust the glasses' focal length for proper correction
    f_glasses = -26.155

    # Create the corrected eye model
    corrected_eye = ImagingPath()
    corrected_eye.label = "Corrected Myopic Eye Model"

    # Add components
    print("Adding Space to Object...")
    corrected_eye.append(Space(d=object_distance, label="Space to Object")) 
    print(corrected_eye)

    print("Adding Glasses Lens...")
    corrected_eye.append(Lens(f=f_glasses, label="Glasses")) 
    print(corrected_eye)

    print("Adding Myopic Eye Lens...")
    corrected_eye.append(Lens(f=f_eye, label="Myopic Eye Lens")) 
    print(corrected_eye)

    print("Adding Space to Retina...")
    corrected_eye.append(Space(d=lens_to_retina, label="Space to Retina")) 
    print(corrected_eye)

    print("Adding Retina...")
    corrected_eye.append(Aperture(diameter=2.0, label="Retina"))
    print(corrected_eye)

   
    rays = ObjectRays(
        diameter=10.0,   
        halfAngle=0.01, 
        z=0.0
    )

    print("Final System Matrix:")
    print(corrected_eye)

    try:
        imageDistance, conjugateMatrix = corrected_eye.forwardConjugate()
    except Exception as e:
        print(f"Error during forward conjugate calculation: {e}")
        return

    opticalLength = corrected_eye.L

    if conjugateMatrix is not None and abs(-imageDistance - opticalLength) < 0.5:
        print(f"Image is formed at {imageDistance:.4f} cm, retina is at {opticalLength:.4f} cm.")
    else:
        print(f"Image is formed at {imageDistance:.4f} cm, retina is at {opticalLength:.4f} cm.")

    # Display the corrected eye model
    corrected_eye.display(
        raysList=[rays],
        onlyPrincipalAndAxialRays=False,
        limitObjectToFieldOfView=False,
    )
