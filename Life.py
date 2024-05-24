import sys
import pygame
from operator import itemgetter, attrgetter
from pygame.locals import *
from LifeCell import LifeCell
BLUE = (173, 216, 230)
RED = (255, 0, 0)


def contain(square, point):
    #print(f'bSearch square: CellCords: {square.CellCords}, CenterCords{square.CenterCords}\n')
    #print(f'bSearch point:{point}\n')
    if point[0] >= square.CellCords[0] and point[0] <= square.CellCords[0] + square.CellCords[2]:
        if point[1] >= square.CellCords[1] and point[1] <= square.CellCords[1] + square.CellCords[3]:
            return True
    else: 
        return False

def show_cords(cells):
    for line in cells:
        for cell in line:
            print(cell.CenterCords)

def binarySearch(arr, low, high, mouse, position):
    start_low = low
    start_high = high
    print(f'start_low: {start_low}\n')
    print(f'start_high: {start_high}\n')
    if position == 1:
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid][0].CenterCords[position] == mouse:
                break
            elif arr[mid][0].CenterCords[position] < mouse:
                low = mid + 1
            else:
                high = mid - 1
        if(low < start_low):
            low = start_low
        elif(low > start_high):
            low = start_high
        low_val = arr[low][0].CenterCords[position]
        mid_val = arr[mid][0].CenterCords[position]
        high_val = arr[high][0].CenterCords[position]
        if abs(mouse - low_val) < abs(mouse - high_val) and abs(mouse - low_val) < abs(mouse - mid_val):
            return low
        elif abs(mouse - high_val) < abs(mouse - mid_val) and abs(mouse - high_val) < abs(mouse - low_val):
            return high
        else:
            return mid
        #Tutaj dać wybór high, low lub mid w zależności która różnica najbliżej mouse i zwrócić indeks(linie)
    else:
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid].CenterCords[position] == mouse:
                break
            elif arr[mid].CenterCords[position] < mouse:
                low = mid + 1
            else:
                high = mid - 1
        if(low < start_low):
            low = start_low
        elif(low > start_high):
            low = start_high
        low_val = arr[low].CenterCords[position]
        mid_val = arr[mid].CenterCords[position]
        high_val = arr[high].CenterCords[position]
        if abs(mouse - low_val) < abs(mouse - high_val) and abs(mouse - low_val) < abs(mouse - mid_val):
            return low
        elif abs(mouse - high_val) < abs(mouse - mid_val) and abs(mouse - high_val) < abs(mouse - low_val):
            return high
        else:
            return mid

def change_cell(cells, mouse, screen):
    line = binarySearch(cells, 0, len(cells)-1, mouse[1], 1)
    id = binarySearch(cells[line], 0, len(cells[line])-1, mouse[0], 0)
    if cells[line][id].Color == RED:
        pygame.draw.rect(screen, BLUE, cells[line][id].CellCords)
        pygame.display.flip()
        cells[line][id].Color = BLUE
    else:
        pygame.draw.rect(screen, RED, cells[line][id].CellCords)
        pygame.display.flip()
        cells[line][id].Color = RED


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
        line = []
        for rect_num in range(int(rectangle_amount)):
            left = 1
            if rect_num % 10 == 0 and rect_num != 0:
                top = top + distance
                rectangles.append(line)
                line = []
            left = left + (rect_num%10)*distance
            x_center = left + (width/2)
            y_center = top + (height/2)
            curr_rect = LifeCell((left, top, width, height), (x_center, y_center), rect_num, BLUE)
            line.append(curr_rect)
        rectangles.append(line)
    elif size == 100:
        display_mode = (1000, 1000)
        width = 8
        height = 8
        distance = width + 2
        rectangles = []
        line = []
        for rect_num in range(int(rectangle_amount)):
            left = 1
            if rect_num % 100 == 0 and rect_num != 0:
                top = top + distance
                rectangles.append(line)
                line = []
            left = left + (rect_num%100)*distance
            x_center = left + (width/2)
            y_center = top + (height/2)
            curr_rect = LifeCell((left, top, width, height), (x_center, y_center), rect_num, BLUE)
            line.append(curr_rect)
        rectangles.append(line)
    return display_mode, rectangles
            
def main(mode):
    pygame.init()
    display_mode, rectangles = select_mode(mode)
    #sorted(rectangles, key=attrgetter('CenterCords'))
    show_cords(rectangles)
    print(len(rectangles[0]))
    print(len(rectangles))
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
                #print(f'MOUSE:{pygame.mouse.get_pos()}')
                change_cell(rectangles, pygame.mouse.get_pos(), screen)

    pygame.quit()

if __name__ == '__main__':
    main(int(sys.argv[1]))