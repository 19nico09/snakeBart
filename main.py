import pygame 
import time
import object
import random

pygame.init()
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Snake_variables 
snake_height = 10
snake_width = 10
snake_radius = 20
snake_startX, snake_startY = 250, 250

# Apple variables
apple_radius = 10

# Colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 252, 0)
GREY = (220, 220, 220)
RED = (255, 0, 0)
LIGHT_GRAY = (211, 211, 211)

# Game options
win.fill(WHITE)
x = snake_startX
y = snake_startY
apple_x = random.randint(0,WIDTH-50)
apple_y = random.randint(0,HEIGHT-50)
vel = 1
score = 0
pressed_keys = {
    'left': False,
    'right': False,
    'up': False,
    'down': False
}

snake = object.Snake(RED, snake_height, snake_width, snake_startX, snake_startY, snake_radius)
apple = object.Apple(BLACK, apple_radius)
circle = object.Circle(x, y)

def game():
    print('game')
    start_time = time.time()

    global x
    global y
    global score

    run = True 
    while run: 

        for event in pygame.event.get():
            
            keys = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_LEFT]:
                        pressed_keys['left'] = True
                        pressed_keys['right'] = False
                        pressed_keys['up'] = False
                        pressed_keys['down'] = False
                if keys[pygame.K_RIGHT]:
                        pressed_keys['left'] = False
                        pressed_keys['right'] = True
                        pressed_keys['up'] = False
                        pressed_keys['down'] = False
                if keys[pygame.K_UP]:
                        pressed_keys['left'] = False
                        pressed_keys['right'] = False
                        pressed_keys['up'] = True
                        pressed_keys['down'] = False
                if keys[pygame.K_DOWN]:
                        pressed_keys['left'] = False
                        pressed_keys['right'] = False
                        pressed_keys['up'] = False
                        pressed_keys['down'] = True

        if pressed_keys['left']:
            x += -vel
        elif pressed_keys['right']:
            x += vel
        elif pressed_keys['up']:
            y += -vel 
        else:
            y += vel

        if not WIDTH > x > 0 or not HEIGHT > y > 0:
            print('Game over')
            run = False


        win.fill(WHITE)
        apple.draw()
        snake.move(x, y) 
        if apple.tuch(x, y, snake_radius):
            score += 1
            snake.get_bigger(x, y, score)
        for circle in object.circle_array:
            circle.draw(score)
        
        
        pygame.display.update()
        clock.tick(60)

game()

if __name__ == '__main__':
    game()