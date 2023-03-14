import pygame
import random

# Game settings
WIDTH = 500
HEIGHT = 500
SPEED = 10
CELL_SIZE = 10
FONT_SIZE = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Set up the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Load the font
font = pygame.font.SysFont(None, FONT_SIZE)

# Initialize the snake
snake_pos = [WIDTH/2, HEIGHT/2]
snake_body = [[snake_pos[0], snake_pos[1]],
              [snake_pos[0]-CELL_SIZE, snake_pos[1]],
              [snake_pos[0]-CELL_SIZE*2, snake_pos[1]]]
snake_dir = "RIGHT"

# Initialize the food
food_pos = [random.randrange(0, WIDTH-CELL_SIZE, CELL_SIZE),
            random.randrange(0, HEIGHT-CELL_SIZE, CELL_SIZE)]

# Initialize the score and high score
score = 0
high_score = 0

# Define a function to draw the snake
def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))

# Define a function to move the snake
def move_snake(snake_body, snake_dir):
    if snake_dir == "UP":
        new_head = [snake_body[0][0], snake_body[0][1]-CELL_SIZE]
    elif snake_dir == "DOWN":
        new_head = [snake_body[0][0], snake_body[0][1]+CELL_SIZE]
    elif snake_dir == "LEFT":
        new_head = [snake_body[0][0]-CELL_SIZE, snake_body[0][1]]
    elif snake_dir == "RIGHT":
        new_head = [snake_body[0][0]+CELL_SIZE, snake_body[0][1]]
    snake_body.insert(0, new_head)
    return snake_body

# Define a function to generate a new food
def generate_food():
    return [random.randrange(0, WIDTH-CELL_SIZE, CELL_SIZE),
            random.randrange(0, HEIGHT-CELL_SIZE, CELL_SIZE)]

# Define a function to check if the snake has collided with the food
def check_food_collision(snake_head, food_pos):
    if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
        return True
    return False

# Define a function to check if the snake has collided with itself
def check_self_collision(snake_body):
    if snake_body[0] in snake_body[1:]:
        return True
    return False

# Define a function to check if the snake has collided with the wall
def check_wall_collision(snake_head):
    if snake_head[0] >= WIDTH or snake_head[0] < 0 or snake_head[1] >= HEIGHT or snake_head[1] < 0:
        return True
    return False

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != "DOWN":
                snake_dir = "UP"
            elif event.key == pygame.K_DOWN and snake_dir != "UP":
                snake_dir = "DOWN"
            elif event.key == pygame.K_LEFT and snake_dir != "RIGHT":
                snake_dir = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_dir != "LEFT":
                snake_dir = "RIGHT"

            # Move the snake
    snake_body = move_snake(snake_body, snake_dir)

        # Check if the snake has collided with the food
    if check_food_collision(snake_body[0], food_pos):
        score += 1
        food_pos = generate_food()
    else:
        snake_body.pop()

        # Check if the snake has collided with itself or the wall
    if check_self_collision(snake_body) or check_wall_collision(snake_body[0]):
        if score > high_score:
            high_score = score
        score = 0
        snake_pos = [WIDTH / 2, HEIGHT / 2]
        snake_body = [[snake_pos[0], snake_pos[1]],
                        [snake_pos[0] - CELL_SIZE, snake_pos[1]],
                        [snake_pos[0] - CELL_SIZE * 2, snake_pos[1]]]
        snake_dir = "RIGHT"

    # Update the display
    window.fill(BLACK)
    draw_snake(snake_body)
    pygame.draw.rect(window, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))
    score_text = font.render("Score: " + str(score), True, WHITE)
    high_score_text = font.render("High Score: " + str(high_score), True, WHITE)
    window.blit(score_text, (10, 10))
    window.blit(high_score_text, (WIDTH - high_score_text.get_width() - 10, 10))
    pygame.display.update()

    # Set the game's speed
    clock.tick(SPEED)
