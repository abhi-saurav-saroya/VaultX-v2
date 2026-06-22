import tkinter as tk
from storage.vault_storage import vault_exists, load_vault
from tkinter import messagebox
from ui.setup_window import SetupWindow
from ui.dashboard_window import DashboardWindow
from security.hashing import hash_password


class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("VaultX v2")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        self.attempts_left = 3

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
            vault = load_vault()

            stored_hash = vault["master_password_hash"]

            entered_hash = hash_password(self.password_entry.get())

            if entered_hash == stored_hash:
                self.root.withdraw()
                DashboardWindow()

            else:
                self.attempts_left -= 1

                if self.attempts_left > 0:
                    messagebox.showerror(
                        "VaultX",
                        f"Wrong password. {self.attempts_left} attempts remaining."
                    )
                else:
                    messagebox.showerror(
                        "VaultX",
                        "Access denied."
                    )
        else:
            messagebox.showinfo(
                "VaultX",
                "No vault found. First-time setup required."
            )
            self.root.withdraw()
            SetupWindow(self.root)