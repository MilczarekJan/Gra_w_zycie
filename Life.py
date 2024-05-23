import sys
import pygame
from pygame.locals import *
BLUE = (173, 216, 230)
RED = (255, 0, 0)


class LifeCell:
    def __init__(self, cords, center_cords, id, color) -> None:
        self.CellCords = cords
        self.CenterCords = center_cords
        self.Id = id
        self.Color = color

def select_mode(size):
    rectangle_amount = size*size
    left = 1
    top = 1
    if size == 10:
        display_mode = (480, 480) #10x10, przerwa 2, początek i koniec 1
        width = 46
        height = 46
        distance = width + 2
        rectangles = []
        for rect_num in range(int(rectangle_amount)):
            left = 1
            if rect_num % 10 == 0 and rect_num != 0:
                top = top + distance
            left = left + (rect_num%10)*distance
            x_center = left + (width/2)
            y_center = top + (height/2)
            curr_rect = LifeCell((left, top, width, height), (x_center, y_center), rect_num, BLUE)
            rectangles.append(curr_rect)
    elif size == 100:
        display_mode = (1000, 1000)
        width = 8
        height = 8
        distance = width + 2
        rectangles = []
        for rect_num in range(int(rectangle_amount)):
            left = 1
            if rect_num % 100 == 0 and rect_num != 0:
                top = top + distance
            left = left + (rect_num%100)*distance
            x_center = left + (width/2)
            y_center = top + (height/2)
            curr_rect = LifeCell((left, top, width, height), (x_center, y_center), rect_num, BLUE)
            rectangles.append(curr_rect)
    return display_mode, rectangles
            

pygame.init()
display_mode, rectangles = select_mode(int(sys.argv[1]))
screen = pygame.display.set_mode(display_mode)
screen.fill((255, 255, 255))
for rect in rectangles:
    pygame.draw.rect(screen, rect.Color, rect.CellCords)
pygame.display.flip()

# Variable to keep our game loop running
gameOn = True
while gameOn:
    # for loop through the event queue
    for event in pygame.event.get():        
        if event.type == QUIT:
            gameOn = False
            break
pygame.quit()