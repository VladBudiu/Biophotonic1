import sys
from src import lens_magnifying_glass, lens_properties, lens_projection, concave_lens, lens_camera, task6, task7, task8, task9, task8_simplified, task9_simplified, task10, task11

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
    elif task == "task6":
        task6.run()
    elif task == "task7":
        task7.run()
    elif task == "task8":
        task8.run()
    elif task == "task8_simplified":
        task8_simplified.run()
    elif task == "task9":
        task9.run()
    elif task == "task9_simplified":
        task9.run()
    elif task == "task10":
        task10.run()
    elif task == "task11":
        task11.run()
    else:
        print("Specify a valid task (e.g., 'task1')")