import copy
import random

import pyglet
from pyglet import shapes
from queue import Queue


width = 1200
height = 1200
delta_time = 0.02


# class Vector2:


class System:
    def __init__(self, planet_list):
        self.planets = planet_list
        self.com = self.calculate_centre_of_mass()

    def calculate_centre_of_mass(self):
        pass

    def get_centre_of_mass(self):
        return self.com


class Kew(list):
    def append(self, item):
        list.append(self, item)
        if len(self) > 1000:
            self[:1] = []


class Planet:
    def __init__(self, position_x, position_y, velocity_x, velocity_y, mass, radius):
        self.x = self.eval_position(position_x, width)
        self.y = self.eval_position(position_y, height)
        self.vx = velocity_x
        self.vy = velocity_y
        self.mass = mass
        self.radius = radius
        self.trail_x = Kew()
        self.trail_y = Kew()

    def draw(self):
        pyglet.shapes.Circle(
            x=self.x, y=self.y, radius=self.radius, color=(250, 25, 30)
        ).draw()

        for i in range(len(self.trail_x)):
            j = i - 1
            if i - 1 < 0:
                j = i
            if not (
                abs(self.trail_x[i] - self.trail_x[j]) > (width / 100)
                or abs(self.trail_y[i] - self.trail_y[j]) > (height / 100)
            ):

                pyglet.shapes.Line(
                    x=self.trail_x[i],
                    y=self.trail_y[i],
                    x2=self.trail_x[j],
                    y2=self.trail_y[j],
                    color=(250, 25, 30),
                ).draw()

    def update_position(self):
        self.trail_x.append(self.x)
        self.trail_y.append(self.y)
        self.x = self.eval_position(self.x + self.vx * delta_time, width)
        self.y = self.eval_position(self.y + self.vy * delta_time, height)
        self.update_velocity()

    def update_velocity(self):
        ax, ay = self.find_acceleration()
        self.vx = self.vx + ax
        self.vy = self.vy + ay

    def find_acceleration(self):
        return random.randrange(-2,2), random.randrange(-2,2)

    @staticmethod
    def eval_position(new_coord, dimension):
        if new_coord > dimension:
            return new_coord - dimension
        if new_coord < 0:
            return new_coord + dimension
        return new_coord


window = pyglet.window.Window(height, width, resizable=True, vsync=True)
planet1 = Planet(50, 50, 90, 5, 10, 10)
planet2 = Planet(450, 450, 30, 10, 15, 20)
planets = [planet1, planet2]

for i in range(300):
    planets.append(Planet(random.randrange(0,width),random.randrange(0,height),random.randrange(-150,150),random.randrange(-150,150),random.randrange(5,12),random.randrange(5,12)))



class Tick:
    def __init__(self):
        self.tick = 0

    def increment_tick(self):
        self.tick = self.tick + 1

    def get_tick(self):
        return self.tick




def update(_):
    window.clear()


    for planet in planets:
        planet.update_position()
        planet.draw()




# run the pyglet application
pyglet.clock.schedule_interval(update, delta_time)

pyglet.app.run()
