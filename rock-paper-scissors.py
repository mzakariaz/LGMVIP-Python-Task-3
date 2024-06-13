import random as rd
import tkinter as tk
import textwrap as tw

window = tk.Tk()
window.title("Rock, Paper, Scissors")
frame = tk.Frame(window)
frame.pack()

choices = ("Rock", "Paper", "Scissors")
round = 1
player_score = 0
cpu_score = 0
cpu_choice = rd.choice(choices)
player_choice = None

# Initialise the How to Play frame and its content
how_to_play = tk.LabelFrame(frame, text = "How to Play")
how_to_play.grid(row = 0, column = 0, padx = 10, pady = 10)
instructions = """Welcome! This application is an elementary Rock, Paper, Scissors game. Here are the rules:
    - The game shall run indefinitely, until the player chooses to quit.
    - Each round, the player must choose between one of the following menu: "Rock", "Paper", or "Scissors".
    - The player is up against the CPU, which will be the opponent.
    - The CPU will also automatically pick from the same list of menu each round.
    - Each round, the player or the CPU wins according to the following: "Rock" beats "Scissors", "Scissors" beats "Paper" and "Paper" beats "Rock".
    - Each round, the winner gains one point, and the loser gains no points (hence will also lose no points).
Enjoy the game!"""

# Add the label for the instructions
instruction_label = tk.Label(how_to_play, text = instructions, justify = "left")
instruction_label.grid(row = 0, column = 0)

# Add an Menu LabelFrame
menu = tk.LabelFrame(frame, text = "Menu")
menu.grid(row = 1, column = 0, padx = 10, pady = 10)

# Define play and quit functions
def quit():
    window.destroy()

def play():
    def next_round():
        global round
        global player_choice
        global cpu_choice
        global player_score
        global cpu_score
        player_choice = selected_option.get()
        if player_choice in choices:
            round += 1
            win = bool(((player_choice, cpu_choice) in [("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Paper")]))
            lose = bool(((player_choice, cpu_choice) in [("Scissors", "Rock"), ("Rock", "Paper"), ("Paper", "Scissors")]))
            if win:
                player_score += 1
                game_progress.config(text = f"Round {round}")
                player_score_label.config(text = f"Your score: {player_score}")
                opponent_score_label.config(text = f"Opponent's score: {cpu_score}")
                win_text = f"Congratulations! You've won this round! Your opponent picked {cpu_choice} and you picked {player_choice}. Well done!"
                win_label = tw.fill(win_text, width = 50, subsequent_indent = '\n')
                update_notice.config(text = win_label)
                cpu_choice = rd.choice(choices)
            elif lose:
                cpu_score += 1
                game_progress.config(text = f"Round {round}")
                player_score_label.config(text = f"Your score: {player_score}")
                opponent_score_label.config(text = f"Opponent's score: {cpu_score}")
                lose_text = f"Bad luck! You've lost this round! Your opponent picked {cpu_choice} and you picked {player_choice}. Better luck next time!"
                lose_label = tw.fill(lose_text, width = 50, subsequent_indent = '\n')
                update_notice.config(text = lose_label)
                cpu_choice = rd.choice(choices)
            elif not(player_choice is None):
                game_progress.config(text = f"Round {round}")
                player_score_label.config(text = f"Your score: {player_score}")
                opponent_score_label.config(text = f"Opponent's score: {cpu_score}")
                draw_text = f"Great timing! This round is a draw! You and your opponent both picked {player_choice}. Keep going!"
                draw_label = tw.fill(draw_text, width = 50, subsequent_indent = '\n')
                update_notice.config(text = draw_label)
                cpu_choice = rd.choice(choices)
            else:
                pass
        else:
            pass
    new_window = tk.Tk()
    new_window.title("Game")
    new_frame = tk.Frame(new_window)
    new_frame.pack()
    option_selection = tk.LabelFrame(new_frame, text = "Object Selection")
    option_selection.pack()
    option_selection.grid(row = 0, column = 0)
    option_label = tk.Label(option_selection, text = "Select your object:")
    option_label.grid(row = 0, column = 0)
    selected_option = tk.StringVar(option_selection)
    option_list = tk.OptionMenu(option_selection, selected_option, *list(choices))
    option_list.grid(row = 0, column = 1)
    submit_label = tk.Label(option_selection, text = "Submit your selection:")
    submit_label.grid(row = 1, column = 0)
    submit_button = tk.Button(option_selection, text = "Submit", command = next_round)
    submit_button.grid(row = 1, column = 1)
    game_progress = tk.LabelFrame(new_frame, text = f"Round {round}")
    game_progress.grid(row = 1, column = 0)
    player_score_label = tk.Label(game_progress, text = f"Your score: {player_score}")
    player_score_label.grid(row = 0, column = 0)
    opponent_score_label = tk.Label(game_progress, text = f"Opponent's score: {cpu_score}")
    opponent_score_label.grid(row = 0, column = 1)
    update = tk.LabelFrame(new_frame, text = "Latest Update")
    update.grid(row = 2, column = 0)
    update_notice = tk.Label(update, text = f"The game has now begun. Good luck!")
    update_notice.grid(row = 1, column = 0)
    for label_frame in [option_selection, game_progress, update]:
        label_frame.grid_configure(pady = 15)
        for widget in label_frame.winfo_children():
            widget.grid_configure(padx = 10, pady = 5)
    new_window.resizable(False, False)
    new_window.geometry("400x400")
    new_window.mainloop()



# Add Play and Quit buttons
play_button = tk.Button(menu, text = "Play", command = play)
play_button.grid(row = 0, column = 0)
quit_button = tk.Button(menu, text = "Quit", command = quit)
quit_button.grid(row = 0, column = 1)

# Add spaces between the labels and their entries
for label_frame in [how_to_play, menu]:
    for widget in label_frame.winfo_children():
        widget.grid_configure(padx = 10, pady = 5)

# Make the window impossible to resize
window.resizable(False, False)

# Make the window run indefinitely until the user manually closes it.
window.geometry("800x300")
window.mainloop()