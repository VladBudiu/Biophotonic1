from raytracing import ImagingPath, Lens, Space, ObjectRays, Aperture
import matplotlib.pyplot as plt

def run():
    # Constants for the human eye model
    f_c = 2.3  # focal length of the cornea in cm
    f_l = 6.4  # focal length of the lens in cm
    d_retina = 1.69  # distance to retina from lens system in cm

    # Create the eye model
    eye = ImagingPath()
    eye.append(Lens(f=f_c, label="Cornea"))  # Cornea lens
    eye.append(Space(d=0.5))  # Distance between cornea and lens
    eye.append(Aperture(diameter=2.0, label="Aperture Stop"))  # Add an aperture stop
    eye.append(Lens(f=f_l, label="Lens"))  # Eye lens
    eye.append(Space(d=d_retina))  # Distance from lens to retina
    eye.append(Aperture(diameter=5.0, label="Retina Aperture"))  # Retina aperture for final imaging
    eye.label = "Human Eye Model"

    # Define object rays explicitly
    rays = ObjectRays(
        diameter=2.0,    # Object's diameter in cm
        halfAngle=0.2,   # Spread of rays in radians
        H=7,            # Number of point sources (ray fans)
        T=10,           # Rays per point source
        z=-25.0          # Closer object position (~25 cm)
    )

    # Check for image formation
    try:
        if eye.isImaging:
            image_distance = eye.imagePosition
            print(f"Image formed at {image_distance:.2f} cm for an object at 25 cm.")
        else:
            print("No sharp image formed. Adjust focal lengths further.")
    except Exception as e:
        print(f"Error during imaging check: {e}")

    # Display the model with the defined rays
    try:
        eye.display(raysList=[rays])  # Correct usage of raysList parameter
    except ValueError as e:
        print(f"Error during display: {e}")

    # Visualize the system
    plt.title("Human Eye Model - Object Moved Closer")
    plt.xlabel("Position (cm)")
    plt.ylabel("Height (cm)")
    plt.grid()
    plt.show()