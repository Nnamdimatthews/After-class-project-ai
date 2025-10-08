import pygame

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event: Color Change")

# Define colors
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Custom event ID
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# Sprite class
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color

    def change_color(self):
        # Cycle through colors
        if self.color == BLUE:
            self.color = GREEN
        elif self.color == GREEN:
            self.color = RED
        elif self.color == RED:
            self.color = YELLOW
        else:
            self.color = BLUE
        self.image.fill(self.color)

# Create two sprites
sprite1 = ColorSprite(200, 200, BLUE)
sprite2 = ColorSprite(400, 200, GREEN)

all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill((30, 30, 30))  # Dark background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Trigger custom event with spacebar
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT))

        # Handle custom event
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()