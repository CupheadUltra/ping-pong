import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Колір
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Розміри рахунків та швидкості
BALL_RADIUS = 20
BALL_SPEED_X = 7
BALL_SPEED_Y = 7
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 10

# Створення м'яча та ракеток
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 -
                   BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
player = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT //
                     2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT //
                       2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Початкова швидкість м'яча
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

# Оновлення екрану
def draw_window():
    win.fill(WHITE)
    pygame.draw.ellipse(win, GREEN, ball)
    pygame.draw.rect(win, GREEN, player)
    pygame.draw.rect(win, GREEN, opponent)
    pygame.display.update()

# Головний цикл
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += PADDLE_SPEED

    if keys[pygame.K_w] and opponent.top > 0:
        opponent.y -= PADDLE_SPEED
    if keys[pygame.K_s] and opponent.bottom < HEIGHT:
        opponent.y += PADDLE_SPEED

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x = -ball_speed_x

    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x
        ball.x = WIDTH // 2 - BALL_RADIUS
        ball.y = HEIGHT // 2 - BALL_RADIUS

    draw_window()
    clock.tick(60)

pygame.quit()
