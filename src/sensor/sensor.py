from src.environment.environment import Environment


class Sensor:
    def __init__(self, environment: Environment):
        self.environment = environment

    def sense(self):
        x, y = self.environment.robot_position
        surroundings = {
            'up': self.environment.is_dirty(x, y - 1) if y > 0 else False,
            'down': self.environment.is_dirty(x, y + 1) if y < self.environment.sizeY - 1 else False,
            'left': self.environment.is_dirty(x - 1, y) if x > 0 else False,
            'right': self.environment.is_dirty(x + 1, y) if x < self.environment.sizeX - 1 else False,
        }
        return surroundings