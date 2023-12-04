import sys
import argparse

from time import time

from puzzle import a_star, ida_star



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



def count_inversions(state):
    flatten_state = [number for line in state for number in line if number != 0]
    numbinversions = 0

    for i, number1 in enumerate(state):
        for number2 in state[i+1:]:
            if number1 > number2:
                numbinversions += 1

    return numbinversions



if __name__ == "__main__":
    #global initial_state, goal_state, size
    parser = argparse.ArgumentParser(prog='N-Puzzle', description='The goal of this project is to programmatically solve the N-puzzle.', epilog='Solve it better than brut force!')
    parser.add_argument('filename', type=argparse.FileType("r"))
    parser.add_argument('-astar', action='store_true')
    args = parser.parse_args()

    with args.filename as file:
        data = [line.strip().split("#")[0].strip() for line in file] # erase comments
    data = list(filter(lambda x: x != '', data)) # remove empty lines of list
    #print(data)

    size = int(data.pop(0)) if data else None
    data = ' '.join(data).split()
    #REM verificar se o data esta vazio? ou se o size nao existe?

    if parser_board(data, size) != 'continue':
        print(parser_board(data, size))
        sys.exit()

    #print(data)
    initial_state = [int(value) for value in data] # Convert into int list
    # initial_state = [initial_state[i:i+size] for i in range(0, len(initial_state), size)] # group in sublist
    
    goal_state = list(range(1, size**2 - 1 + 1))
    goal_state.append(0) # insert last element
    # goal_state = [goal_state[i:i+size] for i in range(0, len(goal_state), size)] # group in sublist
    

    # check if has solution
    # initial_invertions = count_inversions(initial_state)
    # goal_invertions = count_inversions(goal_state)
    # if initial_invertions % 2 != goal_invertions % 2:
    #     print('\033[0;31mError: No solution.\033[0;00m')
    #     sys.exit()


    #print(args.astar)
    if args.astar:
        print('initial_state:', initial_state)
        print('goal_state:', goal_state)
        start_time = time()
        if size == 3:
            path = a_star(initial_state, goal_state, size) 
        else:
            path = ida_star(initial_state, goal_state, size) 
        print('A* Time:', (time() - start_time) * 1000, 'ms')
        print(f'Steps: {len(path)}')
        if len(path) <= 20:
            [print(step) for step in path]

    sys.exit()



    # root = tk.Tk()
    # root.title("N-Puzzle Game")
    # N = 3
    # game = NPuzzle(root, N)
    # initial_state = buttons_2_list(game.buttons)
    # goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    # path = a_star_puzzle(initial_state, goal_state, N)
    #print(line.path)
    #for step in path:
    #    for row in step:
    #        print(row)
        #print()

    root.mainloop()

