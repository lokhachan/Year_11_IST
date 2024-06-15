import pygame
import time
import math
from utils import scale_image, blit_rotate_center, blit_text_center
pygame.init()
pygame.font.init()

#The code below loads all the images and assets used, and scales them from the directory (python assets folder)
GRASS = scale_image(pygame.image.load("python assets folder/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("python assets folder/track.png"), 0.9)

TRACK_BORDER = scale_image(pygame.image.load("python assets folder/track-border.png"), 0.9)
# Scale the image to 90% of its original size using the scale_image() function
# Assign the resulting image to the variable TRACK_BORDER
#Adding Masks allows me to determine the areas where objects could collide, allowing me to add collisions into the game.

TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
# Create a collision mask for the TRACK_BORDER image
# Use the from_surface() function of the pygame.mask module to generate a collision mask based on the opaque parts of the image
# Assign the collision mask to the variable TRACK_BORDER_MASK

FINISH = pygame.image.load("python assets folder/finish.png")
# Assigns the loaded image to the variable FINISH

FINISH_MASK = pygame.mask.from_surface(FINISH)
# Create a collision area for the FINISH image
# Use the from_surface() function of the pygame.mask module to generate a collision mask based on the opaque parts of the image
# Assign the collision mask to the variable FINISH_MASK



FINISH_POSITION = (130, 250)
# Assign the tuple (130, 250) to the variable FINISH_POSITION
# Represents the position at which the FINISH image will be drawn on the game window
# The values (130, 250) indicate the x and y coordinates, where the top-left corner of the image will be placed

BLUE_CAR = scale_image(pygame.image.load("python assets folder/blue-car.png"), 0.10)
RED_CAR = scale_image(pygame.image.load("python assets folder/red-car.png"), 0.10)
# Loads and scales both the blue car and red car image.

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height() #This gets the width and height of the track image
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #This creates the game window
pygame.display.set_caption("Racing Game!") #This sets the caption for the game window

MAIN_FONT = pygame.font.SysFont("Arial", 44)
#This creates a font object for displaying text
FPS = 60 #This sets the frames per second for the game, allowing for a smoother expirence
PATH = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
        (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]
#The path function is used by the computer car, allowing it to follow the track.

class GameInfo:
    LEVELS = 5 #total numer of levels in the game

    def __init__(self, level=1):
        self.level = level # Current level of the game
        self.started = False # Flag indicating if the game has started
        self.level_start_time = 0 #Time at which the current level started

    def next_level(self):
        self.level += 1 # Move to the next level
        self.started = False # Reset the started flag

    def reset(self):
        self.level = 1 # Reset the level to 1
        self.started = False # Reset the started flag
        self.level_start_time = 0 # Reset the level start time

    def game_finished(self):
        return self.level > self.LEVELS #This checks whether the game is finished (after all levels are completed)

    def start_level(self):
        self.started = True  # Start the current level
        self.level_start_time = time.time() # Record the level start time

    def get_level_time(self):
        if not self.started:
            return 0  # If the level hasn't started, return 0
        return round(time.time() - self.level_start_time) # Calculate the elapsed time for the current level



class AbstractCar:#This is a parent class that sets conditions for both the player and computer car
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel # Maximum velocity of the car
        self.vel = 0 #Current velocity of the car
        self.rotation_vel = rotation_vel # Rotation velocity of the car
        self.angle = 0 # Current angle of the car
        self.x, self.y = self.START_POS # Starting position of the car
        self.acceleration = 0.1 # Acceleration rate of the car

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel # Rotate the car to the left
        elif right:
            self.angle -= self.rotation_vel # Rotate the car to the right

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
        # Draw the car on the game window

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel) # Increase the velocity of the car
#This line of code updates the velocity (self.vel) of an object by adding the acceleration (self.acceleration) but ensures that the new velocity does not exceed the maximum velocity (self.max_vel).

        self.move() # Moves the car

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)  #Decreases the velocity of the car
        self.move() #Moves the car

    def move(self):
        radians = math.radians(self.angle)  # Convert the angle to radians
        vertical = math.cos(radians) * self.vel # Calculate the vertical component of the movement
        horizontal = math.sin(radians) * self.vel # Calculate the horizontal component of the movement
        #print(f"radians: {radians}, vertical: {vertical}, horizontal: {horizontal}")
        self.y -= vertical  #Update the y-coordinate of the car

        self.x -= horizontal # Update the x-coordinate of the car
        #These lines updates the position of an object in a 2D space using its velocity and angle. It first converts the angle from degrees to radians. Then, it calculates the vertical and horizontal components of the object's movement based on the cosine and sine of the angle, multiplied by the velocity. The object's y-coordinate is updated by subtracting the vertical distance, and the x-coordinate is updated by subtracting the horizontal distance. Together, these calculations enable the object to move in a specific direction determined by the angle and velocity, resulting in a defined trajectory.

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)  #Create a collision mask for the car image
        offset = (int(self.x - x), int(self.y - y)) # Calculates the offset of the car's position
        poi = mask.overlap(car_mask, offset) # Check for collision with the given mask at the offset
        return poi # Returns the point of intersection (collision) if any

    def reset(self):
        self.x, self.y = self.START_POS # Reset the car's position to the starting position
        self.angle = 0 # Reset the car's angle
        self.vel = 0 # Reset the car's velocity


