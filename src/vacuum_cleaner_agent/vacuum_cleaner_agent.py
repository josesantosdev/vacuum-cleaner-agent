import random
import time

from src.vacuum_cleaner_agent.utils.interface_vacuum_cleaner_agent import InterfaceVacuumCleaner


class VacuumCleanerAgent(InterfaceVacuumCleaner):
    def __init__(self, engine, sensor, cleaning_strategy):
        self.environment = engine.environment
        self.engine = engine
        self.sensor = sensor
        self.cleaning_strategy = cleaning_strategy

    def run(self):
        while self.environment.dirty_count > 0:
            sensor_data = self.sensor.sense()
            action = self.cleaning_strategy.move(sensor_data)
            if action == 'clean':
                self.engine.clean_current_position()
            else:
                self.move(action)
                time.sleep(1)

    def move(self, direction):
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