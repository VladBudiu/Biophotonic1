import sys
from src import task6, task7, task8, task9, task8_simplified, task9_simplified, task10, task11
from src import task1, task2, task3, task4, task5

if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else None

    if task == "task1":
        task1.simulate_magnifying_glass()
    elif task == "task2":
        task2.show_lens_properties()
    elif task == "task3":
        task3.simulate_projection()
    elif task == "task4":
        task4.simulate_concave_mirror()
    elif task == "task5":
        task5.simulate_lens_camera()
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
        task9_simplified.run()
    elif task == "task10":
        task10.run()
    elif task == "task11":
        task11.run()
    else:
        print("Specify a valid task (e.g., 'task1')")