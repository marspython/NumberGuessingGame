import random
import tkinter as tk
from tkinter import messagebox


class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guess")  # Set the window title

        # Initialize game variables
        self.secret_number = random.randint(1, 100)  # Generate a random number
        self.max_tries = 5  # Maximum number of tries per round
        self.tries = 0  # Number of tries in the current round
        self.score = 0  # Player's score

        # Create a label widget to display instructions
        self.label = tk.Label(master, text="I'm thinking of a number between 1 and 100.")
        self.label.pack()  # Display the label

        # Create an entry widget for the player's guesses
        self.entry = tk.Entry(master)
        self.entry.pack()  # Display the entry field

        # Create a button for the player to submit their guess
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()  # Display the button

    def check_guess(self):
        try:
            guess = int(self.entry.get())  # Get the player's guess from the entry field
        except ValueError:
            # Display an error message for invalid input
            messagebox.showerror("Error", "Invalid input. Please enter a number.")
            self.entry.delete(0, tk.END)  # Clear the entry field
            return

        self.tries += 1  # Increment the number of attempts

        if guess < self.secret_number:
            result = "Higher! Try again."
        elif guess > self.secret_number:
            result = "Lower! Try again."
        else:
            result = f"Congratulations! You guessed the number {self.secret_number} in {self.tries} attempts."
            self.score += self.max_tries - self.tries  # Update the score
            self.label.config(text=f"Your current score: {self.score}")  # Update the score display
            self.tries = 0  # Reset the number of tries
            self.secret_number = random.randint(1, 100)  # Generate a new random number

        if self.tries == self.max_tries:
            result = f"Sorry, you've run out of tries. The secret number was {self.secret_number}."
            self.tries = 0  # Reset the number of tries
            self.secret_number = random.randint(1, 100)  # Generate a new random number

        # Display the result message in a message box
        messagebox.showinfo("Result", result)
        self.entry.delete(0, tk.END)  # Clear the entry field


if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    game = NumberGuessingGame(root)  # Instantiate the game
    root.mainloop()  # Start the Tkinter main loop
