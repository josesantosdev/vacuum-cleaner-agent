import random


class Environment:
    def __init__(self, size_x=5, size_y=5):
        self.sizeX = size_x
        self.sizeY = size_y
        self.grid = [[random.choice([0, 1]) for _ in range(size_x)] for _ in range(size_y)]
        self.dirty_count = sum(row.count(1) for row in self.grid)
        self.robot_position = (random.randint(0, size_x - 1), random.randint(0, size_y - 1))

    def set_robot_position(self, pos_x, pos_y):
        self.robot_position = (pos_x, pos_y)

    def is_clean(self, x, y):
        return self.is_valid_position(x, y) and self.grid[y][x] == 0

    def is_dirty(self, x, y):
        return self.is_valid_position(x, y) and self.grid[y][x] == 1

    def is_obstacle(self, x, y):
        return self.is_valid_position(x, y) and self.grid[y][x] == 2

    def clean(self, x, y):
        if self.is_valid_position(x, y):
            self.grid[y][x] = 0
            self.dirty_count -= 1

    def is_valid_position(self, x, y):
        return 0 <= x < self.sizeX and 0 <= y < self.sizeY

