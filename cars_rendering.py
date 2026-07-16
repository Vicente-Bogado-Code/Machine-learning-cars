import pygame

pygame.init()
screen = pygame.display.set_mode((1600, 1000))
clock = pygame.time.Clock()
running = True
dt = 0 

class newCar():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 40
        self.velocity = 100 # Speed per second
    def draw(self, surface):
        pygame.draw.rect(surface, "red", (self.x, self.y, self.width, self.height))

def draw_wall(screen, color, pos_x, pos_y, width, height, wall_list):
    wall = pygame.draw.rect(screen, color, (pos_x, pos_y, width, height))
    wall_list.append(wall)

cars = [
    newCar(screen.get_width() / 2, 100)
]
while running:
    dt = clock.tick(60) / 1000.0 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("gray")

    walls = []
    # walls
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

    for car in cars:
        car.draw(screen)
    # Set raycasts
    def cast_ray(startX,startY,stepX,stepY,walls,screen):
        ray_x = startX
        ray_y = startY
        while not any(wall.collidepoint(ray_x,ray_y) for wall in walls):
            ray_x += stepX
            ray_y += stepY
            if ray_y >= screen.get_height() or ray_y <= 0 or ray_x >= screen.get_width() or ray_x <= 0:
                break 
        return ray_x,ray_y

    for car in cars:    
        start_x = car.x + car.width / 2
        start_y = car.y + car.height / 2
        fx, fy = cast_ray(start_x, start_y, 0, 5, walls, screen)
    # Right Ray
        rx, ry = cast_ray(start_x, start_y, 5, 0, walls, screen)
    # Left Ray
        lx, ly = cast_ray(start_x, start_y, -5, 0, walls, screen)
        pygame.draw.line(screen, "green", (start_x, start_y), (fx,fy))
        pygame.draw.line(screen, "yellow", (start_x, start_y), (rx,ry))
        pygame.draw.line(screen, "blue", (start_x, start_y), (lx,ly))
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        cars[0].y += cars[0].velocity * dt   
    if keys[pygame.K_w]:
        cars[0].y -= cars[0].velocity * dt 
    pygame.display.flip()
pygame.quit()