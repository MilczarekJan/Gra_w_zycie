import sys
import pygame
import multiprocessing
import time
from multiprocessing import Pool
from collections import deque
from pygame.locals import *
from lifeconfig import LifeConfig
BLUE = (173, 216, 230)
RED = (255, 0, 0)


def show_cords(cells):
    for line in cells:
        for cell in line:
            print(cell.CenterCords)

def calculate_neighbours(neighbours):
    alive_neighbours = 0
    for neighbour in neighbours:
        if neighbour.Color == BLUE:
            alive_neighbours+=1
    return alive_neighbours

def order_lines(cells):
    lines_actual = cells
    lines_before = lines_actual.copy()
    lines_before.rotate(1)
    lines_after = lines_actual.copy()
    lines_after.rotate(-1)
    return lines_before, lines_actual, lines_after

def update_lines(line_before, line_actual, line_after):
    cells_in_line = int(len(line_actual))
    for i in range(cells_in_line):
        east = (i+1)%cells_in_line
        west = ((i-1)+cells_in_line)%cells_in_line
        neighbours = [line_before[i], line_before[west], line_before[east], line_actual[west], line_actual[east], line_after[west], line_after[i], line_after[east]]
        alive_neighbours = calculate_neighbours(neighbours)
        if line_actual[i].Color == BLUE and alive_neighbours < 2:
            line_actual[i].Color = RED
        elif line_actual[i].Color == BLUE and alive_neighbours > 3:
            line_actual[i].Color = RED
        elif line_actual[i].Color == RED and alive_neighbours == 3:
            line_actual[i].Color = BLUE
    return line_actual

def update_all_cells(cells, screen):
    lines_before, lines_actual, lines_after = order_lines(cells)
    with Pool(processes=multiprocessing.cpu_count()) as pool1:
        new_cells = pool1.starmap(update_lines, zip(lines_before, lines_actual, lines_after))
    pool1.join()
    for line in new_cells:
        for rect in line:
            pygame.draw.rect(screen, rect.Color, rect.CellCords)
    pygame.display.flip()
    return deque(new_cells)

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
    screen = pygame.display.set_mode(display_mode) #To jest zmienna której nie potrafię prawidłowo przekazać procesom.
    screen.fill((255, 255, 255))
    for line in rectangles:
        for rect in line:
            pygame.draw.rect(screen, rect.Color, rect.CellCords)
    pygame.display.flip()

    gameOn = True
    pause = False
    while gameOn:
        for event in pygame.event.get():        
            if event.type == pygame.QUIT:
                gameOn = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                change_cell(rectangles, pygame.mouse.get_pos(), screen)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                if pause == True:
                    pause = False
                else:
                    pause = True
            if not pause:
                rectangles = update_all_cells(rectangles, screen)
    pygame.quit()

if __name__ == '__main__':
    main(int(sys.argv[1]))