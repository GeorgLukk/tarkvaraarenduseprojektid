import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the game screen
screen_width = 800
screen_height = 600

# Create the game screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set the font and font size
font = pygame.font.Font(None, 30)

# Set the colors for the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Set the initial position of the snake and the size of each segment
snake_position = [400, 300]
snake_size = 10

# Set the initial velocity of the snake
velocity = [0, 0]

# Create a list to hold the segments of the snake
snake_segments = [[snake_position[0], snake_position[1]]]

# Set the initial position of the food
food_position = [random.randrange(1, screen_width / snake_size) * snake_size,
                 random.randrange(1, screen_height / snake_size) * snake_size]

# Set the initial score
score = 0

# Set the initial game speed
game_speed = 10

# Set the initial game state
game_over = False

# Set the extra options for the game
game_options = {"speed_up": False, "slow_down": False, "reverse": False}

# Set the main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and velocity[0] != snake_size:
                velocity[0] = -snake_size
                velocity[1] = 0
            elif event.key == pygame.K_RIGHT and velocity[0] != -snake_size:
                velocity[0] = snake_size
                velocity[1] = 0
            elif event.key == pygame.K_UP and velocity[1] != snake_size:
                velocity[0] = 0
                velocity[1] = -snake_size
            elif event.key == pygame.K_DOWN and velocity[1] != -snake_size:
                velocity[0] = 0
                velocity[1] = snake_size

            # Check if any of the extra options keys were pressed
            elif event.key == pygame.K_SPACE:
                game_options["speed_up"] = not game_options["speed_up"]
            elif event.key == pygame.K_s:
                game_options["slow_down"] = not game_options["slow_down"]
            elif event.key == pygame.K_r:
                game_options["reverse"] = not game_options["reverse"]

    # Update the position of the snake
    snake_position[0] += velocity[0]
    snake_position[1] += velocity[1]

    # Check if the snake collided with the wall
    if snake_position[0] < 0 or snake_position[0] > screen_width - snake_size or \
            snake_position[1] < 0 or snake_position[1] > screen_height - snake_size:
        game_over = True

    # Check if the snake collided with itself
    for segment in snake_segments[1:]:
        if snake_position == segment:
            game_over = True

    # Check if
