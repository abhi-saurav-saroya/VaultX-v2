import tkinter as tk


class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("VaultX v2")
        self.root.geometry("500x300")

        title = tk.Label(
            self.root,
            text="VaultX v2",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=50)

        self.root.mainloop()