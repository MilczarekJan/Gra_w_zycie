import sys
import pygame
from pygame.locals import *
BLUE = (173, 216, 230)
RED = (255, 0, 0)

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
            curr_rect = (left, top, width, height)
            rectangles.append(curr_rect)
    elif size == 100:
        display_mode = (1000, 1000) #10x10, przerwa 2, początek i koniec 1
        width = 8
        height = 8
        distance = width + 2
        rectangles = []
        for rect_num in range(int(rectangle_amount)):
            left = 1
            if rect_num % 100 == 0 and rect_num != 0:
                top = top + distance
            left = left + (rect_num%100)*distance
            curr_rect = (left, top, width, height)
            rectangles.append(curr_rect)
    return display_mode, rectangles
            

pygame.init()
display_mode, rectangles = select_mode(int(sys.argv[1]))
screen = pygame.display.set_mode(display_mode)
screen.fill((255, 255, 255))
for rect in rectangles:
    pygame.draw.rect(screen, BLUE, rect)
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