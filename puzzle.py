import sys
import heapq
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue

def manhattan_distance(state, goal, N):
    distance = 0
    for i in range(N):
        for j in range(N):
            if state[i][j] != 0:
                goal_i, goal_j = next((x, y) for x in range(N) for y in range(N) if goal[x][y] == state[i][j])
                distance += abs(goal_i - i) + abs(goal_j - j)
    return distance


def get_neighbors(state, N):
    neighbors = []
    i, j = next((i, j) for i, row in enumerate(state) for j, x in enumerate(row) if x == 0)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append(new_state)
    return neighbors

def a_star_puzzle(start, goal, N):
    open_set = [(manhattan_distance(start, goal, N), start, 0, None)]
    #print(open_set)
    open_set_set = set([tuple(map(tuple, start))])
    came_from = {}
    g_score = {str(start): 0}
    #print(g_score)
    #sys.exit()

    while open_set:
        _, current, g, parent = min(open_set, key=lambda x: x[0])
        open_set.remove((_, current, g, parent))

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(str(current))
            return path[::-1]

        for neighbor in get_neighbors(current, N):
            neighbor_g = g + 1
            neighbor_f = neighbor_g + manhattan_distance(neighbor, goal, N)
            neighbor_str = str(neighbor)
            
            if neighbor_g < g_score.get(neighbor_str, float('inf')):
                came_from[neighbor_str] = current
                g_score[neighbor_str] = neighbor_g
                if (neighbor_f, neighbor, neighbor_g, current) not in open_set:
                    open_set.append((neighbor_f, neighbor, neighbor_g, current))

    return "Path nor found"

