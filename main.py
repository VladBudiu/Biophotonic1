import sys
from src import lens_magnifying_glass, lens_properties, lens_projection, concave_lens, lens_camera

if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else None

    if task == "task1":
        lens_magnifying_glass.simulate_magnifying_glass()
    elif task == "task2":
        lens_properties.show_lens_properties()
    elif task == "task3":
        lens_projection.simulate_projection()
    elif task == "task4":
        concave_lens.simulate_concave_mirror()
    elif task == "task5":
        lens_camera.simulate_lens_camera()
    else:
        print("Specify a valid task (e.g., 'task1')")
