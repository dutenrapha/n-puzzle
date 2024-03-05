import sys
import argparse

from time import time

from puzzle import a_star, ida_star

from tabulate import tabulate

def parser_board(board, sizeboard):

    if sizeboard < 2:
        return '\033[0;31mError: square board must be higher or equal then 2.\033[0;00m'

    if not all(valor.isdigit() for valor in board):
        return '\033[0;31mError: all arguments of input must be numeric.\033[0;00m'

    if len(board) / int(sizeboard) != int(sizeboard):
        return '\033[0;31mError: input must be a square board (NxN).\033[0;00m'

    if any(int(value) < 0 or int(value) >= int(sizeboard)**2 for value in board):
        return f'\033[0;31mError: all arguments of puzzle must be between 0 and {int(sizeboard)**2-1}.\033[0;00m'
    
    if len(set(board)) != len(board):
        return '\033[0;31mError: arguments must be unique.\033[0;00m'

    return 'continue'


def while_if_zero(value):
	if value == 0:
		return '\033[47m' + ' ' * len(str(value)) + '\033[0m'
	else:
		return value


def count_inversions(state):
    flatten_state = [number for line in state for number in line if number != 0]
    numbinversions = 0

    for i, number1 in enumerate(state):
        for number2 in state[i+1:]:
            if number1 > number2:
                numbinversions += 1

    return numbinversions



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='N-Puzzle', description='The goal of this project is to programmatically solve the N-puzzle.', epilog='Solve it better than brut force!')
    parser.add_argument('filename', type=argparse.FileType("r"))
    parser.add_argument('-astar', action='store_true')
    parser.add_argument('-manhattan', action='store_true')
    parser.add_argument('-euclidean', action='store_true')
    parser.add_argument('-misplaced', action='store_true')
    parser.add_argument('-chebyshev', action='store_true')

    args = parser.parse_args()

    with args.filename as file:
        data = [line.strip().split("#")[0].strip() for line in file] # erase comments
    data = list(filter(lambda x: x != '', data)) # remove empty lines of list
    
    size = int(data.pop(0)) if data else None
    data = ' '.join(data).split()

    if parser_board(data, size) != 'continue':
        print(parser_board(data, size))
        sys.exit()

    initial_state = [int(value) for value in data] # Convert into int list
    initial_state_ck = [initial_state[i:i+size] for i in range(0, len(initial_state), size)] # group in sublist
    
    goal_state = list(range(1, size**2 - 1 + 1))
    goal_state.append(0) # insert last element
    goal_state_ck = [goal_state[i:i+size] for i in range(0, len(goal_state), size)] # group in sublist
    
    initial_invertions = count_inversions(initial_state_ck)
    goal_invertions = count_inversions(goal_state_ck)
    if initial_invertions % 2 != goal_invertions % 2:
        print('\033[0;31mError: No solution.\033[0;00m')
        sys.exit()

    print('initial_state:')
    print(tabulate(initial_state_ck, tablefmt="fancy_grid"))
    print('goal_state:')
    print(tabulate(goal_state_ck, tablefmt="fancy_grid"))

    if args.astar:
        start_time = time()
        if size == 3:
            if args.manhattan == True:
                path_states, path, step_max, complexity_time, complexity_size = a_star(initial_state, goal_state, size, "manhattan")
                print("\n\033[1;32mSolved using method A* with manhattan heuristic\n\033[0;00m")
            if args.euclidean == True:
                path_states, path, step_max, complexity_time, complexity_size = a_star(initial_state, goal_state, size, "euclidean")
                print("\n\033[1;32mSolved using method A* with euclidean heuristic\n\033[0;00m")
            if args.misplaced == True:
                path_states, path, step_max, complexity_time, complexity_size = a_star(initial_state, goal_state, size, "misplaced")
                print("\n\033[1;32mSolved using method A* with misplaced heuristic\n\033[0;00m")
            if args.chebyshev == True:
                path_states, path, step_max, complexity_time, complexity_size = a_star(initial_state, goal_state, size, "chebyshev")
                print("\n\033[1;32mSolved using method A* with chebyshev heuristic\n\033[0;00m")

            stat_val = [['Time (ms)', round((time() - start_time) * 1000,4)],
                        ['Steps', max(1, len(path))],
                        ['Steps max', step_max],
                        ['Complexity in time', complexity_time],
                        ['Complexity in size', complexity_size]]
            
            print(tabulate(stat_val, tablefmt="pretty"))
            if len(path) <= 20:
                print('\nSteps:')
                for step_state, step_mov in zip(path_states[1:], path):
                    steps = [step_state[i:i+size] for i in range(0, len(step_state), size)]
                    print(f'Moviment: {step_mov}')
                    print(tabulate(steps, tablefmt="fancy_grid"))
                    print()
        else:
            if args.manhattan == True:
                path, step_max, complexity_time, complexity_size = ida_star(initial_state, goal_state, size, "manhattan") 
                print("\n\033[1;32mSolved using method idA* with manhattan heuristic\n\033[0;00m")
            if args.euclidean == True:
                path, step_max, complexity_time, complexity_size = ida_star(initial_state, goal_state, size, "euclidean")
                print("\n\033[1;32mSolved using method idA* with euclidean heuristic\n\033[0;00m")
            if args.misplaced == True:
                path, step_max, complexity_time, complexity_size = ida_star(initial_state, goal_state, size, "misplaced")
                print("\n\033[1;32mSolved using method idA* with misplaced heuristic\n\033[0;00m")
            if args.chebyshev == True:
                path, step_max, complexity_time, complexity_size = ida_star(initial_state, goal_state, size, "chebyshev")
                print("\n\033[1;32mSolved using method idA* with chebyshev heuristic\n\033[0;00m")

            stat_val = [['Time (ms)', round((time() - start_time) * 1000,4)],
                        ['Steps', max(1, len(path) - 2)],
                        ['Steps max', step_max],
                        ['Complexity in time', complexity_time],
                        ['Complexity in size', complexity_size]]
            print(tabulate(stat_val, tablefmt="pretty"))
            if len(path) <= 20:
                print('\nSteps:')
                for vec, mov in path[1:]:
                    steps = [vec[i:i+size] for i in range(0, len(vec), size)]
                    last_mov = mov[-1] if mov else '-'
                    print(f'Moviment: {last_mov}')
                    print(tabulate(steps, tablefmt="fancy_grid"))
                    print()

    sys.exit()
