import pygame
import sys

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Огонь и Вода")

clock = pygame.time.Clock()
fps = 60

try:
    fire_image = pygame.image.load('assets/fire_character.png')
    water_image = pygame.image.load('assets/water_character.png')
except pygame.error as e:
    print(f'невозможно загрузить изображение: {e}')
    sys.exit(1)

fire_pos = [100, 550]
water_pos = [150, 550]

# Скорость движения персонажей
speed = 3

# Параметры прыжка
jump_speed = 5
gravity = 0.1

fire_jumping = False
fire_y_velocity = 0

water_jumping = False
water_y_velocity = 0

# Определение платформ (координаты x, y, ширина, высота)
platforms = [
    pygame.Rect((150, 500), (700, 10)),
    pygame.Rect((-150, 350), (750, 10))
]

platform_color = (0, 128, 0)

def chek_platform_collisions(rect, vel):
    collided = False
    for platform in platforms:
        if rect.colliderect(platform):
            if vel[1] > 0:
                rect.bottom = platform.top
                vel[1] = 0
                collided = True
            elif vel[1] < 0:
                rect.top = platform.bottom
                vel[1] = 0
                collided = True
            elif vel[0] > 0:
                rect.right = platform.left
                vel[0] = 0
                collided = True
            elif vel[0] < 0:
                rect.left = platform.right
                vel[0] = 0
                collided = True
    return collided

# Основной цикл
running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        


    # Обработка движения персонажа Огонь (стрелки)
keys = pygame.key.get_pressed()
fire_dx = 0
fire_dy = fire_y_velocity
if keys[pygame.K_LEFT] and fire_pos[0] > 0:
    fire_dx -= speed
if keys[pygame.K_RIGHT] and fire_pos[0] < size[0] - fire_image.get_width():
    fire_dx += speed
if keys[pygame.K_UP] and not fire_jumping:
    fire_jumping = True
    fire_dy = -jump_speed

if fire_jumping:
    fire_y_velocity += gravity
    fire_pos += fire_y_velocity

fire_rect = pygame.Rect(fire_pos[0] + fire_dx, fire_pos[1] + fire_dy, fire_image.get_width(), fire_image.get_height())

fire_jumping = chek_platform_collisions(fire_rect, [fire_dx, fire_dy])

fire_pos[0] = fire_rect.x
fire_pos[1] = fire_rect.y

if fire_pos[1] >= size[1] - fire_image.get_height():
    fire_pos[1] = size[1] - fire_image.get_height()
    fire_jumping = False
    fire_y_velocity = 0
            

# Обработка движения персонажа Вода (WASD)
    water_dx = 0
    water_dy = water_y_velocity
    if keys[pygame.K_a] and water_pos[0] > 0:
        water_dx -= speed
    if keys[pygame.K_d] and water_pos[0] < size[0] - water_image.get_width():
        water_dx += speed
    if keys[pygame.K_w] and not water_jumping:
        water_jumping = True
        water_dy = -jump_speed

    
    if water_jumping:
        water_y_velocity += gravity
        water_dy += water_y_velocity

    water_rect = pygame.Rect(water_pos[0] + water_dx, water_pos(1) + water_dy, water_image.get_width(), water_image.get_height())

    water_jumping = chek_platform_collisions(water_rect, [water_dx, water_dy])

    water_pos[0] = water_rect.x
    water_pos[1] = water_rect.y

    if water_pos[1] >= size[1] - water_image.get_height():
        water_pos[1] = size[1] - water_image.get_height()
        water_jumping = False
        water_y_velocity = 0

    for platform in platforms:
        pygame.draw.rect(screen, platform_color, platform)
        pygame.draw.rect(screen, (0, 0, 0), platform, 1)

    

    screen.blit(fire_image, fire_pos)
    screen.blit(water_image, water_pos)

    pygame.display.flip()

    clock.tick(fps)


pygame.quit()
sys.exit()
















        
       