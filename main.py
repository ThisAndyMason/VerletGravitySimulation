import pyglet
from pyglet import shapes


width = 500
height = 500
delta_time = 0.2



# class Vector2:


class Planet:
    def __init__(self, position_x, position_y, velocity_x, velocity_y, mass, radius):
        self.x = self.eval_position(position_x, width)
        self.y = self.eval_position(position_y, height)
        self.vx = velocity_x
        self.vy = velocity_y
        self.mass = mass
        self.radius = radius

    def draw(self):
        pyglet.shapes.Circle(
            x=self.x, y=self.y, radius=self.radius, color=(250, 25, 30)
        ).draw()

    def update_position(self):
        self.x = self.eval_position(self.x + self.vx * delta_time, width)
        self.y = self.eval_position(self.y + self.vy * delta_time, height)

    def update_velocity(self):
        pass

    @staticmethod
    def eval_position(new_coord, dimension):
        if new_coord > dimension:
            return new_coord - dimension
        if new_coord < 0:
            return new_coord + dimension
        return new_coord


window = pyglet.window.Window(600, 600, resizable=True, vsync=True)
planet1 = Planet(50, 50, 5, 5, 10, 10)
planet2 = Planet(450, 450, 10, 10, 15, 20)


class Tick:
    def __init__(self):
        self.tick = 0

    def increment_tick(self):
        self.tick = self.tick + 1

    def get_tick(self):
        return self.tick


tick = Tick()


def update(_):
    tick.increment_tick()
    window.clear()

    planet1.update_position()

    planet1.draw()

    if tick.get_tick() > 10:
        planet2.draw()
        planet2.update_position()


# run the pyglet application
pyglet.clock.schedule_interval(update, delta_time)

pyglet.app.run()
