import tkinter as tk
from tkinter import messagebox
import random

# List of words for the game
WORD_LIST = [
    "PYTHON",
    "JAVA",
    "HTML",
    "CSS",
    "JAVASCRIPT",
    "RUBY",
    "PHP",
    "SWIFT",
    "KOTLIN",
    "GO",
    "CPLUSPLUS",
    "C",
    "TYPESCRIPT",
    "PERL"
]

# Dictionary of hints for each word
WORD_HINTS = {
    "PYTHON": "A widely used high-level programming language.",
    "JAVA": "A popular programming language that is used to create applications.",
    "HTML": "The standard markup language for creating web pages.",
    "CSS": "A stylesheet language used to describe the presentation of a document written in HTML.",
    "JAVASCRIPT": "A programming language that adds interactivity to your website.",
    "RUBY": "A dynamic, open source programming language with a focus on simplicity and productivity.",
    "PHP": "A widely-used open source general-purpose scripting language that is especially suited for web development.",
    "SWIFT": "A powerful and intuitive programming language for macOS, iOS, watchOS, and tvOS.",
    "KOTLIN": "A statically-typed programming language that runs on the Java Virtual Machine (JVM).",
    "GO": "An open source programming language that makes it easy to build simple, reliable, and efficient software.",
    "CPLUSPLUS": "A general-purpose programming language created as an extension of the C programming language.",
    "C": "A general-purpose, procedural computer programming language.",
    "TYPESCRIPT": "A typed superset of JavaScript that compiles to plain JavaScript.",
    "PERL": "A highly capable, feature-rich programming language with over 30 years of development."
}

# Function to pick a random word from WORD_LIST
def pick_random_word():
    return random.choice(WORD_LIST)

# Function to initialize game
def init_game():
    global chosen_word, guessed_letters, remaining_attempts

    chosen_word = pick_random_word()
    guessed_letters = set()
    remaining_attempts = 6
    update_word_display()

# Function to update the display of the word with correctly guessed letters
def update_word_display():
    displayed_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    word_label.config(text=displayed_word)

# Function to handle a letter guess
def guess_letter(event=None):
    global remaining_attempts
    letter = letter_entry.get().upper()
    letter_entry.delete(0, tk.END)

    if not letter.isalpha() or len(letter) != 1:
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    if letter in guessed_letters:
        messagebox.showinfo("Already Guessed", f"You've already guessed '{letter}'.")
        return

    guessed_letters.add(letter)

    if letter not in chosen_word:
        remaining_attempts -= 1
        update_attempts_display()

    update_word_display()
    check_game_over()

# Function to update the display of remaining attempts
def update_attempts_display():
    attempts_label.config(text=f"Remaining Attempts: {remaining_attempts}")

# Function to check if the game is over (win or lose)
def check_game_over():
    global remaining_attempts
    if all(letter in guessed_letters for letter in chosen_word):
        messagebox.showinfo("You Win!", "Congratulations! You guessed the word.")
        init_game()
    elif remaining_attempts == 0:
        messagebox.showinfo("Game Over", f"Sorry, you ran out of attempts.\nThe word was '{chosen_word}'.")
        init_game()

# Function to display a hint for the current word
def display_hint():
    if chosen_word in WORD_HINTS:
        messagebox.showinfo("Hint", WORD_HINTS[chosen_word])
    else:
        messagebox.showinfo("Hint", "No hint available for this word.")

# Initialize GUI
root = tk.Tk()
root.title("Hangman Game")

# Widgets
word_label = tk.Label(root, text="", font=("Arial", 24))
word_label.pack(pady=20)

letter_entry = tk.Entry(root, font=("Arial", 16))
letter_entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess Letter", font=("Arial", 16), command=guess_letter)
guess_button.pack(pady=10)

hint_button = tk.Button(root, text="Hint", font=("Arial", 16), command=display_hint)
hint_button.pack(pady=10)

attempts_label = tk.Label(root, text="", font=("Arial", 16))
attempts_label.pack()

# Bind Enter key to guess_letter function
root.bind('<Return>', guess_letter)

# Initialize the game
init_game()

# Start the main loop
root.mainloop()
