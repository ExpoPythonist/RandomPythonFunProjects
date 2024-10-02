import tkinter as tk
from tkinter import messagebox

def is_palindrome(s):
    # Normalize the string: remove spaces and convert to lowercase
    s = s.replace(" ", "").replace(",", "").replace("'", "").replace(".", "").lower()
    # Check if the string is the same forwards and backwards
    return s == s[::-1]

def check_palindrome():
    user_input = entry.get()
    if is_palindrome(user_input):
        messagebox.showinfo("Result", f'"{user_input}" is a palindrome!')
    else:
        messagebox.showinfo("Result", f'"{user_input}" is not a palindrome.')

# Set up the GUI
root = tk.Tk()
root.title("Palindrome Checker")

# Input label
label = tk.Label(root, text="Enter a string:")
label.pack(pady=10)

# Entry field
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Check button
check_button = tk.Button(root, text="Check", command=check_palindrome, font=("Arial", 14))
check_button.pack(pady=20)

# Run the application
root.mainloop()
