import pygame
import math
from cars_neuronal_network import generate_weigths, forward_pass, pre_trained_model
from draw_tracks import track_A
from mutation import new_generation
"""
IN THIS FILE:
-Car rendering: A class that handles car creation(position, angle, colors, steering) 
-Raycast: this file has a function in it that cast raycast in all 5 directions needed to EACH car created using "newCars()" that will later be used as inputs for the car learning. It handles raycast rotation while the car turns and only detects wall collision with walls created using "draw_wall()"
-Connection to the car brain: this file is considered the main file, in it are called all the functions that handle the learning.
"""
print("----------------------")
print(">")
print(">")
input("--Press enter to start > ")


    

pygame.init()
font = pygame.font.Font(None, 36)  # None = default font, 36 = size
screen = pygame.display.set_mode((1600, 1000))
clock = pygame.time.Clock()
running = True
dt = 0 
max_possible_ray_distance = math.sqrt(screen.get_width()**2 + screen.get_height()**2)

class newCars():
        def __init__(self,x,y,color):
            self.x = x
            self.y = y
            self.originalX = x
            self.originalY = y
            self.dead = False
            #Generate random weights 
            self.w1,self.w2 = generate_weigths()
            #self.w1, self.w2 = pre_trained_model()
            self.output = [0,0]
            self.width = 30
            self.height = 50
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.set_colorkey("black")
            self.surface.fill(color)
            #Some details to make the front of the car easier to spot
            pygame.draw.rect(self.surface, "yellow", (self.width - 25, self.height - 6, 5, self.height - 40))
            pygame.draw.rect(self.surface, "yellow", (self.width - 10, self.height - 6, 5, self.height - 40))
            pygame.draw.rect(self.surface, "yellow", (self.width - 4, self.height - 34, 3, self.height - 25))
            pygame.draw.rect(self.surface, "yellow", (self.width - 28, self.height - 34, 3, self.height - 25))
            self.angle_in_degrees = 0
        def draw(self,surface):
            rotated_surface = pygame.transform.rotate(self.surface, self.angle_in_degrees)
            rotated_car = rotated_surface.get_rect(center=(self.x,self.y))
            screen.blit(rotated_surface,rotated_car)

#Cars population
cars = [
        newCars(60, 200,"red"),
        newCars(90,200,"blue"),
        newCars(130,200,"purple"),
        newCars(170,200,"orange"),
        newCars(180,200,"gray30"),
        newCars(75,200,"darkblue")
]
cars_crashed = 0
#Start game loop
generation = 1
while running:
    dt = clock.tick(60) / 1000.0 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("gray")
    pygame.display.set_caption('Machine learning cars')

    """
    The next part is for building the tracks from draw_tracks.py and show the number of the generation
    """
    walls = []
    track_A(screen,walls)
    gen_text = text_surface = font.render(f"Generation: {generation}", True, "black")
    screen.blit(text_surface, (1240, 900))
    """
    This next part is going to handle raycasts and car angles, so the car always move where the front of it is looking and the raycast too.
    """
    for car in cars:
        car.draw(screen)
    def cast_ray(startX,startY,stepX,stepY,walls,screen):
        ray_x = startX 
        ray_y = startY 
        while not any(wall.collidepoint(ray_x,ray_y) for wall in walls):
            ray_x += stepX
            ray_y += stepY
            if ray_y >= screen.get_height() or ray_y <= 0 or ray_x >= screen.get_width() or ray_x <= 0:
                break 
        input_distance = math.sqrt((start_x - ray_x)**2 + (start_y - ray_y )**2)
        normalized_distance = input_distance / max_possible_ray_distance
        return ray_x,ray_y, normalized_distance
    for car in cars:
        """
        Next part is about making the car choose how to rotate and accelerate. First it checks for collisions, and if there is none, it applies the movement logic.
        """
        def check_collisions():
            global cars_crashed
            collided = False
            if car.dead:
                return
            for wall in walls:
                car_rect = pygame.Rect(0,0,car.width,car.height)
                car_rect.center = (car.x, car.y)
                if car_rect.colliderect(wall): 
                    collided = True
                    car.dead = True
                    cars_crashed += 1
                    break
            return collided
        collided = check_collisions()
        get_angle = car.angle_in_degrees + 90
        to_radians = math.radians(-get_angle)
        if collided == False:
            #Car deciding how much to rotate
            car_max_turn = 3 #MAX rotation is +3 numbers per frame
            angle_change = car.output[0] * car_max_turn
            car.angle_in_degrees += angle_change
            #Car deciding how much to accelerate
            car_decides_acceleration = False #If this boolean is change to true, the car will decide by itself the acceleration using output[1] of the car forward pass output. If not, the car will have a fixed acceleration of 3
            car_max_acceleration = 3
            acceleration_change = car.output[1] * car_max_acceleration + 0.5 if car_decides_acceleration else 3
            if acceleration_change <= 0: acceleration_change = 0
            car.y -= math.sin(to_radians) * acceleration_change
            car.x -=  math.cos(to_radians) * acceleration_change
        #Variables used on the raycast logic
        ray_speed = 2
        start_x = car.x
        start_y = car.y
        #Rotate raycast with the car
        def get_ray_angle(offset, ray_speed):
             ray_angle = get_angle + offset + 180
             ray_to_radians = math.radians(-ray_angle)
             stepX = math.cos(ray_to_radians) * ray_speed
             stepY = math.sin(ray_to_radians) * ray_speed 
             return stepX, stepY
        """
        Next part is all about calculating the angle of the raycast and shooting it using cast_ray()
        """
        front_stepX, front_stepY = get_ray_angle(0,2)
        right_stepX, right_stepY = get_ray_angle(90,2)
        left_stepX, left_stepY = get_ray_angle(-90,2)
        dright_stepX, dright_stepY = get_ray_angle(-45,2)
        dleft_stepX, dleft_stepY = get_ray_angle(45,2)
        #First two variables are the raycast X and Y end point and the third variable is the distance from that raycast start point to the it's end point (a wall):
        #Front ray
        fx, fy,fd = cast_ray(start_x, start_y, front_stepX,front_stepY, walls, screen)
        # Right Ray
        rx, ry,rd = cast_ray(start_x, start_y, right_stepX, right_stepY, walls, screen)
        # Left Ray
        lx, ly,ld = cast_ray(start_x, start_y, left_stepX, left_stepY, walls, screen)
        #From front, left rotated raycast:
        lrx, lry,lrd = cast_ray(start_x, start_y,dleft_stepX,dleft_stepY,walls,screen)
        #From front, right rotated ray:
        rrx, rry, rrd = cast_ray(start_x, start_y,dright_stepX,dright_stepY,walls,screen)
        input_neurons_values = [fd,rd,ld,lrd,rrd]
        #Now we'll call the forward pass function with the values that changed during the loop
        car.output = forward_pass(input_neurons_values,car.w1,car.w2)
        if cars_crashed == len(cars):
            generation += 1
            cars_crashed = 0
            new_generation(cars,car)
    pygame.display.flip()
pygame.quit()