class PlayerCar(AbstractCar): #This is the class for the player's class, the (Abstract Car) function allows us to copy the same functions of rules that apply to the abstract car and applies it here
    IMG = BLUE_CAR
    START_POS = (170,100) #(170, 300)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)# Reduce the speed of the car

        self.move()

    def bounce(self):
        print("Bounce")
        # self.vel = -self.vel
        # self.move()


class ComputerCar(AbstractCar):#Still inherits the same condtions from the Abstract Car parent class
    IMG = RED_CAR # Assign the red car image to the IMG attribute
    START_POS = (150, 100)  #Starting position of the computer car

    def __init__(self, max_vel, rotation_vel, path=[]):
        super().__init__(max_vel, rotation_vel) # Initialize the parent class (AbstractCar)
        self.path = path # Set the path for the computer car to follow (can be found at the beginning of the code)
        self.current_point = 0 #keep track of the current point in the path that the car is moving towards
        self.vel = max_vel # Set the initial velocity of the car to the maximum velocity provided

    def draw_points(self, win):
        for point in self.path:
            pygame.draw.circle(win, (255, 0, 0), point, 5)
            # Draw a red circle at each point in the path
            #Can be used to represent the car's path and trajectory, this is useful because it allows us to determine whether the car is following the intended path or not


    def draw(self, win):
        super().draw(win)
        self.draw_points(win)

    def calculate_angle(self):
        target_x, target_y = self.path[self.current_point]  #Get the x and y coordinates of the current target point
        x_diff = target_x - self.x # Calculate the difference between the target x-coordinate and the car's x-coordinate
        y_diff = target_y - self.y # Calculate the difference between the target y-coordinate and the car's y-coordinate


        if y_diff == 0:
            desired_radian_angle = math.pi / 2 # Set the desired angle to 90 degrees (pi/2) if y_diff is 0

        else:
            desired_radian_angle = math.atan(x_diff / y_diff) # Calculate the desired angle using the arctangent function

        if target_y > self.y:
            desired_radian_angle += math.pi # Add pi (180 degrees) to the desired angle if the target is below the car


        difference_in_angle = self.angle - math.degrees(desired_radian_angle)  # Calculate the difference between the car's current angle and the desired angle in degrees
        if difference_in_angle >= 180:
            difference_in_angle -= 360  # Adjust the difference if it exceeds 180 degrees

        if difference_in_angle > 0:
            self.angle -= min(self.rotation_vel, abs(difference_in_angle))  # Decrease the car's angle by the minimum between the rotation velocity and the absolute difference in angle
        else:
            self.angle += min(self.rotation_vel, abs(difference_in_angle)) # Increase the car's angle by the minimum between the rotation velocity and the absolute difference in angle

    def update_path_point(self):
        target = self.path[self.current_point] # Get the current target point
        rect = pygame.Rect(
            self.x, self.y, self.img.get_width(), self.img.get_height()) # Create a rectangle representing the car's position and size
        if rect.collidepoint(*target):  # Check if the rectangle collides with the target point
            self.current_point += 1  # If there is a collision, move to the next target point in the path


    def move(self):
        if self.current_point >= len(self.path):
            return  # If the current point exceeds the number of points in the path, return and do not move the car

        self.calculate_angle() # Calculate the angle of movement
        self.update_path_point() # Update the current target point
        super().move()  #Call the move method of the parent class

    def next_level(self, level):
        self.reset()  # Reset the car's position and angle
        self.vel = self.max_vel + (level - 1) * 0.2 # Increase the car's velocity based on the level
        self.current_point = 0 # Reset the current target point to the beginning of the path


