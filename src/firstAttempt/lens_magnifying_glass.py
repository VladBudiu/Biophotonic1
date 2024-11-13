from raytracing import *
import matplotlib.pyplot as plt
import numpy as np

def simulate_magnifying_glass():
    focal_length = 50  # Focal length of the lens
    lens_position = 0  # Position of the lens on the optical axis

    # Place the object within the focal length (half of the focal length for 2x magnification)
    object_distance = focal_length / 2  # To achieve 2x magnification

    # Create a convex lens
    lens = Lens(f=focal_length, diameter=25)

    # Define rays with starting positions and angles (within focal length)
    rays = [
        {"y": -5, "theta": 0.1, "color": "blue", "label": "Input Ray 1"},
        {"y": 0, "theta": 0.2, "color": "green", "label": "Input Ray 2"},
        {"y": 5, "theta": -0.1, "color": "red", "label": "Input Ray 3"}
    ]

    # Set up the plot
    fig, ax = plt.subplots()

    # Plot the lens as a vertical line
    ax.plot([lens_position, lens_position], [-15, 15], 'k-', linewidth=2, label="Lens")

    # Trace and plot each ray
    for ray in rays:
        # Calculate the initial position (before lens)
        initial_x = np.linspace(-20, lens_position, 100)
        initial_y = ray["y"] + ray["theta"] * (initial_x - initial_x[0])

        # Create Ray object for input ray
        input_ray = Ray(ray["y"], ray["theta"])

        # Trace ray through the lens
        output_rays = lens.trace(input_ray)  # Assuming this returns a list of Ray objects

        # Debugging: Print the initial ray and output rays
        print(f"Tracing ray {ray['label']} - Initial position: ({ray['y']}, {ray['theta']})")
        for output_ray in output_rays:
            print(f"Output ray: {output_ray.__dict__}")  # Print the properties of the output ray

        # If output_rays is not empty, plot each ray in the list
        final_x = np.linspace(lens_position, 40, 100)
        if output_rays:
            for i, output_ray in enumerate(output_rays):
                if hasattr(output_ray, 'y') and hasattr(output_ray, 'theta'):
                    final_y = output_ray.y + output_ray.theta * (final_x - final_x[0])

                    # Plot the initial and final segments of each ray in the output list
                    ax.plot(initial_x, initial_y, color=ray["color"], linestyle="--", label=ray["label"] if i == 0 else None)
                    ax.plot(final_x, final_y, color=ray["color"])
        else:
            print(f"No output rays generated for {ray['label']}")

    # Set plot labels and titles
    plt.legend()
    plt.title("Ray Tracing for Magnifying Glass with 2x Virtual Image")
    plt.xlabel("Position along Optical Axis (mm)")
    plt.ylabel("Height (mm)")
    plt.xlim(-20, 40)  # Adjusted x-axis limits for visibility on the virtual image side
    plt.ylim(-15, 15)  # Adjusted y-axis limits for visibility
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_magnifying_glass()
