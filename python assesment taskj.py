import pygame
import time  #this is usually used to see how long a player has taken to complete a level, but for some reason it comes up as unresolved, probably a pycharm bug.
import math
from utils import scale_image, blit_rotate_center

# Load and scale images of the cars and backgrounds
GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)  # Load and scale the grass image
TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)  # Load and scale the track image
TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)  # Load and scale the track border image
RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)  # Load and scale the red car image
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.55)  # Load and scale the green car image

# Set window dimensions and create the game window
WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()  # Get the width and height of the track image
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create a window with the specified dimensions
pygame.display.set_caption("Racing Game!")  # Sets a caption for the game window called Racing Game.

FPS = 60  # Determines the frames per seconds of the game, a higher fps would result in a smoother gaming expirence

# Abstract class representing a car
class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel  # Maximum velocity of the car
        self.vel = 0  # Current velocity of the car
        self.rotation_vel = rotation_vel  # Rotation velocity of the car
        self.angle = 0  # Current angle of the car
        self.x, self.y = self.START_POS  # Starting position of the car on the track
        self.acceleration = 0.1  # Acceleration of the car
        #These functions help determine the car's state before the player has taken any action, and how it responds when the player does so (Acceleration value preset)

    def rotate(self, left=False, right=False):
        # Rotate the car either left or right based on the input
        if left:
            self.angle += self.rotation_vel  # Increase the angle for a left rotation
        elif right:
            self.angle -= self.rotation_vel  # Decrease the angle for a right rotation

    def draw(self, win):
        # Draw the car on the game window
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        # Accelerate the car and move it forward
        self.vel = min(self.vel + self.acceleration, self.max_vel)  # Increase the velocity up to the maximum velocity
        self.move()

    def move(self):
        # Move the car based on its velocity and angle
        radians = math.radians(self.angle)  # Convert the angle to radians
        vertical = math.cos(radians) * self.vel  # Calculate the vertical component of the movement
        horizontal = math.sin(radians) * self.vel  # Calculate the horizontal component of the movement

        self.y -= vertical  # Move the car vertically
        self.x -= horizontal  # Move the car horizontally
        #These functions allow the car to update its position in a more smooth and realistic manner, giving the player more control of the car.

    def reduce_speed(self):
        # Reduce the car's speed gradually
        self.vel = max(self.vel - self.acceleration / 2, 0)  # Decrease the velocity gradually
        self.move()

# Class representing the player's car, inheriting from AbstractCar
class PlayerCar(AbstractCar):
    IMG = RED_CAR  # Image of the player's car
    START_POS = (180, 200)  # Starting position of the player's car on the track

# Function to draw the game window
def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)  # Draw the background images on the window

    player_car.draw(win)  # Draw the player's car on the window
    pygame.display.update()  # Update the display

run = True
clock = pygame.time.Clock()  # Create a clock object for controlling the frame rate
images = [(GRASS, (0, 0)), (TRACK, (0, 0))]  # List of background images and their positions
player_car = PlayerCar(4, 4)  # Create an instance of the player's car

while run:
    clock.tick(FPS)  # Control the frame rate of the game

    draw(WIN, images, player_car)  # Draw the game window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()  # Get the state of all keyboard keys
    moved = False

    # Check keyboard inputs for car rotation and movement
    if keys[pygame.K_a]:
        player_car.rotate(left=True)  # Rotate the player's car to the left
    if keys[pygame.K_d]:
        player_car.rotate(right=True)  # Rotate the player's car to the right
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()  # Move the player's car forward

    # If no movement input, gradually reduce the car's speed
    if not moved:
        player_car.reduce_speed()  # Reduce the player's car speed gradually

pygame.quit()  # Quit the game and close the window