def draw(win, images, player_car, computer_car, game_info):
    for img, pos in images:
        win.blit(img, pos)

    level_text = MAIN_FONT.render(
        f"Level {game_info.level}", 1, (255, 255, 255))
    win.blit(level_text, (10, HEIGHT - level_text.get_height() - 70))

    time_text = MAIN_FONT.render(
        f"Time: {game_info.get_level_time()}s", 1, (255, 255, 255))
    win.blit(time_text, (10, HEIGHT - time_text.get_height() - 40))

    vel_text = MAIN_FONT.render(
        f"Vel: {round(player_car.vel, 1)}px/s", 1, (255, 255, 255))
    win.blit(vel_text, (10, HEIGHT - vel_text.get_height() - 10))

    player_car.draw(win)
    computer_car.draw(win)
    pygame.display.update()


def move_player(player_car):
    keys = pygame.key.get_pressed() # Get the current state of all keyboard keys
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)  #Rotate the player car to the left if the 'a' key is pressed
    if keys[pygame.K_d]:
        player_car.rotate(right=True)  #Rotate the player car to the right if the 'd' key is pressed
    if keys[pygame.K_w]:

        moved = True
        player_car.move_forward() # Move the player car forward if the 'w' key is pressed
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward() # Move the player car backward if the 's' key is pressed

    if not moved:
        player_car.reduce_speed()  #Reduce the player car's speed if no movement keys are pressed


def handle_collision(player_car, computer_car, game_info):
    if player_car.collide(TRACK_BORDER_MASK) != None: # Check if the player car collides with the track border
        player_car.bounce()  # Make the player car bounce off the track border


    computer_finish_poi_collide = computer_car.collide(
        FINISH_MASK, *FINISH_POSITION)  #Check if the computer car collides with the finish point
    if computer_finish_poi_collide != None:
        blit_text_center(WIN, MAIN_FONT, "YOU LOST TRY AGAIN")
        pygame.display.update()
        pygame.time.wait(5000) # Wait for 5 seconds
        game_info.reset() # Reset the game info
        player_car.reset() # Reset the player car
        computer_car.reset()# Reset the computer car

    player_finish_poi_collide = player_car.collide(
        FINISH_MASK, *FINISH_POSITION) # Check if the player car collides with the finish point
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            player_car.bounce()  # Make the player car bounce off the finish point if it collides with the top boundary
        else:
            game_info.next_level() # Move to the next level in the game
            player_car.reset() # Reset the player car
            computer_car.next_level(game_info.level) # Move the computer car to the next level


run = True
clock = pygame.time.Clock() # Create a clock object to track time
images = [(GRASS, (0, 0)), (TRACK, (0, 0)),
          (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))] # List of images and their positions
player_car = PlayerCar(4, 4) # Create a player car object with initial position (4, 4)
computer_car = ComputerCar(2, 4, PATH)  #Create a computer car object with initial position (2, 4) and a given path
game_info = GameInfo() # Create a game info object

while run:
    clock.tick(FPS) # Limit the frame rate to a maximum of FPS (frames per second)

    draw(WIN, images, player_car, computer_car, game_info) # Draw the window, images, player car, computer car, and game info

    while not game_info.started:
        blit_text_center(WIN, MAIN_FONT, f"Press any key to start level {game_info.level}!")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  #Quit the game if the window is closed
                break

            if event.type == pygame.KEYDOWN:
                game_info.start_level() # Start the level when any key is pressed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  #Stop the game if the window is closed
            break

    move_player(player_car) # Move the player car based on keyboard input
    computer_car.move()  # Move the computer car

    handle_collision(player_car, computer_car, game_info) # Handle collisions between cars and game objects


    if game_info.game_finished():
        blit_text_center(WIN, MAIN_FONT, "Congratulations, You WON!")
        pygame.time.wait(5000) # Wait for 5 seconds
        game_info.reset() # Reset the game info
        player_car.reset()  # Reset the player car
        computer_car.reset()  # Reset the computer car


pygame.quit() # Quit the game and closes the window