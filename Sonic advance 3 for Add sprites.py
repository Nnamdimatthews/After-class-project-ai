import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sunset Hill Act 1")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Load sprites
sonic_img = pygame.image.load("sonic.png")
tails_img = pygame.image.load("tails.png")
ring_img = pygame.image.load("ring.png")
chao_img = pygame.image.load("chao.png")
bounce_img = pygame.image.load("bounce.png")
rail_img = pygame.image.load("rail.png")

# Resize
sonic_img = pygame.transform.scale(sonic_img, (40, 40))
tails_img = pygame.transform.scale(tails_img, (30, 30))
ring_img = pygame.transform.scale(ring_img, (30, 30))
chao_img = pygame.transform.scale(chao_img, (30, 30))
bounce_img = pygame.transform.scale(bounce_img, (100, 20))
rail_img = pygame.transform.scale(rail_img, (200, 10))

# Characters
sonic = pygame.Rect(100, 500, 40, 40)
tails = pygame.Rect(60, 500, 30, 30)
velocity = 0
jumping = False

# Game state
rings = 0
chao = 0
emerald = False

# Objects
ring_boxes = [pygame.Rect(random.randint(100, 700), 500, 30, 30) for _ in range(5)]
chao_boxes = [pygame.Rect(random.randint(100, 700), 400, 30, 30) for _ in range(3)]
bounce_pad = pygame.Rect(300, 550, 100, 20)
rail = pygame.Rect(500, 300, 200, 10)

def draw():
    screen.fill((135, 206, 250))  # Sky
    screen.blit(bounce_img, bounce_pad)
    screen.blit(rail_img, rail)

    screen.blit(sonic_img, (sonic.x, sonic.y))
    screen.blit(tails_img, (tails.x, tails.y))

    for box in ring_boxes:
        screen.blit(ring_img, (box.x, box.y))
    for c in chao_boxes:
        screen.blit(chao_img, (c.x, c.y))

    stats = font.render(f"Rings: {rings}  Chao: {chao}/3  Emerald: {'Yes' if emerald else 'No'}", True, (0, 0, 0))
    screen.blit(stats, (20, 20))
    pygame.display.flip()

def check_collisions():
    global rings, chao, emerald, jumping, velocity
    for box in ring_boxes[:]:
        if sonic.colliderect(box):
            rings += 10
            ring_boxes.remove(box)
    for c in chao_boxes[:]:
        if sonic.colliderect(c):
            chao += 1
            chao_boxes.remove(c)
    if chao >= 3 and not emerald:
        emerald = True
    if sonic.colliderect(bounce_pad):
        velocity = -15
        jumping = True
    if sonic.colliderect(rail):
        sonic.x += 5

run = True
while run:
    clock.tick(60)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sonic.x -= 5
    if keys[pygame.K_RIGHT]:
        sonic.x += 5
    if keys[pygame.K_SPACE] and not jumping:
        velocity = -15
        jumping = True

    # Gravity
    sonic.y += velocity
    velocity += 1
    if sonic.y >= 500:
        sonic.y = 500
        velocity = 0
        jumping = False

    # Tails follows Sonic
    tails.x += (sonic.x - tails.x - 40) * 0.1
    tails.y += (sonic.y - tails.y) * 0.1

    check_collisions()

pygame.quit()
