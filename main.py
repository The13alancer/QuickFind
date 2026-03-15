from contact_manager import ContactManager
from storage import load_contacts, save_contacts


def display_menu():
    print("\n=== QuickFind Contact Manager ===")
    print("1. Add Contact")
    print("2. Search Contact by Exact Name")
    print("3. Search Contact by Partial Name")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. List All Contacts")
    print("7. Exit")


def print_contact(name, info):
    print(f"\nName : {name}")
    print(f"Phone: {info['phone']}")
    print(f"Email: {info['email']}")


def main():
    contacts = load_contacts()
    manager = ContactManager(contacts)

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")

            success, message = manager.add_contact(name, phone, email)
            print(message)

            if success:
                save_contacts(manager.contacts)

        elif choice == "2":
            name = input("Enter exact name to search: ")
            contact = manager.search_contact(name)

            if contact:
                print_contact(name, contact)
            else:
                print("Contact not found.")

        elif choice == "3":
            query = input("Enter part of the name to search: ")
            results = manager.search_by_partial_name(query)

            if results:
                print("\nMatching Contacts:")
                for name, info in results.items():
                    print_contact(name, info)
            else:
                print("No matching contacts found.")

        elif choice == "4":
            name = input("Enter contact name to update: ")
            print("Leave a field blank if you do not want to change it.")
            new_phone = input("Enter new phone: ").strip()
            new_email = input("Enter new email: ").strip()

            new_phone = new_phone if new_phone else None
            new_email = new_email if new_email else None

            success, message = manager.update_contact(name, new_phone, new_email)
            print(message)

            if success:
                save_contacts(manager.contacts)

        elif choice == "5":
            name = input("Enter contact name to delete: ")
            success, message = manager.delete_contact(name)
            print(message)

            if success:
                save_contacts(manager.contacts)

        elif choice == "6":
            all_contacts = manager.list_contacts()
            if not all_contacts:
                print("No contacts available.")
            else:
                print("\n=== All Contacts ===")
                for name, info in all_contacts.items():
                    print_contact(name, info)

        elif choice == "7":
            if save_contacts(manager.contacts):
                print("Contacts saved. Goodbye.")
            else:
                print("Warning: Could not save contacts, but exiting anyway.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
