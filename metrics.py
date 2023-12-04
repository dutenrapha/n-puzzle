def euclidean_distance(puzzle, goal, N):
    distance = 0
    for i in range(len(puzzle)):
        x1, y1 = divmod(puzzle[i], N)
        x2, y2 = divmod(goal.index(i), N)
        distance += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance

def misplaced_tiles(puzzle, goal):
    count = 0
    for i in range(len(puzzle)):
        if puzzle[i] != goal[i]:
            count += 1
    return count

def chebyshev_distance(puzzle, goal, N):
    distance = 0
    for i in range(len(puzzle)):
        x1, y1 = divmod(puzzle[i], N)
        x2, y2 = divmod(goal.index(i), N)
        distance = max(distance, abs(x1 - x2), abs(y1 - y2))
    return distance

def manhattan_distance(state, goal, N):
    distance = 0
    side_length = int(len(state) ** 0.5)
    for number in range(1, N**2):
        current_index = state.index(number)
        goal_index = goal.index(number)
        current_row, current_col = divmod(current_index, side_length)
        goal_row, goal_col = divmod(goal_index, side_length)
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance