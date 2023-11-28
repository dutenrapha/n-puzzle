import sys
import argparse
import pandas as pd
from time import time
import tkinter as tk
import random
from puzzle import a_star_puzzle


class NPuzzle:
    def __init__(self, master, size=3):
        self.master = master
        self.size = size
        self.buttons = []
        self.blank_position = (size - 1, size - 1)

        self.shuffle_puzzle()
        self.create_widgets()

    def create_widgets(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                number = self.puzzle[i][j]
                button = tk.Button(self.master, text='' if number == self.size ** 2 else str(number),
                                   command=lambda x=i, y=j: self.move_tile(x, y), 
                                   width=10, height=3)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def shuffle_puzzle(self):
        numbers = list(range(1, self.size ** 2 + 1))
        random.shuffle(numbers)
        self.puzzle = [numbers[i:i + self.size] for i in range(0, len(numbers), self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == self.size ** 2:
                    self.blank_position = (i, j)

    def move_tile(self, x, y):
        if self.is_adjacent((x, y), self.blank_position):
            self.swap_positions((x, y), self.blank_position)
            self.update_buttons()
            if self.is_solved():
                print("Puzzle Solved!")

    def is_adjacent(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1

    def swap_positions(self, pos1, pos2):
        self.puzzle[pos1[0]][pos1[1]], self.puzzle[pos2[0]][pos2[1]] = self.puzzle[pos2[0]][pos2[1]], self.puzzle[pos1[0]][pos1[1]]
        self.blank_position = pos1

    def update_buttons(self):
        for i in range(self.size):
            for j in range(self.size):
                number = self.puzzle[i][j]
                self.buttons[i][j].config(text='' if number == self.size ** 2 else str(number))

    def is_solved(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] != i * self.size + j + 1:
                    return False
        return True

def buttons_2_list(btn):
    final_lst = []
    for row in btn:
        lst = []
        for col in row:
            val = col.cget("text")
            if val == '':
                lst.append(0)
            else:
                lst.append(int(val))
        final_lst.append(lst)
    return final_lst




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

    for i, number1 in enumerate(flatten_state):
        for number2 in flatten_state[i+1:]:
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
    initial_state = [initial_state[i:i+size] for i in range(0, len(initial_state), size)] # group in sublist
    
    goal_state = list(range(1, size**2 - 1 + 1))
    goal_state.append(0) # insert last element
    goal_state = [goal_state[i:i+size] for i in range(0, len(goal_state), size)] # group in sublist
    

    # check if has solution
    initial_invertions = count_inversions(initial_state)
    goal_invertions = count_inversions(goal_state)
    if initial_invertions % 2 != goal_invertions % 2:
        print('\033[0;31mError: No solution.\033[0;00m')
        sys.exit()


    #print(args.astar)
    if args.astar:
        print('initial_state:', initial_state)
        print('goal_state:', goal_state)
        start_time = time()
        path = a_star_puzzle(initial_state, goal_state, size) 
        print('A* Time:', (time() - start_time) * 1000, 'ms')
        print(f'Steps: {len(path)}')
        if len(path) <= 20:
            [print(step) for step in path]

    sys.exit()



    root = tk.Tk()
    root.title("N-Puzzle Game")
    N = 3
    game = NPuzzle(root, N)
    initial_state = buttons_2_list(game.buttons)
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    path = a_star_puzzle(initial_state, goal_state, N)
    #print(line.path)
    #for step in path:
    #    for row in step:
    #        print(row)
        #print()

    root.mainloop()

