import pygame
import random

pygame.init()

# Window
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Flappy Bird")

clock = pygame.time.Clock()

# Colors
SKY = (135, 206, 235)
GREEN = (50, 180, 70)
YELLOW = (255, 220, 0)
BLACK = (0, 0, 0)

# Bird
bird_x = 100
bird_y = 300
bird_size = 30

velocity = 0
gravity = 0.5
jump_strength = -8

# Pipes
pipe_width = 70
pipe_gap = 180
pipe_speed = 4

pipe_x = WIDTH

gap_y = random.randint(150, 400)

running = True
game_over = False

while running:

    # ------------------------------
    # Handle events
    # ------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and not game_over:
                velocity = jump_strength

            if event.key == pygame.K_SPACE and game_over:
                bird_y = 300
                velocity = 0
                pipe_x = WIDTH
                gap_y = random.randint(150, 400)
                game_over = False

    if not game_over:

        # ------------------------------
        # Bird physics
        # ------------------------------

        velocity += gravity
        bird_y += velocity

        # ------------------------------
        # Move pipe
        # ------------------------------

        pipe_x -= pipe_speed

        if pipe_x < -pipe_width:
            pipe_x = WIDTH
            gap_y = random.randint(150, 400)

        # ------------------------------
        # Create rectangles
        # ------------------------------

        bird = pygame.Rect(
            bird_x,
            bird_y,
            bird_size,
            bird_size
        )

        top_pipe = pygame.Rect(
            pipe_x,
            0,
            pipe_width,
            gap_y - pipe_gap // 2
        )

        bottom_pipe = pygame.Rect(
            pipe_x,
            gap_y + pipe_gap // 2,
            pipe_width,
            HEIGHT
        )

        # ------------------------------
        # Collision detection
        # ------------------------------

        if bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe):
            game_over = True

        if bird.top <= 0 or bird.bottom >= HEIGHT:
            game_over = True

    # ------------------------------
    # Draw everything
    # ------------------------------

    screen.fill(SKY)

    pygame.draw.rect(
        screen,
        YELLOW,
        (bird_x, bird_y, bird_size, bird_size)
    )

    pygame.draw.rect(
        screen,
        GREEN,
        (pipe_x, 0, pipe_width, gap_y - pipe_gap // 2)
    )

    pygame.draw.rect(
        screen,
        GREEN,
        (
            pipe_x,
            gap_y + pipe_gap // 2,
            pipe_width,
            HEIGHT
        )
    )

    # ------------------------------
    # Game over message
    # ------------------------------

    if game_over:

        font = pygame.font.Font(None, 50)

        text = font.render(
            "GAME OVER - Press SPACE",
            True,
            BLACK
        )

        screen.blit(
            text,
            (WIDTH // 2 - text.get_width() // 2, 250)
        )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()