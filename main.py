import pygame
import random

pygame.init()

# Variables
height = 600
width = 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Caylak Yazilimci')
running = True

speed = 5
FPS = 60
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 30)



class Kahraman:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, (192, 32, 81), (self.x, self.y,50, 50))

    def move(self, direction):
        if direction == 'up' and self.y > 0:
            self.y -= speed
        if direction == 'down' and self.y < height - 50:
            self.y += speed
        if direction == 'right' and self.x < width - 50:
            self.x += speed
        if direction == 'left' and self.x > 0:
            self.x -= speed

class Dusman:

    def __init__(self):
        self.x = random.randint(0, width - 50)
        self.y = random.randint(0, height - 50)

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y,50, 50))

    def relocate(self):
        self.x = random.randint(0, width - 50)
        self.y = random.randint(0, height - 50)

def display_score(score):
    score_text =font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))



kahraman = Kahraman(100, 100)
dusman = Dusman()


while running:
    direction = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        direction = "up"
    if keys[pygame.K_DOWN]:
        direction = "down"
    if keys[pygame.K_RIGHT]:
        direction = "right"
    if keys[pygame.K_LEFT]:
        direction = "left"

    screen.fill((0, 0, 0))
    kahraman.draw()
    dusman.draw()
    display_score(score)

    if direction:
        kahraman.move(direction)

    if pygame.Rect(kahraman.x, kahraman.y, 50, 50).colliderect(pygame.Rect(dusman.x, dusman.y,50,50)):
        score += 1
        dusman.relocate()


    pygame.display.update()



    clock.tick(FPS)

pygame.quit()
