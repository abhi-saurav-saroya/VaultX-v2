import tkinter as tk
from tkinter import messagebox
from storage.vault_storage import save_new_vault
from ui.dashboard_window import DashboardWindow
from security.hashing import hash_password


class SetupWindow:
    def __init__(self, login_window):
        self.login_window = login_window

        self.window = tk.Toplevel()

        self.window.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )

        self.window.title("VaultX Setup")
        self.window.geometry("500x300")
        self.window.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.window,
            text="VaultX v2 Setup",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=20)

        password_label = tk.Label(
            self.window,
            text="Create Master Password"
        )
        password_label.pack()

        self.password_entry = tk.Entry(
            self.window,
            show="*",
            width=30
        )
        self.password_entry.pack(pady=5)

        confirm_label = tk.Label(
            self.window,
            text="Confirm Master Password"
        )
        confirm_label.pack()

        self.confirm_entry = tk.Entry(
            self.window,
            show="*",
            width=30
        )
        self.confirm_entry.pack(pady=5)

        create_button = tk.Button(
            self.window,
            text="Create Vault",
            command=self.create_vault
        )
        create_button.pack(pady=20)

    def create_vault(self):
        password = self.password_entry.get()
        confirm_password = self.confirm_entry.get()

        if password != confirm_password:
            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return
        
        if not password:
            messagebox.showerror(
                "Error",
                "Password cannot be empty."
            )
            return

        hashed_password = hash_password(password)
        save_new_vault(hashed_password)

        messagebox.showinfo(
            "Success",
            "Vault created successfully!"
        )

        self.window.destroy()
        DashboardWindow()
        

    def on_close(self):
        self.login_window.deiconify()
        self.window.destroy()