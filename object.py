import pygame
import random
import math

circle_array = []

WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0,0,0)
score = 0

class Snake:
    def __init__(self, color, height, width, snake_startX, snake_startY, radius):
        self.color = color
        self.height = height 
        self.width = width
        self.snake_startX = snake_startX
        self.snake_startY = snake_startY
        self.radius = radius

    def draw(self):
        pygame.draw.circle(win, self.color, (self.snake_startX, self.snake_startY), self.radius)
    
    def move(self, x, y):
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def get_bigger(self, x, y, score):
        print(score)
        circle_array.append(Circle(x,y, score))

class Circle:
    def __init__(self,score,x = 0,y = 0):
        self.x=x
        self.y=y
        self.score = score
        self.Snake = Snake
        self.draw()

    def draw(self):
        pygame.draw.circle(win, BLACK, ((self.x + 10 * self.score), (self.y + 10 * self.score)), 10)


class Apple:
    def __init__(self, color, radius, x = None, y = None):
        self.color = color
        self.radius = radius
        self.score = 0
        self.x, self.y = x, y
        if not x or not y: self.new_position()
    
    def new_position(self):
        self.x, self.y = random.choice(range(0, WIDTH, 25)), random.choice(range(0, HEIGHT, 25))

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def tuch(self, snake_x, snake_y, snake_radius):
        if self.radius * 2 > math.sqrt((self.x - snake_x)**2 + (self.y - snake_y)**2):
                self.new_position()
                return True
        return False
