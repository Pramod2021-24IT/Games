import tkinter as tk 
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"  
        self.board = [ ["" for _ in range(3)] for _ in range(3) ]  
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.buttons = []  
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=20, height=10, 
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
        
    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player) 

            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.destroy()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.destroy()

            self.current_player = "O" if self.current_player == "X" else "X" 

    def check_winner(self, player):
        # Check rows
        for i in range(3): 
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True

        # Check columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False  

    def is_board_full(self):
        for row in self.board:
            for cell in row: 
                if cell == "":
                    return False
        return True

    def run(self):
        self.window.mainloop()

# Game Execution
if __name__ == "__main__": 
    game = TicTacToe()
    game.run()

