import numpy as np
import random as rd
import tkinter as tk

choices = ("Rock", "Paper", "Scissors")
player_score = 0
cpu_score = 0
player_choice = None
cpu_choice = rd.choice(choices)

window = tk.Tk()
window.title("Rock, Paper, Scissors")
frame = tk.Frame(window)
frame.pack()

# Initialise the How to Play frame and its content
how_to_play = tk.LabelFrame(frame, text = "How to Play")
how_to_play.grid(row = 0, column = 0, padx = 10, pady = 10)
instructions = """Welcome! This application is an elementary Rock, Paper, Scissors game. Here are the rules:
    - The game shall run indefinitely, until the player chooses to quit.
    - Each round, the player must choose between one of the following options: "Rock", "Paper", or "Scissors".
    - The CPU will also automatically pick from the same list of options each round.
    - Each round, the player or the CPU wins according to the following: "Rock" beats "Scissors", "Scissors" beats "Paper" and "Paper" beats "Rock".
    - Each round, the winner gains one point, and the loser gains no points (hence will also lose no points).
Enjoy the game!"""

# Add the label for the instructions
instruction_label = tk.Label(how_to_play, text = instructions, justify = "left")
instruction_label.grid(row = 0, column = 0)

# Add an Options LabelFrame
options = tk.LabelFrame(frame, text = "Options")
options.grid(row = 1, column = 0, padx = 10, pady = 10)

# Add Play and Quit buttons
play_button = tk.Button(options, text = "Play", command = None)
play_button.grid(row = 0, column = 0)
quit_button = tk.Button(options, text = "Quit", command = None)
quit_button.grid(row = 0, column = 1)

# Add spaces between the labels and their entries
for label_frame in [how_to_play, options]:
    for widget in label_frame.winfo_children():
        widget.grid_configure(padx = 10, pady = 5)

# Make the window impossible to resize
window.resizable(False, False)

# Make the window run indefinitely until the user manually closes it.
window.mainloop()