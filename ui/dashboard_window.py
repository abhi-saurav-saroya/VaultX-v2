import tkinter as tk


class DashboardWindow:
    def __init__(self):
        self.window = tk.Toplevel()

        self.window.title("VaultX Dashboard")
        self.window.geometry("700x500")

        title = tk.Label(
            self.window,
            text="VaultX Dashboard",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=20)