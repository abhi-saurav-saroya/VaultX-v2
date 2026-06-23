import tkinter as tk


class DashboardWindow:
    def __init__(self):
        self.window = tk.Toplevel()

        self.window.title("VaultX Dashboard")
        self.window.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.window,
            text="VaultX Dashboard",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=20)

        add_button = tk.Button(
            self.window,
            text="Add Credential",
            width=20,
            command=self.add_credential
        )
        add_button.pack(pady=5)

        view_button = tk.Button(
            self.window,
            text="View Credentials",
            width=20,
            command=self.view_credentials
        )
        view_button.pack(pady=5)

        generate_button = tk.Button(
            self.window,
            text="Generate Password",
            width=20,
            command=self.generate_password
        )
        generate_button.pack(pady=5)

        exit_button = tk.Button(
            self.window,
            text="Exit",
            width=20,
            command=self.window.destroy
        )
        exit_button.pack(pady=20)

    def add_credential(self):
        print("Add Credential clicked")

    def view_credentials(self):
        print("View Credentials clicked")

    def generate_password(self):
        print("Generate Password clicked")