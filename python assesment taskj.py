import pygame
import time  #use of these modules allow players to
import math
from utils import scale_image, blit_rotate_center

# Load and scale images of the cars and backgrounds
GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)
TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.55)

# Set window dimensions and create the game window
WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()  #determining this allows us to prevent cars from going out of the track
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Creates a game window
pygame.display.set_caption("Racing Game!")  #Displays game's name/caption and places it at the bottom of the game

FPS = 60 #Determines the framerate of the game

# Abstract class representing a car
class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS  #Determines starting position on the track, eg left and right
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        # Rotate the car either left or right based on the input
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        # Draw the car on the game window
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        # Accelerate the car and move it forward
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        # Move the car based on its velocity and angle
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        # Reduce the car's speed gradually
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

# Class representing the player's car, inheriting from AbstractCar
class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200)

# Function to draw the game window
def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    pygame.display.update()

run = True
clock = pygame.time.Clock() #Determines how long the player takes to complete the level
images = [(GRASS, (0, 0)), (TRACK, (0, 0))]  #Background and Track
player_car = PlayerCar(4, 4)

while run:
    clock.tick(FPS)

    draw(WIN, images, player_car)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    moved = False

    # Check keyboard inputs for car rotation and movement
    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()

    # If no movement input, gradually reduce the car's speed
    if not moved:
        player_car.reduce_speed()

pygame.quit()