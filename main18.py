import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")

        self.player_score = 0
        self.computer_score = 0

        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
        self.label.pack(pady=20)

        self.score_label = tk.Label(root, text=f"Player: {self.player_score}  Computer: {self.computer_score}", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play("Rock"), width=10)
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play("Paper"), width=10)
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play("Scissors"), width=10)
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

    def play(self, player_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(player_choice, computer_choice)

        if result == "You Win!":
            self.player_score += 1
        elif result == "You Lose!":
            self.computer_score += 1

        self.update_score()
        self.result_label.config(text=f"You chose: {player_choice}\nComputer chose: {computer_choice}\nResult: {result}")

    def determine_winner(self, player, computer):
        if player == computer:
            return "It's a Tie!"
        elif (player == "Rock" and computer == "Scissors") or \
             (player == "Scissors" and computer == "Paper") or \
             (player == "Paper" and computer == "Rock"):
            return "You Win!"
        else:
            return "You Lose!"

    def update_score(self):
        self.score_label.config(text=f"Player: {self.player_score}  Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
