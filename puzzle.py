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
    open_list = []
    heapq.heappush(open_list, (h(start, goal, N, algo), 0, start, []))
    visited = set()

    while open_list:
        h_val, g_val, current_state, path = heapq.heappop(open_list)
        if current_state == goal:
            return path

        visited.add(tuple(current_state))
        for move, successor in get_successors(current_state, N):
            if tuple(successor) not in visited:
                new_path = path + [move]
                heapq.heappush(open_list, (g_val + 1 + h(successor, goal, N, algo), g_val + 1, successor, new_path))

    return None 

def ida_star(start, goal, N, algo='manhattan'):
    def search(node, g, bound, path_so_far):
        f = g + h(node, goal, N, algo)
        if f > bound:
            return f, None
        if node == goal:
            return 0, [(node, path_so_far)]

        min_cost = float("inf")
        min_path = None
        for move, successor in get_successors(node, N):
            successor_tuple = tuple(successor)
            if successor_tuple not in visited:
                visited.add(successor_tuple)
                result, path = search(successor, g + 1, bound, path_so_far + [move])
                if result == 0:
                    return 0, [(node, path_so_far)] + path
                if result < min_cost:
                    min_cost = result
                    min_path = path
                visited.remove(successor_tuple)
        return min_cost, min_path

    open_list = []
    heapq.heappush(open_list, (h(start, goal, N, algo), 0, start, []))
    bound = h(start, goal, N, algo)
    visited = set()

    while True:
        visited.clear()
        visited.add(tuple(start))
        result, path = search(start, 0, bound, [])
        if result == 0:
            return [(start, [])] + path
        if result == float("inf"):
            return None
        bound = result