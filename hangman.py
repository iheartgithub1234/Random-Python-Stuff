import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.words = [
            "pizza", "burger", "sushi", "taco", "pasta", "salad", "ramen", "curry",
            "noodle", "sandwich", "kebab", "chicken", "steak", "hotdog", "popcorn",
            "fries", "potato", "carrot", "broccoli", "spinach", "tomato", "cucumber",
            "avocado", "banana", "orange", "apple", "pear", "watermelon", "strawberry",
            "blueberry", "raspberry", "grape", "pineapple", "peach", "mango", "kiwi",
            "grapefruit", "lemon", "lime", "pomegranate", "pepperoni", "bacon", "sausage",
            "pancake", "waffle", "fajita", "enchilada", "quesadilla", "guacamole", "hummus",
            "salsa", "yogurt", "cheese", "icecream", "chocolate", "cookie", "cake", "brownie",
            "pudding", "jelly", "popcorn", "candy", "hot sauce", "ketchup", "mayonnaise",
            "mustard", "ranch dressing", "barbecue sauce", "honey mustard", "caesar dressing",
            "italian dressing", "tartar sauce", "syrup", "honey",
            "peanut butter", "jelly", "jam", "marshmallow", "caramel", "butterscotch", "whipped cream",
            "cherry", "apple juice", "orange juice", "cranberry juice", "pineapple juice", "grape juice",
            "lemonade", "iced tea", "milk", "chocolate milk", "smoothie", "coffee", "tea"
        ]

        self.word = random.choice(self.words)
        self.guesses = []
        self.remaining_guesses = 10
        self.output = "_ " * len(self.word)

        self.guessed_letters_label = tk.Label(root, text="Guessed letters:")
        self.guessed_letters_label.pack()

        self.guesses_left_label = tk.Label(root, text=f"Guesses left: {self.remaining_guesses}")
        self.guesses_left_label.pack()

        self.word_to_guess_label = tk.Label(root, text=self.output)
        self.word_to_guess_label.pack()

        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack()
        self.guess_entry.bind("<Return>", self.make_guess)

        self.update_labels()

    def make_guess(self, event=None):
        guess = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1:
            messagebox.showinfo("Invalid Guess", "Please enter a single letter.")
            return

        if guess in self.guesses:
            messagebox.showinfo("Invalid Guess", f'You already guessed "{guess}". Please try a different letter.')
            return

        self.guesses.append(guess)

        if guess in self.word:
            new_output = ""
            for letter in self.word:
                if letter in self.guesses:
                    new_output += letter + " "
                else:
                    new_output += "_ "
            self.output = new_output
            self.update_labels()

            if "_" not in self.output:
                messagebox.showinfo("Congratulations", f"Congratulations! You won! The word was {self.word}.")
                self.root.quit()

        else:
            self.remaining_guesses -= 1
            self.update_labels()

            if self.remaining_guesses == 0:
                messagebox.showinfo("Game Over", f"Game over. The word was {self.word}.")
                self.root.quit()

    def update_labels(self):
        self.guesses_left_label.config(text=f"Guesses left: {self.remaining_guesses}")
        self.word_to_guess_label.config(text=self.output)
        self.guessed_letters_label.config(text=f"Guessed letters: {' '.join(self.guesses)}")


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
