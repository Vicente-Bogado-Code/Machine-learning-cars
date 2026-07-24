import pygame
#function to create walls, used only in draw_tracks.py
def draw_wall(screen, color, pos_x, pos_y, width, height, wall_list):
    wall = pygame.draw.rect(screen, color, (pos_x, pos_y, width, height))
    wall_list.append(wall)
def track_A(screen,wall_list):
   #draw_wall(surface,color,Xpos,Ypos,width,height,wall_list)
   draw_wall(screen,"black",20,45,10,510,wall_list)
   draw_wall(screen,"black",200,200,10,200,wall_list)
   draw_wall(screen,"black",20,550,500,10,wall_list)
   draw_wall(screen,"black",200,400,550,10,wall_list)
   draw_wall(screen,"black",750,400,10,350,wall_list)
   draw_wall(screen,"black",520,550,10,350,wall_list)
   draw_wall(screen,"black",520,900,700,10,wall_list)
   draw_wall(screen,"black",1210,550,10,350,wall_list)
   draw_wall(screen,"black",750,750,280,10,wall_list)
   draw_wall(screen,"black",1020,380,10,380,wall_list)
   draw_wall(screen,"black",1020,380,350,10,wall_list)
   draw_wall(screen,"black",1210,550,380,10,wall_list)
   draw_wall(screen,"black",1580,50,10,500,wall_list)
   draw_wall(screen,"black",1360,200,10,180,wall_list)
   draw_wall(screen,"black",20,45,1570,10,wall_list)
   draw_wall(screen,"black",200,200,1160,10,wall_list)