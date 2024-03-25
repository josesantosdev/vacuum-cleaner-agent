from src.environment.environment import Environment


class Engine:
    def __init__(self, environment: Environment):
        self.environment = environment

    def move(self, direction: str):
        x, y = self.environment.robot_position
        if direction == 'up':
            if y > 0:
                self.environment.set_robot_position(x, y - 1)
        elif direction == 'down':
            if y < self.environment.sizeY - 1:
                self.environment.set_robot_position(x, y + 1)
        elif direction == 'left':
            if x > 0:
                self.environment.set_robot_position(x - 1, y)
        elif direction == 'right':
            if x < self.environment.sizeX - 1:
                self.environment.set_robot_position(x + 1, y)

    def clean_current_position(self):
        x, y = self.environment.robot_position
        if self.environment.is_dirty(x, y):
            self.environment.clean(x, y)
