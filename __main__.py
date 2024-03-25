import pygame
import time
from src.environment.environment import Environment
from src.engine.engine import Engine
from src.sensor.sensor import Sensor
from src.vacuum_cleaner_agent.vacuum_cleaner_agent import VacuumCleanerAgent
from src.engine.strategy.cleaning_strategy import IntelligentCleaningStrategy


def initialize_pygame(environment):
    # Calculate screen dimensions based on environment and cell size
    cell_size = 50  # Adjust cell size as needed
    screen_width = environment.sizeX * cell_size
    screen_height = environment.sizeY * cell_size

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Vacuum Cleaner Agent")
    return screen, cell_size


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)  # Color for dirty cells
GREEN = (0, 255, 0)  # Color for clean cells
YELLOW = (255, 255, 0)  # Color for the robot

def draw_grid(screen, environment, cell_size):
    for y in range(environment.sizeY):
        for x in range(environment.sizeX):
            color = BLACK
            if environment.is_dirty(x, y):
                color = RED
            elif environment.is_clean(x, y):
                color = GREEN
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, WHITE, (x * cell_size, y * cell_size, cell_size, cell_size), 1)

    # Draw robot position
    robot_x, robot_y = environment.robot_position
    pygame.draw.circle(screen, YELLOW, (robot_x * cell_size + cell_size // 2, robot_y * cell_size + cell_size // 2), cell_size // 3)

def update_display(screen):
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def print_environment(environment, robot_position):
    for y in range(environment.sizeY):
        for x in range(environment.sizeX):
            if (x, y) == robot_position:
                print("9", end=" ")
            elif environment.is_dirty(x, y):
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()

def main():
    environment = Environment()
    engine = Engine(environment)
    sensor = Sensor(environment)
    agent = VacuumCleanerAgent(engine, sensor, IntelligentCleaningStrategy())

    while environment.dirty_count > 0:
        # ... your existing cleaning logic
        print_environment(environment, environment.robot_position)
        print()

        sensor_data = sensor.sense()
        print("Sensor Data:", sensor_data)

        direction = agent.cleaning_strategy.move(sensor_data)
        print("Moving", direction)
        engine.move(direction)
        engine.clean_current_position()

        # Update Pygame display
        draw_grid(screen, environment, cell_size)
        update_display(screen)
        time.sleep(1)  # Adjust delay as needed


if __name__ == "__main__":
    environment = Environment()
    screen, cell_size = initialize_pygame(environment)
    main()

