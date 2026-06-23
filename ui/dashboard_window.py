import tkinter as tk
from tkinter import messagebox

from storage.vault_storage import add_credential


class DashboardWindow:
    def __init__(self):
        self.window = tk.Toplevel()

        self.window.title("VaultX Dashboard")
        self.window.geometry("900x600")

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.window,
            text="VaultX Dashboard",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        # Main container
        main_frame = tk.Frame(self.window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Left navigation panel
        nav_frame = tk.Frame(main_frame)
        nav_frame.pack(side="left", fill="y", padx=(0, 10))

        tk.Button(
            nav_frame,
            text="Add Credential",
            width=20,
            command=self.show_add_credential
        ).pack(pady=5)

        tk.Button(
            nav_frame,
            text="View Credentials",
            width=20,
            command=self.show_view_credentials
        ).pack(pady=5)

        tk.Button(
            nav_frame,
            text="Generate Password",
            width=20,
            command=self.show_generate_password
        ).pack(pady=5)

        tk.Button(
            nav_frame,
            text="Exit",
            width=20,
            command=self.window.destroy
        ).pack(pady=20)

        # Right content panel
        self.content_frame = tk.Frame(
            main_frame,
            relief="solid",
            borderwidth=1
        )
        self.content_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.show_welcome_screen()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clear_content()

        tk.Label(
            self.content_frame,
            text="Welcome to VaultX v2",
            font=("Arial", 18, "bold")
        ).pack(pady=30)

    def show_add_credential(self):
        self.clear_content()

        tk.Label(
            self.content_frame,
            text="Add Credential",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        tk.Label(
            self.content_frame,
            text="Website"
        ).pack()

        self.website_entry = tk.Entry(
            self.content_frame,
            width=40
        )
        self.website_entry.pack(pady=5)

        tk.Label(
            self.content_frame,
            text="Username"
        ).pack()

        self.username_entry = tk.Entry(
            self.content_frame,
            width=40
        )
        self.username_entry.pack(pady=5)

        tk.Label(
            self.content_frame,
            text="Password"
        ).pack()

        self.password_entry = tk.Entry(
            self.content_frame,
            width=40,
            show="*"
        )
        self.password_entry.pack(pady=5)

        tk.Button(
            self.content_frame,
            text="Save Credential",
            command=self.save_credential
        ).pack(pady=20)

    def show_view_credentials(self):
        self.clear_content()

        tk.Label(
            self.content_frame,
            text="View Credentials",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

    def show_generate_password(self):
        self.clear_content()

        tk.Label(
            self.content_frame,
            text="Generate Password",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

    def save_credential(self):
        website = self.website_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
    
        if not website or not username or not password:
            messagebox.showerror(
                "Error",
                "All fields are required."
            )
            return
    
        add_credential(
            website,
            username,
            password
        )
    
        messagebox.showinfo(
            "Success",
            "Credential saved successfully."
        )
    
        self.website_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)