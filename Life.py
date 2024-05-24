import sys
import pygame
from pygame.locals import *
from LifeConfig import LifeConfig
BLUE = (173, 216, 230)
RED = (255, 0, 0)


def show_cords(cells):
    for line in cells:
        for cell in line:
            print(cell.CenterCords)

def change_cell(cells, mouse, screen):
    line = LifeConfig.binarySearch(cells, 0, len(cells)-1, mouse[1], 1)
    id = LifeConfig.binarySearch(cells[line], 0, len(cells[line])-1, mouse[0], 0)
    if cells[line][id].Color == RED:
        pygame.draw.rect(screen, BLUE, cells[line][id].CellCords)
        pygame.display.flip()
        cells[line][id].Color = BLUE
    else:
        pygame.draw.rect(screen, RED, cells[line][id].CellCords)
        pygame.display.flip()
        cells[line][id].Color = RED
            
def main(mode):
    pygame.init()
    display_mode, rectangles = LifeConfig.select_mode(mode)
    screen = pygame.display.set_mode(display_mode)
    screen.fill((255, 255, 255))
    for line in rectangles:
        for rect in line:
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
            elif event.type == MOUSEBUTTONDOWN:
                change_cell(rectangles, pygame.mouse.get_pos(), screen)

    pygame.quit()

if __name__ == '__main__':
    main(int(sys.argv[1]))