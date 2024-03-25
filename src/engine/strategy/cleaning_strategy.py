from abc import ABC, abstractmethod
import random


class CleaningStrategy(ABC):
    @abstractmethod
    def move(self, sensor_data):
        pass


class SimpleCleaningStrategy(CleaningStrategy):
    def move(self, sensor_data):
        max_dirty_direction = max(sensor_data, key=sensor_data.get)
        return max_dirty_direction

class IntelligentCleaningStrategy(CleaningStrategy):
    def move(self, sensor_data):
        max_dirty_direction = max(sensor_data, key=sensor_data.get)

        # If all surrounding cells are clean, choose a random direction
        if not any(sensor_data.values()):
            return random.choice(['up', 'down', 'left', 'right'])

        # Prioritize cleaning the current cell first if it's dirty
        if sensor_data.get(max_dirty_direction):  # Cell in the chosen direction is dirty
            return max_dirty_direction
        else:  # Cell in the chosen direction is clean, clean the current cell
            return 'clean'
