import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (200, 0, 0)
BLUE  = (0, 0, 200)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player setup
player_size = 50
player = pygame.Rect(WIDTH//2, HEIGHT-60, player_size, player_size)
player_speed = 7

# Enemy setup
enemy_size = 50
enemy_list = []
enemy_speed = 5

# Font
font = pygame.font.SysFont("Arial", 30)

# Score
score = 0

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH-enemy_size)
        enemy_list.append(pygame.Rect(x_pos, 0, enemy_size, enemy_size))

def draw_enemies(enemy_list):
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, enemy)

def update_enemy_positions(enemy_list, score):
    for idx, enemy in enumerate(enemy_list):
        if enemy.y >= 0 and enemy.y < HEIGHT:
            enemy.y += enemy_speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score

def collision_check(enemy_list, player):
    for enemy in enemy_list:
        if player.colliderect(enemy):
            return True
    return False

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player_size:
        player.x += player_speed

    # Enemy logic
    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Draw enemies
    draw_enemies(enemy_list)

    # Collision check
    if collision_check(enemy_list, player):
        text = font.render("Game Over! Final Score: " + str(score), True, WHITE)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2))
        pygame.display.update()
        pygame.time.wait(2000)
        running = False

    # Draw score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
