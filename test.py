# Import necessary modules from raytracing
from raytracing import *

# Task 1: Create a Simple Lens for a Magnifying Glass (Virtual Image)
def create_magnifying_glass_lens():
    focal_length = 10  # Focal length for desired magnification
    magnifying_glass_lens = Lens(f=focal_length, diameter=20)
    object_distance = focal_length / 2  # Place object closer than the focal length for virtual image

    # Imaging path setup
    system = ImagingPath()
    system.append(Space(d=object_distance))  # Distance from object to lens
    system.append(magnifying_glass_lens)
    system.append(Space(d=2 * focal_length))  # Space after lens to show ray divergence

  #  system.showRays(yMin=-10, yMax=10, rays=5)
    # Display the system, which should now show diverging rays for a virtual image
    system.display()
    return magnifying_glass_lens, object_distance

# Task 2: Show Lens Properties
def show_lens_properties(magnifying_glass_lens, object_distance):
    print("Lens Properties:")
    print(f"Focal length: {magnifying_glass_lens.f} cm")
    print(f"Diameter: {magnifying_glass_lens.apertureDiameter} cm")
    print(f"Expected Magnification: (for object distance {object_distance} cm)")

# Task 3: Projecting an Image onto a Screen (Real Image)
def project_image_on_screen(magnifying_glass_lens):
    object_distance_for_projection = 3 * magnifying_glass_lens.f  # Beyond 2f for a real image
    projection_system = ImagingPath()
    projection_system.append(Space(d=object_distance_for_projection))  # Distance to lens
    projection_system.append(magnifying_glass_lens)
    projection_system.append(Space(d=object_distance_for_projection))  # Space for image formation

    # Display system with real image rays
    projection_system.display()

# Main function to run the tasks
def main():
    print("Task 1: Magnifying Glass with Virtual Image")
    magnifying_glass_lens, object_distance = create_magnifying_glass_lens()
    input("Press Enter to continue...")

    print("\nTask 2: Lens Properties")
    show_lens_properties(magnifying_glass_lens, object_distance)
    
    print("\nTask 3: Projecting Image onto a Screen")
    project_image_on_screen(magnifying_glass_lens)

# Run the main function
if __name__ == "__main__":
    main()
