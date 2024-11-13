from raytracing import *
import matplotlib.pyplot as plt
import numpy as np

def simulate_projection():
    # Set up parameters for the lens and object
    focal_length = 50       # Focal length of the lens
    object_distance = -75   # Object distance from the lens (negative to place it to the left of the lens)
    image_distance = 1 / (1 / focal_length - 1 / abs(object_distance))  # Calculate image distance using lens formula

    # Create the optical path with spaces and lens
    # The object is to the left of the lens, so space_to_lens has positive distance
    space_to_lens = Space(d=abs(object_distance))
    lens = Lens(f=focal_length, label="Lens")
    space_to_screen = Space(d=image_distance)

    # Combine the elements to form the optical path system
    system = ImagingPath()
    system.append(space_to_lens)
    system.append(lens)
    system.append(space_to_screen)

    # Define multiple points along the object height
    object_heights = np.linspace(-10, 10, 5)  # Points on the object between -10 and 10 units

    # Set up the plot
    plt.figure(figsize=(10, 5))
    
    # Trace rays from each point on the object
    for y0 in object_heights:
        # Each point on the object emits rays with a small range of angles
        angles = np.linspace(-0.05, 0.05, 3)  # Small angular spread for better visibility
        for theta in angles:
            # Create a ray starting from the object position with a slight angle
            ray = Ray(y=y0, theta=theta)
            
            # Trace the ray through the optical system
            ray_trace = system.trace(ray)
            
            # Extract positions and heights for plotting
            x_positions = [point.z for point in ray_trace]
            y_positions = [point.y for point in ray_trace]
            
            # Plot the ray path
            plt.plot(x_positions, y_positions, 'b-')

    # Plot the lens and screen as vertical lines for reference
    plt.axvline(x=0, color='black', linestyle='--', label="Lens")           # Lens at x = 0
    plt.axvline(x=image_distance, color='red', linestyle='--', label="Screen (Image Plane)")

    # Plot the object on the left side of the lens with markers
    plt.plot([-abs(object_distance)] * len(object_heights), object_heights, 'go', label="Object Points")  # Green dots for object

    # Calculate magnification and projected image heights
    magnification = -image_distance / abs(object_distance)
    image_heights = object_heights * magnification  # Scaled object heights for the projected image

    # Plot the projected image on the screen as a vertical line with markers
    plt.plot([image_distance] * len(image_heights), image_heights, 'ro', label="Image Points")  # Red dots for image

    # Labels and display settings
    plt.xlabel("Position along optical axis (z)")
    plt.ylabel("Ray height (y)")
    plt.legend()
    plt.title("Image Projection through a Lens onto a Screen")
    plt.grid()
    plt.xlim(-abs(object_distance) - 10, image_distance + 10)
    plt.ylim(-15, 15)
    plt.show()

if __name__ == "__main__":
    simulate_projection()
