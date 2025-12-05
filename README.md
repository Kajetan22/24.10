[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-fQBFLq-)
# Smart Library System

## Task Description
Build a Library Management System where users can **add books**, **borrow** and **return** them, and search for books by title
or author. The program must demonstrate object-oriented programming concepts and separate logic from interface. The main entry
point should be `main.py`. Add any custom modules and packages as needed.

## Minimum Requirements (Basic Implementation)

### Modules & Structure
* Logic Module:
  * **Book class**: attributes like title, `author`, `is_available`.
  * **User class**: attributes like name, `borrowed_books`.
  * **Library class**: manages a collection of Book objects, with methods:
    * `add_book()`
    * `borrow_book()`
    * `return_book()`
    * `search_book()`

* Interface Module:
  * Handles user interaction (text-based menu).
  * Calls methods from Library class.

This separation mirrors the “Kitchen and Dining Room” concept.

### Features
* Add books to the library.
* Borrow and return books (update availability).
* Search by title or author.
* Display all available books.

## Extension Ideas (For Higher Marks)

* **Persistence**: Save and load library data using pickle or JSON.
* **Graphical Interface**: Use tkinter or PyQt for a GUI.
* **Advanced Search**: Implement filters (e.g., by genre, year).
* **User Accounts**: Add User class with borrowing history.
* **Statistics**: Show most borrowed books.
* **External APIs**: Integrate with Google Books API for book details.

## Grading Criteria
* Basic (Pass): Implements Book and Library classes, text-based interface, modular design.
* Intermediate (Good): Adds error handling, persistence (e.g., JSON), and clean code structure.
* Advanced (Excellent): Adds GUI, user accounts, analytics, or integrates external APIs (e.g., Google Books).
* Code Quality: Proper naming, comments, PEP8 compliance, and modularity are required for higher marks.
