import tkinter as tk
import random

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
                print("Puzzle resolvido!")

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

def main():
    root = tk.Tk()
    root.title("N-Puzzle Game")
    game = NPuzzle(root, 3)
    root.mainloop()

if __name__ == "__main__":
    main()