from pathlib import Path


VAULT_FILE = Path("data/vault.json")


def vault_exists():
    return VAULT_FILE.exists()