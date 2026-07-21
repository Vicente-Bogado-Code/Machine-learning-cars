import pygame
import math

"""
IN THIS FILE:
-Car rendering: A class that handles car creation(position, angle, colors, steering) 
-Raycast: this file has a function in it that cast raycast in all 5 directions needed to EACH car created using "newCars()" that will later be used as inputs for the car learning. It handles raycast rotation while the car turns and only detects wall collision with walls created using "draw_wall()"
"""
pygame.init()
screen = pygame.display.set_mode((1600, 1000))
clock = pygame.time.Clock()
running = True
dt = 0 

#Class to create cars
class newCars():
        def __init__(self,x,y):
            self.x = x
            self.y = y
            self.width = 30
            self.height = 50
            self.velocity = 2
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.set_colorkey("black")
            self.surface.fill("red")
            #Some windows and lights to make the front of the car easier to spot
            pygame.draw.rect(self.surface, "yellow", (self.width - 25, self.height - 6, 5, self.height - 40))
            pygame.draw.rect(self.surface, "yellow", (self.width - 10, self.height - 6, 5, self.height - 40))
            pygame.draw.rect(self.surface, "blue", (self.width - 4, self.height - 34, 3, self.height - 25))
            pygame.draw.rect(self.surface, "blue", (self.width - 28, self.height - 34, 3, self.height - 25))
            self.angle_in_degrees = 0
        def draw(self,surface):
            rotated_surface = pygame.transform.rotate(self.surface, self.angle_in_degrees)
            rotated_car = rotated_surface.get_rect(center=(self.x,self.y))
            screen.blit(rotated_surface,rotated_car)

#function to create walls
def draw_wall(screen, color, pos_x, pos_y, width, height, wall_list):
    wall = pygame.draw.rect(screen, color, (pos_x, pos_y, width, height))
    wall_list.append(wall)
#Cars population
cars = [
    newCars(screen.get_width() / 2, 100),
]

while running:
    dt = clock.tick(60) / 1000.0 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("gray")
    pygame.display.set_caption('Machine learning cars')

    walls = []
    """
    The next part is for creating walls objects for debug purposes
    """
    for i in range(2):
        # Vertical
        change_x = screen.get_width() / 2 - 300 if i == 1 else screen.get_width() / 2 + 300
        draw_wall(screen, "black", change_x, 100, 10, 300, walls)
        # Horizontal
        change_y = 600 if i == 1 else 25
        draw_wall(screen, "black", screen.get_width() / 2 - 300, change_y, 600, 10, walls)
    # Additional walls
    draw_wall(screen, "black", screen.get_width() / 2 + 600, 450, 10, 100, walls)
    draw_wall(screen, "black", screen.get_width() / 2 - 600, 450, 10, 50, walls)

    """
    This next part is going to handle raycasts and car angles, so the car always move where the front of it is looking and the raycast too.
    Also built the collide detection at the very end of it.
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
        return ray_x,ray_y
    keys = pygame.key.get_pressed()
    for car in cars: 
        """
        Next part is about calculating the angle of the car and moving it in the direccion that is facing at the moment
        """
        get_angle = car.angle_in_degrees + 90
        to_radians = math.radians(-get_angle)
        if keys[pygame.K_w]:
            #Inverted because pygame game increases angles clockwise, while math.cos/sin do it counterclockwise
            car.y -= math.sin(to_radians) * car.velocity
            car.x -=  math.cos(to_radians) * car.velocity
        if keys[pygame.K_d]:
                car.angle_in_degrees += 2
        if keys[pygame.K_a]:
                car.angle_in_degrees -= 2
        #Declaring some varibales that need to be on the loop for the raycast behaviour
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
        Collide logic:
        """
        def check_collisions():
            for wall in walls:
                car_rect = pygame.Rect(car.x,car.y,car.width,car.height)
                if car_rect.colliderect(wall):
                    print("Collision detected at: X: ", car.x, "Y: ", car.y)
        check_collisions()
        """
        Next part is all about calculating the angle of the raycast, shooting it using the function for it and then draw them
        """
        front_stepX, front_stepY = get_ray_angle(0,2)
        right_stepX, right_stepY = get_ray_angle(90,2)
        left_stepX, left_stepY = get_ray_angle(-90,2)
        dright_stepX, dright_stepY = get_ray_angle(-45,2)
        dleft_stepX, dleft_stepY = get_ray_angle(45,2)
    #Front ray
        fx, fy = cast_ray(start_x, start_y, front_stepX,front_stepY, walls, screen)
    # Right Ray
        rx, ry = cast_ray(start_x, start_y, right_stepX, right_stepY, walls, screen)
    # Left Ray
        lx, ly = cast_ray(start_x, start_y, left_stepX, left_stepY, walls, screen)
    #From front, left rotated raycast:
        lrx, lry = cast_ray(start_x, start_y,dleft_stepX,dleft_stepY,walls,screen)
    #From front, right rotated ray:
        rrx, rry = cast_ray(start_x, start_y,dright_stepX,dright_stepY,walls,screen)
    #Draw them for debug
        pygame.draw.line(screen, "green", (start_x, start_y), (fx,fy))
        pygame.draw.line(screen, "green", (start_x, start_y), (rx,ry))
        pygame.draw.line(screen, "green", (start_x, start_y), (lx,ly))
        pygame.draw.line(screen, "green", (start_x, start_y), (lrx,lry))
        pygame.draw.line(screen, "green", (start_x, start_y), (rrx,rry))




    pygame.display.flip()
pygame.quit()