from pathlib import Path
import json


VAULT_FILE = Path("data/vault.json")


def vault_exists():
    return VAULT_FILE.exists()


def save_new_vault(master_password):
    vault_data = {
        "master_password_hash": master_password,
        "credentials": []
    }

    with open(VAULT_FILE, "w") as file:
        json.dump(vault_data, file, indent=4)

    
def load_vault():
    with open(VAULT_FILE, "r") as file:
        return json.load(file)
    

def add_credential(website, username, password):
    vault = load_vault()

    credential = {
        "website": website,
        "username": username,
        "password": password
    }

    vault["credentials"].append(credential)

    with open(VAULT_FILE, "w") as file:
        json.dump(vault, file, indent=4)