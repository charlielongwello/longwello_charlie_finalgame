# This file was created by: charlie longwello
# The Final Game
# my goal for my final project is to make a survival game
# stay alive as long as you can
# beat previous record each time
# replicate flappy bird 


import pygame
import random
import sys

pygame.init()

# Constants
WIDTH = 600
HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (26, 152, 22)
BLUE = (108, 231, 255)


# The Bird
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 15
bird_velocity = 0
gravity = 1

# The Pipes
pipe_width = 50
pipe_gap = 150
pipe_velocity = 5
pipes = [{"x": WIDTH, "height": random.randint(100, HEIGHT - pipe_gap - 100)}]

# Game state
game_active = False
score = 0

# Making the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))


# The font
font = pygame.font.SysFont(None, 36)

# Game Loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_active:
                    # Start or restart the game
                    bird_y = HEIGHT // 2
                    bird_velocity = 0
                    pipes = [{"x": WIDTH, "height": random.randint(100, HEIGHT - pipe_gap - 100)}]
                    score = 0
                    game_active = True
                bird_velocity = -10

    # pipe position
    for pipe in pipes:
        pipe["x"] -= pipe_velocity

    # collision with the bird
    for pipe in pipes:
        if bird_x < pipe["x"] + pipe_width and bird_x + bird_radius > pipe["x"]:
            if bird_y - bird_radius < pipe["height"] or bird_y + bird_radius > pipe["height"] + pipe_gap:
                game_active = False

    # chunk to take away the off-screen pipes
    if pipes and pipes[0]["x"] < -pipe_width:
        pipes.pop(0)
        score += 1

    # adding new pipes onto the screen
    if pipes[-1]["x"] < WIDTH - WIDTH // 2:
        pipes.append({"x": WIDTH, "height": random.randint(100, HEIGHT - pipe_gap - 100)})

    # screen when won
    win.fill(BLUE)

    # The Bird
    pygame.draw.circle(win, BLACK, (bird_x, int(bird_y)), bird_radius)

    # The Pipes
    for pipe in pipes:
        pygame.draw.rect(win, GREEN, (pipe["x"], 0, pipe_width, pipe["height"]))
        pygame.draw.rect(win, GREEN, (pipe["x"], pipe["height"] + pipe_gap, pipe_width, HEIGHT))

    # Score
    score_text = font.render(f"Score: {score}", True, BLACK)
    win.blit(score_text, (10, 10))


    # Display Score
    if not game_active:
        score_text = font.render("You Died : Press SPACE to Play again.", True, BLACK)
        win.blit(score_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))

    # Update the display
    pygame.display.update()

    # Move this block inside the game_active check
    if game_active:
        bird_y += bird_velocity
        bird_velocity += gravity

    # Frame rate
    clock.tick(30)


    



                                    
                                        








