from cryptography.fernet import Fernet
from pathlib import Path


KEY_FILE = Path("data/secret.key")


def generate_key():
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)


def load_key():
    with open(KEY_FILE, "rb") as file:
        return file.read()


def encrypt_text(text):
    key = load_key()

    cipher = Fernet(key)

    encrypted_text = cipher.encrypt(
        text.encode()
    )

    return encrypted_text.decode()


def decrypt_text(encrypted_text):
    key = load_key()

    cipher = Fernet(key)

    decrypted_text = cipher.decrypt(
        encrypted_text.encode()
    )

    return decrypted_text.decode()