import tkinter as tk
from tkinter import ttk

name_entry = None
description_entry = None
author_entry = None
add_book_window = None
name_entry = None
description_entry = None
author_entry = None
add_book_window = None
books = [{"name": "Book1", "description": "Description1", "author": "Author1"},
             {"name": "Book2", "description": "Description2", "author": "Author2"},
             {"name": "Book3", "description": "Description3", "author": "Author3"}]

#function that loops through books and show them
def show_books():
    
    for i, book in enumerate(books):
        ttk.Label(root, text=book["name"]).grid(row=i, column=0)
        ttk.Label(root, text=book["description"]).grid(row=i, column=1)
        ttk.Label(root, text=book["author"]).grid(row=i, column=2)
#function that allows you to add the book with label , description and author details , with a submit button that validates the added book
def add_book():
    global name_entry, description_entry, author_entry, add_book_window
    add_book_window = tk.Toplevel(root)
    add_book_window.title("Add a new book")

    name_label = ttk.Label(add_book_window, text="Name:")
    name_label.grid(row=0, column=0)
    name_entry = ttk.Entry(add_book_window)
    name_entry.grid(row=0, column=1)

    description_label = ttk.Label(add_book_window, text="Description:")
    description_label.grid(row=1, column=0)
    description_entry = ttk.Entry(add_book_window)
    description_entry.grid(row=1, column=1)

    author_label = ttk.Label(add_book_window, text="Author:")
    author_label.grid(row=2, column=0)
    author_entry = ttk.Entry(add_book_window)
    author_entry.grid(row=2, column=1)

    submit_button = ttk.Button(add_book_window, text="Submit", command=submit_book)
    submit_button.grid(row=3, column=1)

# a function of submission , it allows you to submit the books that will be shown
def submit_book():
    global name_entry, description_entry, author_entry, add_book_window
    name = name_entry.get()
    description = description_entry.get()
    author = author_entry.get()
    books.append({"name":name, "description":description, "author":author})
    add_book_window.destroy()
    show_books()

#The interfaces on tikenter that shows the two buttons : show book and submit books
root = tk.Tk()
show_books_button = tk.Button(root, text="Show books", command=show_books)
show_books_button.grid(row=0,column=0)
add_book_button = tk.Button(root, text="Add book", command=add_book)
add_book_button.grid(row=1,column=0)

root.mainloop()
