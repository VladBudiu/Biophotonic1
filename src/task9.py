from raytracing import ImagingPath, Lens, Space, ObjectRays, Aperture
import matplotlib.pyplot as plt

def run():
    # Constants for the human eye model
    f_c = 2.3  # focal length of the cornea in cm
    f_l_adjusted = 5.0  # Adjusted focal length of the lens in cm
    d_retina = 1.69  # distance to retina from lens system in cm

    # Create the eye model
    eye = ImagingPath()
    eye.append(Lens(f=f_c, label="Cornea"))  # Cornea lens
    eye.append(Space(d=0.5))  # Distance between cornea and lens
    eye.append(Aperture(diameter=2.0, label="Aperture Stop"))  # Add an aperture stop
    eye.append(Lens(f=f_l_adjusted, label="Lens"))  # Adjusted eye lens
    eye.append(Space(d=d_retina))  # Distance from lens to retina
    eye.append(Aperture(diameter=5.0, label="Retina Aperture"))  # Retina aperture for final imaging
    eye.label = "Human Eye Model"

    # Define object rays explicitly
    rays = ObjectRays(
        diameter=2.0,    # Object's diameter in cm
        halfAngle=0.3,   # Spread of rays in radians
        H=10,            # Number of point sources (ray fans)
        T=15,            # Rays per point source
        z=-25.0          # Closer object position (~25 cm)
    )

    # Check for sharp image formation
    try:
        if eye.isImaging:
            print("Lens adjusted to focus on closer object (25 cm).")
        else:
            print("No sharp image formed even after adjustment.")
    except Exception as e:
        print(f"Error during imaging check: {e}")

    # Display the model with the defined rays
    try:
        eye.display(raysList=[rays])  # Correct usage of raysList parameter
    except ValueError as e:
        print(f"Error during display: {e}")

    # Visualize the system
    plt.title("Human Eye Model - Lens Adjustment for Closer Object")
    plt.xlabel("Position (cm)")
    plt.ylabel("Height (cm)")
    plt.grid()
    plt.show()
