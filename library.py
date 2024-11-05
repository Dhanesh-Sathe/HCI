import tkinter as tk
from tkinter import messagebox

# Initialize root window
root = tk.Tk()
root.title("Library Management System")
root.geometry("600x500")
root.configure(bg="#f5f5dc")  # Light beige background color

# Book information list
books = []
selected_index = None

# Functions for various actions
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    year = year_entry.get()

    if title and author and isbn and year:
        books.append({"title": title, "author": author, "isbn": isbn, "year": year})
        messagebox.showinfo("Success", "Book added successfully!")
        clear_entries()
        display_books()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def delete_book():
    global selected_index
    if selected_index is not None:
        del books[selected_index]
        messagebox.showinfo("Success", "Book deleted successfully!")
        clear_entries()
        display_books()
        selected_index = None
    else:
        messagebox.showwarning("Selection Error", "Please select a book to delete.")

def search_book():
    search_title = title_entry.get()
    matching_books = [book for book in books if book["title"].lower() == search_title.lower()]

    book_list.delete(0, tk.END)
    if matching_books:
        for book in matching_books:
            book_list.insert(tk.END, f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']}")
    else:
        messagebox.showinfo("Not Found", "No matching book found.")

def display_books():
    book_list.delete(0, tk.END)
    for book in books:
        book_list.insert(tk.END, f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']}")

def on_book_select(event):
    global selected_index
    try:
        selection = book_list.curselection()
        if selection:
            selected_index = selection[0]
            selected_book = books[selected_index]

            # Fill entry fields with selected book info
            title_entry.delete(0, tk.END)
            title_entry.insert(tk.END, selected_book["title"])

            author_entry.delete(0, tk.END)
            author_entry.insert(tk.END, selected_book["author"])

            isbn_entry.delete(0, tk.END)
            isbn_entry.insert(tk.END, selected_book["isbn"])

            year_entry.delete(0, tk.END)
            year_entry.insert(tk.END, selected_book["year"])
    except IndexError:
        pass

def clear_entries():
    global selected_index
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    isbn_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    selected_index = None

# Title Label
title_label = tk.Label(root, text="Library Management System", font=("Helvetica", 18, "bold"), bg="#008080", fg="white")  # Teal background
title_label.pack(fill=tk.X, pady=(10, 20))

# Form Frame
form_frame = tk.Frame(root, bg="#f5f5dc")
form_frame.pack(pady=10)

# Book Title
tk.Label(form_frame, text="Book Title:", font=("Arial", 12), bg="#f5f5dc").grid(row=0, column=0, sticky="w", padx=10, pady=5)
title_entry = tk.Entry(form_frame, width=30)
title_entry.grid(row=0, column=1, padx=10, pady=5)

# Author
tk.Label(form_frame, text="Author:", font=("Arial", 12), bg="#f5f5dc").grid(row=1, column=0, sticky="w", padx=10, pady=5)
author_entry = tk.Entry(form_frame, width=30)
author_entry.grid(row=1, column=1, padx=10, pady=5)

# ISBN
tk.Label(form_frame, text="ISBN:", font=("Arial", 12), bg="#f5f5dc").grid(row=2, column=0, sticky="w", padx=10, pady=5)
isbn_entry = tk.Entry(form_frame, width=30)
isbn_entry.grid(row=2, column=1, padx=10, pady=5)

# Year of Publication
tk.Label(form_frame, text="Year of Publication:", font=("Arial", 12), bg="#f5f5dc").grid(row=3, column=0, sticky="w", padx=10, pady=5)
year_entry = tk.Entry(form_frame, width=30)
year_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#f5f5dc")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Book", command=add_book, font=("Arial", 10, "bold"), bg="#008080", fg="white", width=12)  # Teal button
add_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(button_frame, text="Delete Book", command=delete_book, font=("Arial", 10, "bold"), bg="#ff6347", fg="white", width=12)  # Coral button
delete_button.grid(row=0, column=1, padx=10)

search_button = tk.Button(button_frame, text="Search Book", command=search_book, font=("Arial", 10, "bold"), bg="#4682b4", fg="white", width=12)  # Steel blue button
search_button.grid(row=0, column=2, padx=10)

display_button = tk.Button(button_frame, text="Display All Books", command=display_books, font=("Arial", 10, "bold"), bg="#daa520", fg="white", width=15)  # Golden rod button
display_button.grid(row=0, column=3, padx=10)

# Book List Display
book_list = tk.Listbox(root, height=10, width=70, font=("Arial", 10))
book_list.pack(pady=10)
book_list.bind("<<ListboxSelect>>", on_book_select)

# Run the application
root.mainloop()
