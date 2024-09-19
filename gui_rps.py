import tkinter as tk
from tkinter import messagebox
import random


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "win"
    else:
        return "lose"


def on_button_click(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    # Update GUI with results
    choices_label.config(
        text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}"
    )
    if result == "win":
        result_label.config(text="You win!", fg="green")
    elif result == "lose":
        result_label.config(text="You lose!", fg="red")
    else:
        result_label.config(text="It's a tie!", fg="blue")


def reset_game():
    choices_label.config(text="Make your choice:")
    result_label.config(text="")


# Main GUI setup
def main():
    global choices_label, result_label

    root = tk.Tk()
    root.title("Rock-Paper-Scissors Game")

    # Set window size
    root.geometry("300x300")

    # Create title label
    title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # Instructions
    instructions_label = tk.Label(
        root, text="Choose Rock, Paper, or Scissors", font=("Arial", 12)
    )
    instructions_label.pack(pady=5)

    # Buttons for user choices
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    tk.Button(
        button_frame, text="Rock", width=10, command=lambda: on_button_click("rock")
    ).pack(side=tk.LEFT, padx=5)
    tk.Button(
        button_frame, text="Paper", width=10, command=lambda: on_button_click("paper")
    ).pack(side=tk.LEFT, padx=5)
    tk.Button(
        button_frame,
        text="Scissors",
        width=10,
        command=lambda: on_button_click("scissors"),
    ).pack(side=tk.LEFT, padx=5)

    # Labels to display choices and result
    choices_label = tk.Label(root, text="Make your choice:", font=("Arial", 12))
    choices_label.pack(pady=10)

    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.pack(pady=10)

    # Reset button
    reset_button = tk.Button(root, text="Play Again", command=reset_game)
    reset_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
