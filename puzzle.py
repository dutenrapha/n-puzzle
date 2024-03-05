import heapq

from metrics import euclidean_distance, misplaced_tiles, chebyshev_distance, manhattan_distance 
def h(state, goal, N, algo):
    if algo == 'euclidean': 
      return(euclidean_distance(state, goal, N))
    elif algo == 'misplaced': 
      return(misplaced_tiles(state, goal))
    elif algo == 'chebyshev': 
      return(chebyshev_distance(state, goal, N))
    else:
      return(manhattan_distance(state, goal, N))


def get_successors(state, N):
    successors = []
    b = state.index(0)
    d, w = divmod(b, N)
   
    if d < N - 1:
        idx = b + N
        successors.append(('Down', state[:b] + [state[idx]] + state[b+1:idx] + [0] + state[idx+1:]))

    if d > 0:
        idx = b - N
        successors.append(('Up', state[:idx] + [0] + state[idx+1:b] + [state[idx]] + state[b+1:]))

    if w < N - 1:
        idx = b + 1
        successors.append(('Right', state[:b] + [state[idx]] + [0] + state[b+2:]))

    if w > 0:
        idx = b - 1
        successors.append(('Left', state[:idx] + [0] + [state[idx]] + state[b+1:]))

    return successors


def a_star(start, goal, N, algo='manhattan'):
    step_max = 0
    open_list = []
    heapq.heappush(open_list, (h(start, goal, N, algo), 0, start, []))
    visited = set()
    path_states = [] 
    complexity_time = 0
    complexity_size = 0
    while open_list:
        complexity_size = max(complexity_size, len(open_list) + len(visited))
        h_val, g_val, current_state, path = heapq.heappop(open_list)
        path_states.append(current_state)
        complexity_time +=1
        if current_state == goal:
            return path_states, path, step_max - 3, complexity_time, complexity_size
     
        visited.add(tuple(current_state))
        step_max = step_max + len(visited)
        for move, successor in get_successors(current_state, N):
            if tuple(successor) not in visited:
                new_path = path + [move]
                heapq.heappush(open_list, (g_val + 1 + h(successor, goal, N, algo), g_val + 1, successor, new_path))
                step_max = step_max + 1
    return None 


def ida_star(start, goal, N, algo='manhattan'):
    step_max = 0
    def search(node, g, bound, path_so_far):
        nonlocal step_max
        f = g + h(node, goal, N, algo)
        if f > bound:
            return f, None, 1
        if node == goal:
            return 0, [(node, path_so_far)], 1

        min_cost = float("inf")
        min_path = None
        total_nodes_expanded = 0
        for move, successor in get_successors(node, N):
            successor_tuple = tuple(successor)
            if successor_tuple not in visited:
                visited.add(successor_tuple)
                step_max = step_max + len(visited) 
                result, path, nodes_expanded = search(successor, g + 1, bound, path_so_far + [move])
                total_nodes_expanded += nodes_expanded
                if result == 0:
                    return 0, [(node, path_so_far)] + path, total_nodes_expanded
                if result < min_cost:
                    min_cost = result
                    min_path = path
                visited.remove(successor_tuple)
        return min_cost, min_path, total_nodes_expanded

    open_list = []
    heapq.heappush(open_list, (h(start, goal, N, algo), 0, start, []))
    bound = h(start, goal, N, algo)
    visited = set()
    complexity_time = 0
    complexity_size = 0

    while True:
        visited.clear()
        visited.add(tuple(start))
        result, path, nodes_expanded = search(start, 0, bound, [])
        complexity_time += nodes_expanded
        complexity_size = max(complexity_size, len(visited))
        if result == 0:
            return [(start, [])] + path, step_max - 3, complexity_time, complexity_size
        if result == float("inf"):
            return None
        bound = result