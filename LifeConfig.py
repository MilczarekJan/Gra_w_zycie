from LifeCell import LifeCell
BLUE = (173, 216, 230)
RED = (255, 0, 0)

class LifeConfig:
    @staticmethod
    def binarySearch(arr, low, high, mouse, position):
        start_low = low
        start_high = high
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
    @staticmethod
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