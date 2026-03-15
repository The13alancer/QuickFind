import re


class ContactManager:
    def __init__(self, contacts=None):
        self.contacts = contacts if contacts is not None else {}

    def add_contact(self, name, phone, email):
        name = name.strip()
        if not name:
            return False, "Name cannot be empty."

        if name in self.contacts:
            return False, "Contact already exists."

        if not self._is_valid_phone(phone):
            return False, "Invalid phone number format."

        if not self._is_valid_email(email):
            return False, "Invalid email format."

        self.contacts[name] = {
            "phone": phone.strip(),
            "email": email.strip()
        }
        return True, f"Contact '{name}' added successfully."

    def search_contact(self, name):
        name = name.strip()
        return self.contacts.get(name)

    def update_contact(self, name, new_phone=None, new_email=None):
        name = name.strip()
        if name not in self.contacts:
            return False, "Contact not found."

        if new_phone:
            if not self._is_valid_phone(new_phone):
                return False, "Invalid phone number format."
            self.contacts[name]["phone"] = new_phone.strip()

        if new_email:
            if not self._is_valid_email(new_email):
                return False, "Invalid email format."
            self.contacts[name]["email"] = new_email.strip()

        return True, f"Contact '{name}' updated successfully."

    def delete_contact(self, name):
        name = name.strip()
        if name not in self.contacts:
            return False, "Contact not found."

        del self.contacts[name]
        return True, f"Contact '{name}' deleted successfully."

    def list_contacts(self):
        return dict(sorted(self.contacts.items()))

    def search_by_partial_name(self, query):
        query = query.strip().lower()
        results = {}

        for name, info in self.contacts.items():
            if query in name.lower():
                results[name] = info

        return dict(sorted(results.items()))

    @staticmethod
    def _is_valid_email(email):
        email = email.strip()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None

    @staticmethod
    def _is_valid_phone(phone):
        phone = phone.strip()
        pattern = r"^[0-9+\-\(\) ]{7,20}$"
        return re.match(pattern, phone) is not None
