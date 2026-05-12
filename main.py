# Create a Rock Paper Scissor Game using the random module and Python functions, loops, conditional statements, and Tkinter.

import tkinter as tk
from tkinter import messagebox
import random as r




# window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("600x300")
root.mainloop()

# image import
rockimage = tk.PhotoImage(file = "rock.png")
# paperimage = tk.PhotoImage(root, file = "paper.png")
# scissorsimage = tk.PhotoImage(root, file = "scissors.png")

# buttons
rock_b = tk.Button(root, image = rockimage, text = "rock", height = 50, width = 50, command = outcome_r)
rock_b.pack()
# paper_b = tk.Button(root, image = "paper", height = 50, width = 50, command = outcome_p)
# scissors_b = tk.Button(root, image = "scissors", height = 50, width = 50, command = outcome_s)

# button placement
#rock_b.grid(row = 1, column = 1)
# paper_b.grid(root, row = 1, column = 2)
# scissors_b.grid(root, row = 1, column = 3)


def outcome_r(random):
    random = r.randint(1, 3)
    rockwindow = tk.Toplevel()
    rockwindow.title("Outcome")
    rock_o = tk.Label(rockwindow, text = f"{rock}")
    rock_o.pack()
    rockwindow.mainloop()
    rock = ""
    if random == 1:
        rock = "The computer chooses rock; Tie"
    if random == 2:
        rock = "The computer chooses paper; Lose"
    else:
        rock = "The computer chooses scissors; Win"