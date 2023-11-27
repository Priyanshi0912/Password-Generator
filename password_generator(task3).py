import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.label_username = ttk.Label(master, text="Username:")
        self.label_username.grid(row=0, column=0, padx=20, pady=20, sticky="E")

        self.entry_username = ttk.Entry(master)
        self.entry_username.grid(row=0, column=1, padx=20, pady=20, sticky="W")

        self.label_length = ttk.Label(master, text="Password Length:")
        self.label_length.grid(row=1, column=0, padx=10, pady=10, sticky="E")

        self.entry_length = ttk.Entry(master)
        self.entry_length.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        self.label_password = ttk.Label(master, text="Generated Password:")
        self.label_password.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.button_generate = ttk.Button(master, text="Generate Password", command=self.generate_password)
        self.button_generate.grid(row=3, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            username = self.entry_username.get()
            length = int(self.entry_length.get())
            if length <= 0:
                raise ValueError("Length should be a positive integer.")

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))

            self.label_password.config(text=f"Generated Password for {username}: {password}")

        except ValueError as e:
            self.label_password.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
