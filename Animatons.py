import turtle
"""
# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.speed(5)

# Function to move the turtle
def move_turtle():
    for _ in range(4):
        t.forward(100)  # Move forward by 100 units
        t.right(90)     # Turn right by 90 degrees

# Animate the turtle
move_turtle()

# Keep the window open until it is closed by the user
wn.mainloop()
"""


# Heart Animation
import turtle
import time

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Heart Animation")

# Create a turtle
t = turtle.Turtle()
t.speed(10)
t.color("red")
t.width(2)

# Function to draw a heart shape
def draw_heart():
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

# Function to animate the heart drawing
def animate_heart():
    draw_heart()
    t.hideturtle()
    time.sleep(1)
    t.clear()

# Animate the heart drawing 5 times
for _ in range(10):
    animate_heart()

# Keep the window open until it is closed by the user
wn.mainloop()

"""
import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Car settings
car_width = 60
car_height = 120
car_x = width // 2
car_y = height - car_height
car_speed = 10

# Car image
car_image = pygame.Surface((car_width, car_height))
car_image.fill(BLACK)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < width - car_width:
        car_x += car_speed
    if keys[pygame.K_UP] and car_y > 0:
        car_y -= car_speed
    if keys[pygame.K_DOWN] and car_y < height - car_height:
        car_y += car_speed

    screen.fill(WHITE)
    screen.blit(car_image, (car_x, car_y))
    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
"""