from classes import CentralObject, SmallObject, Simulation
from file_io import load_data_from_interface
from utils import random_color
from numpy import array
from test import draw_points_path


def main():
    # co_diameter, co_mass, *points, resolution = load_data_from_interface()
    co_diameter, co_mass, points, resolution = 200, 50, [[(10, 20), None, None], [(200, 10), None, None], [(40, 50), None, None]], (300, 500  )

    central_object = CentralObject(co_diameter, co_mass)
    small_objects = [SmallObject(*args, random_color()) for args in points]

    simulation = Simulation(central_object, resolution, small_objects)

    simulation.draw().show()




if __name__ == '__main__':
    main()
