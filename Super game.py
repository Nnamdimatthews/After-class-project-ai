import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader – Sunset Edition")

# Colors
SUNSET_ORANGE = (255, 94, 77)  # Warm sunset fill
WHITE = (255, 255, 255)

# 🧑‍🚀 Player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player_sprite.png").convert_alpha()  # Replace with your sprite
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 60))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5

# 👾 Enemy sprite class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy_sprite.png").convert_alpha()  # Replace with your sprite
        self.rect = self.image.get_rect(
            center=(random.randint(40, WIDTH - 40), random.randint(40, HEIGHT // 2))
        )

# Sprite groups
player = Player()
enemies = pygame.sprite.Group()
for _ in range(7):
    enemies.add(Enemy())

all_sprites = pygame.sprite.Group(player, *enemies)

# Score setup
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill(SUNSET_ORANGE)  # 🌅 Fill with sunset color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw sprites
    all_sprites.update()
    all_sprites.draw(screen)

    # Collision detection
    hits = pygame.sprite.spritecollide(player, enemies, dokill=True)
    score += len(hits)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
