# QuickFind — Contact Management System

QuickFind is a lightweight command-line contact management application built in Python.  
It allows users to store, search, update, and delete contact information while maintaining fast lookup performance using hash-based indexing.

The project demonstrates core computer science concepts such as data structures, file persistence, and modular software design.

---

## Features

- Add new contacts with phone number and email
- Fast contact lookup using hash-map indexing (Python dictionaries)
- Update or delete existing contacts
- Partial name search for quick retrieval
- Persistent storage using JSON files
- Simple command-line interface

---

## Technologies Used

- Python
- Hash maps (Python dictionaries)
- File I/O
- JSON data storage
- Modular program structure

---

## Project Structure

```
QuickFind/
│
├── main.py               # Command-line interface
├── contact_manager.py    # Core contact management logic
├── storage.py            # JSON loading and saving utilities
├── contacts.json         # Persistent data storage
└── README.md             # Project documentation
```

---

## How It Works

Contacts are stored in a hash-based structure for efficient access:

```
{
  "Alice": {
    "phone": "555-1234",
    "email": "alice@email.com"
  },
  "Bob": {
    "phone": "555-5678",
    "email": "bob@email.com"
  }
}
```

This structure enables **constant-time average lookup** when searching by name.

---

## Running the Project

1. Ensure Python is installed on your system.
2. Clone or download the repository.
3. Navigate to the project directory.
4. Run the program:

```
python main.py
```

If your system uses Python3 explicitly:

```
python3 main.py
```

---

## Example Interface

```
=== QuickFind Contact Manager ===

1. Add Contact
2. Search Contact by Exact Name
3. Search Contact by Partial Name
4. Update Contact
5. Delete Contact
6. List All Contacts
7. Exit
```

---

## Example Use Cases

- Managing personal contacts
- Practicing CRUD-based software design
- Demonstrating hash-table indexing
- Learning basic data persistence techniques

---

## Possible Future Improvements

- Search by phone number or email
- CSV export/import functionality
- Graphical user interface (Tkinter)
- Unit testing with pytest
- REST API version using Flask

---

## Author

Anirudh Jha  
Computer Science — San Diego State University
