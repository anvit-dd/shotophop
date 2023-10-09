import tkinter
from tkinter import simpledialog
import pygame
import sys

width, height = 600, 700
flags = pygame.HWSURFACE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((width, height), flags)
screen.fill("white")

open_file_icon = pygame.image.load("Images\\open_icon.png").convert_alpha()
open_file_icon = pygame.transform.scale(open_file_icon, (30, 30))
save_file_icon = pygame.image.load("Images\\save_icon.png").convert_alpha()
save_file_icon = pygame.transform.scale(save_file_icon, (30, 30))
fill_icon = pygame.image.load("Images\\fill_icon.png").convert_alpha()
fill_icon = pygame.transform.scale(fill_icon, (30, 30))
grid_icon = pygame.image.load("Images\\grid_icon.png").convert_alpha()
grid_icon = pygame.transform.scale(grid_icon, (30, 30))
reset_icon = pygame.image.load("Images\\reset_icon.png").convert_alpha()
reset_icon = pygame.transform.scale(reset_icon, (30, 30))
eraser_icon = pygame.image.load("Images\\eraser_icon.png").convert_alpha()
eraser_icon = pygame.transform.scale(eraser_icon, (30, 30))
blackwhite_icon = pygame.image.load("Images\\blackwhite_icon.png").convert_alpha()
blackwhite_icon = pygame.transform.scale(blackwhite_icon, (30, 30))
invert_icon = pygame.image.load("Images\\invert_icon.png")
invert_icon = pygame.transform.scale(invert_icon, (30, 30))
pick_icon = pygame.image.load("Images\\pick_icon.png")
pick_icon = pygame.transform.scale(pick_icon, (30, 30))
brush_one_icon = pygame.image.load("Images\\1x1_icon.png")
brush_one_icon = pygame.transform.scale(brush_one_icon, (30, 30))
brush_two_icon = pygame.image.load("Images\\2x2_icon.png")
brush_two_icon = pygame.transform.scale(brush_two_icon, (30, 30))
brush_three_icon = pygame.image.load("Images\\3x3_icon.png")
brush_three_icon = pygame.transform.scale(brush_three_icon, (30, 30))
brush_four_icon = pygame.image.load("Images\\4x4_icon.png")
brush_four_icon = pygame.transform.scale(brush_four_icon, (30, 30))

color_button_width = 20
color_button_height = 20
pygame.init()
clock = pygame.time.Clock()
running = True
mouse_released = False
mouse_pressed = False
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

menu_color = (40, 40, 40)

top = tkinter.Tk()
top.withdraw()
canvas_dim = simpledialog.askinteger(
    "Input dimensions",
    "Enter the size of your canvas.\nThe canvas will be a sqaure in the range 1-300 px.\n"
)

if canvas_dim is None:
    sys.exit()

elif canvas_dim > 400 or canvas_dim <= 0:
    canvas_dim = 400

pygame.display.set_caption(f"Untitled  |  ShotoPhop  |  {canvas_dim} x {canvas_dim} px")

top.destroy()

pygame.mouse.set_cursor(*pygame.cursors.broken_x)
