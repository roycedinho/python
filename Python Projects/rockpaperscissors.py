import random
from tkinter import *

# Create main window
root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.config(bg="lightblue")

# List of possible choices
choices = ["Rock", "Paper", "Scissors"]

# Function to play the game
def play(user_choice):
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    lbl_result.config(text=f"Computer chose: {computer_choice}\n{result}")

# Title label
lbl_title = Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="lightblue")
lbl_title.pack(pady=10)

# Result label
lbl_result = Label(root, text="", font=("Arial", 14), bg="lightblue")
lbl_result.pack(pady=20)

# Frame to hold buttons
frame = Frame(root, bg="lightblue")
frame.pack(pady=10)

# Buttons for Rock, Paper, Scissors
btn_rock = Button(frame, text="Rock", width=10, font=("Arial", 12), command=lambda: play("Rock"))
btn_paper = Button(frame, text="Paper", width=10, font=("Arial", 12), command=lambda: play("Paper"))
btn_scissors = Button(frame, text="Scissors", width=10, font=("Arial", 12), command=lambda: play("Scissors"))

btn_rock.grid(row=0, column=0, padx=10)
btn_paper.grid(row=0, column=1, padx=10)
btn_scissors.grid(row=0, column=2, padx=10)

# Start the GUI loop
root.mainloop()
