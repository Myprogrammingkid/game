import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLATFORM_WIDTH = 50
PLATFORM_HEIGHT = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FPS = 60

# Player settings
player_width = 50
player_height = 50
player_color = RED
player_speed = 5
jump_power = -10

# Platform settings
platforms = [
    pygame.Rect(0, SCREEN_HEIGHT - PLATFORM_HEIGHT, SCREEN_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(200, 450, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(400, 350, PLATFORM_WIDTH, PLATFORM_HEIGHT),
]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer")
clock = pygame.time.Clock()

# Player variables
player = pygame.Rect(50, 50, player_width, player_height)
player_y_speed = 0
on_ground = False

def draw_platforms():
    for platform in platforms:
        pygame.draw.rect(screen, BLUE, platform)

def move_player():
    global player_y_speed, on_ground

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # Gravity
    if not on_ground:
        player_y_speed += 0.5

    player.y += player_y_speed

    # Collision with platforms
    for platform in platforms:
        if player.colliderect(platform):
            if player_y_speed > 0:
                player.y = platform.y - player.height
                on_ground = True
                player_y_speed = 0
            elif player_y_speed < 0:
                player.y = platform.y + platform.height
                player_y_speed = 0

def jump():
    global player_y_speed, on_ground
    if on_ground:
        player_y_speed = jump_power
        on_ground = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()

    screen.fill(WHITE)

    move_player()
    draw_platforms()

    pygame.draw.rect(screen, player_color, player)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()