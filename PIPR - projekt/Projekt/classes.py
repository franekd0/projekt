from typing import List, Tuple
from PIL import Image, ImageDraw
from test import draw_points_path


class PositionValueError(Exception):
    pass


class VelocityValueError(Exception):
    pass


class CentralObject:
    def __init__(self, diameter: int, mass: float):
        self._diameter = diameter
        self._mass = mass

    @property
    def diameter(self):
        return self._diameter

    @property
    def mass(self):
        return self._mass


class SmallObject:
    def __init__(self, position: List[int], mass: float, velocity: List[float], color=None):
        self._position = position
        self._mass = mass
        self._velocity = velocity
        self._color = color
        self._previous_positions = [position]
        self._color = color

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position: List[int]):
        self._position = new_position

    @property
    def mass(self):
        return self._mass

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, new_velocity: List[float]):
        if new_velocity[0] < 0 or new_velocity[1] < 0:
            raise VelocityValueError
        self._velocity = new_velocity

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def previous_positions(self):
        return self._previous_positions


class Simulation:
    def __init__(self, central_object: CentralObject, screen_resolution: Tuple[int], small_objects: SmallObject = None, steps: int = 10):
        self._central_object = central_object
        self._small_objects = [] if not small_objects else small_objects
        self._screen_resolution = screen_resolution
        self._steps = steps

    @property
    def steps(self):
        return self._steps
    
    @steps.setter
    def steps(self, new_steps: int):
        self._steps = new_steps

    @property
    def central_object(self):
        return self._central_object

    @property
    def small_objects(self):
        return self._small_objects

    @property
    def screen_resolution(self):
        return self._screen_resolution

    def draw(self):
        co = self._central_object
        points = self._small_objects
        radius = co.diameter//2
        image = Image.new('RGB', self._screen_resolution, 'white')
        draw = ImageDraw.Draw(image)
        draw.circle((self.screen_resolution[0]//2, self.screen_resolution[1]//2), radius, 'grey')  # draw central object
        for point in points:
            draw_points_path(image, point, point.color)
            
        image.show()
