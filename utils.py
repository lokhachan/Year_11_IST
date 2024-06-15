import pygame  # Import the pygame library

# Function to scale an image by a factor
def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)  # Calculate the new size based on the scaling factor
    return pygame.transform.scale(img, size)  # Return the scaled image

# Function to blit (draw) a rotated image onto the window
def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)  # Rotate the image by the specified angle
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)  # Get a new rectangle with the rotated image centered at the specified top-left position
    win.blit(rotated_image, new_rect.topleft)  # Blit (draw) the rotated image onto the window

# Function to blit (draw) centered text onto the window
def blit_text_center(win, font, text):
    render = font.render(text, 1, (200, 200, 200))  # Render the text using the specified font and color
    win.blit(render, (win.get_width()/2 - render.get_width()/2, win.get_height()/2 - render.get_height()/2))  # Blit (draw) the rendered text onto the window at the center position