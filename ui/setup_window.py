import tkinter as tk


class SetupWindow:
    def __init__(self):
        self.window = tk.Toplevel()

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
        print("Create Vault clicked")