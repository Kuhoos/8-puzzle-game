# %%
import tkinter as tk
import random

class EightPuzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("8 Puzzle Game")

        self.board = list(range(9))  # 0 represents empty space
        self.buttons = []
        self.moves = 0

        self.shuffle_board()

        self.frame = tk.Frame(root)
        self.frame.pack()

        for i in range(9):
            button = tk.Button(self.frame, text="", font=("Arial", 20),
                               width=4, height=2,
                               command=lambda i=i: self.move_tile(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.update_board()

        self.move_label = tk.Label(root, text="Moves: 0", font=("Arial", 12))
        self.move_label.pack()

        shuffle_btn = tk.Button(root, text="Shuffle", command=self.reset_game)
        shuffle_btn.pack(pady=5)

    def shuffle_board(self):
        random.shuffle(self.board)

    def update_board(self):
        for i in range(9):
            value = self.board[i]
            self.buttons[i]["text"] = "" if value == 0 else str(value)

    def move_tile(self, index):
        empty = self.board.index(0)

        if self.is_adjacent(index, empty):
            self.board[empty], self.board[index] = self.board[index], self.board[empty]
            self.moves += 1
            self.move_label.config(text=f"Moves: {self.moves}")
            self.update_board()

            if self.board == list(range(1,9)) + [0]:
                self.win_message()

    def is_adjacent(self, i, j):
        return (abs(i-j) == 1 and i//3 == j//3) or abs(i-j) == 3

    def win_message(self):
        win = tk.Toplevel(self.root)
        win.title("You Win!")
        tk.Label(win, text=f"Congratulations!\nSolved in {self.moves} moves.",
                 font=("Arial", 14)).pack(padx=20, pady=20)

    def reset_game(self):
        self.moves = 0
        self.move_label.config(text="Moves: 0")
        self.shuffle_board()
        self.update_board()


root = tk.Tk()
game = EightPuzzle(root)
root.mainloop()

# %%



