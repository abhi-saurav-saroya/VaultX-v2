import tkinter as tk
from tkinter import messagebox

from storage.vault_storage import add_credential, get_credentials
from security.encryption import decrypt_text


BUTTON_WIDTH = 20
ENTRY_WIDTH = 40

TITLE_FONT = ("Arial", 20, "bold")
HEADING_FONT = ("Arial", 16, "bold")


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
            font=TITLE_FONT
        )
        title.pack(pady=10)

        # Main container
        main_frame = tk.Frame(self.window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Left navigation panel
        nav_frame = tk.Frame(main_frame)
        nav_frame.pack(side="left", fill="y", padx=(0, 10))

        navigation_buttons = [
            ("Add Credential", self.show_add_credential),
            ("View Credentials", self.show_view_credentials),
            ("Generate Password", self.show_generate_password),
        ]
        
        for text, command in navigation_buttons:
            self.create_button(nav_frame, text, command)

        self.create_button(
            nav_frame,
            "Exit",
            self.window.destroy,
            pady=20
        )

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

    def create_label(self, parent, text, font=None, pady=0):
        label = tk.Label(
            parent,
            text=text,
            font=font
        )
        label.pack(pady=pady)

        return label


    def create_entry(self, parent, show=None):
        entry = tk.Entry(
            parent,
            width=ENTRY_WIDTH,
            show=show
        )
        entry.pack(pady=5)

        return entry


    def create_button(self, parent, text, command, pady=5):
        button = tk.Button(
            parent,
            text=text,
            width=BUTTON_WIDTH,
            command=command
        )
        button.pack(pady=pady)

        return button

    def show_welcome_screen(self):
        self.clear_content()

        self.create_label(
            self.content_frame,
            "Welcome to VaultX v2",
            TITLE_FONT,
            pady=30
        )

    def show_add_credential(self):
        self.clear_content()

        self.create_label(
            self.content_frame,
            "Add Credential",
            HEADING_FONT,
            pady=20
        )

        self.create_label(
            self.content_frame,
            "Website"
        )

        self.website_entry = self.create_entry(
            self.content_frame
        )

        self.create_label(
            self.content_frame,
            "Username"
        )

        self.username_entry = self.create_entry(
            self.content_frame
        )

        self.create_label(
            self.content_frame,
            "Password"
        )

        self.password_entry = self.create_entry(
            self.content_frame,
            show="*"
        )

        self.create_button(
            self.content_frame,
            "Save Credential",
            self.save_credential,
            pady=20
        )

    def show_view_credentials(self):
        self.clear_content()

        self.create_label(
            self.content_frame,
            "Stored Credentials",
            HEADING_FONT,
            pady=10
        )

        credentials = get_credentials()

        if not credentials:
            self.create_label(
                self.content_frame,
                "No credentials stored.",
                pady=20
            )
            return

        for credential in credentials:
            self.create_credential_row(credential)

    def show_generate_password(self):
        self.clear_content()

        self.create_label(
            self.content_frame,
            "Generate Password",
            HEADING_FONT,
            pady=20
        )

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

    def toggle_password(self, credential, password_label, button):
        if button["text"] == "Reveal":
            decrypted_password = decrypt_text(credential["password"])

            password_label.config(
                text=decrypted_password
            )

            button.config(
                text="Hide"
            )

        else:
            password_label.config(
                text="********"
            )

            button.config(
                text="Reveal"
            )

    def create_credential_row(self, credential):
        row_frame = tk.Frame(self.content_frame)
        row_frame.pack(fill="x", padx=10, pady=5)
    
        tk.Label(
            row_frame,
            text=credential["website"],
            width=BUTTON_WIDTH,
            anchor="w"
        ).pack(side="left")
    
        tk.Label(
            row_frame,
            text=credential["username"],
            width=BUTTON_WIDTH,
            anchor="w"
        ).pack(side="left")
    
        password_label = tk.Label(
            row_frame,
            text="********",
            width=BUTTON_WIDTH,
            anchor="w"
        )
        password_label.pack(side="left")
    
        reveal_button = tk.Button(
            row_frame,
            text="Reveal",
            command=lambda: self.toggle_password(
                credential,
                password_label,
                reveal_button
            )
        )
        reveal_button.pack(side="left")