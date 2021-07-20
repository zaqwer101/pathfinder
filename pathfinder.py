from queue import Queue
import time

def get_neighbors(point):
    # можно переходить по диагонали
    neighbors = [
        [-1, -1], [0, -1], [1, -1],
        [-1, 0], [1, 0],
        [-1, 1], [0, 1], [1, 1]
    ]
    # можно переходить только вертикально/горизонтально
    # neighbors = [
    #     [-1, 0], [0, 1], [1, 0], [0, -1]
    # ]

    for neighbor in neighbors:
        neighbors[neighbors.index(neighbor)] = [point[0] + neighbor[0], point[1] + neighbor[1]]
    
    return neighbors 

walls = [[7, 7], [5, 1]]
def init_map(max_x, max_y):
    map = []
    for y in range(0, max_y):
        map.append([])
        for x in range(0, max_x):
            if [y, x] in walls:
                map[y].append(f'X')
            else:
                map[y].append(f' ')
    return map

def is_point_correct(point, map):
    if point[0] >= 0 and point[0] < len(map) and point[1] >= 0 and point[1] < len(map[0]) and not point in walls:
        return True
    return False

def draw_map(map):
    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            print(map[y][x], end='')
        print()

map = init_map(20, 20)


frontier = Queue()
reached = []

initial_pos = [5, 5]

frontier.put(initial_pos)
reached.append(initial_pos)

map[initial_pos[0]][initial_pos[1]] = '*'


while not frontier.empty():
    current = frontier.get()
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            for next in get_neighbors(current):
                if not next in reached and is_point_correct(next, map):
                    time.sleep(0.05)
                    print(next)
                    frontier.put(next)
                    reached.append(next)
                    map[next[0]][next[1]] = '*'
                    draw_map(map)