import tkinter as tk
from storage.vault_storage import vault_exists
from tkinter import messagebox


class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("VaultX v2")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="VaultX v2",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=20)

        password_label = tk.Label(
            self.root,
            text="Master Password"
        )
        password_label.pack()

        self.password_entry = tk.Entry(
            self.root,
            show="*",
            width=30
        )
        self.password_entry.pack(pady=10)

        unlock_button = tk.Button(
            self.root,
            text="Unlock Vault",
            command=self.unlock_vault
        )
        unlock_button.pack(pady=10)

    def unlock_vault(self):
        if vault_exists():
            messagebox.showinfo(
                "VaultX",
                "Vault found!"
            )
        else:
            messagebox.showinfo(
                "VaultX",
                "No vault found. First-time setup required."
            )