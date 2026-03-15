import json
import os


def load_contacts(filename="contacts.json"):
    if not os.path.exists(filename):
        return {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            return {}
    except (json.JSONDecodeError, OSError):
        return {}


def save_contacts(contacts, filename="contacts.json"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(contacts, file, indent=4)
        return True
    except OSError:
        return False
