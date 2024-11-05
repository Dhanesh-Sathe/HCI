import tkinter as tk
from tkinter import messagebox, ttk

def submit():
    name = name_entry.get()
    dob = dob_entry.get()
    gender = gender_var.get()
    course = course_var.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_text.get("1.0", tk.END).strip()
    accept_terms = terms_var.get()

    # Validation
    if not all([name, dob, gender, course, email, phone, address]):
        messagebox.showwarning("Incomplete Data", "Please fill in all fields.")
        return
    if not accept_terms:
        messagebox.showwarning("Terms and Conditions", "You must accept the terms and conditions.")
        return

    # Display the submitted data
    messagebox.showinfo("Student Registration", f"Name: {name}\nDOB: {dob}\nGender: {gender}\n"
                                                f"Course: {course}\nEmail: {email}\n"
                                                f"Phone: {phone}\nAddress: {address}")

def clear_fields():
    name_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_text.delete("1.0", tk.END)
    gender_var.set("Male")
    course_var.set("Select Course")
    terms_var.set(0)

def about():
    messagebox.showinfo("About", "Student Registration Form v1.0\nCreated with Tkinter.")

# Initialize the main window
root = tk.Tk()
root.title("Enhanced Student Registration Form")
root.geometry("450x600")
root.configure(bg="#f0f4f8")

# Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Clear", command=clear_fields)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Title label
title_label = tk.Label(root, text="Student Registration", font=("Helvetica", 16, "bold"), bg="#005b96", fg="white")
title_label.pack(fill=tk.X, pady=(10, 20))

# Frame for form fields
form_frame = tk.Frame(root, bg="#f0f4f8")
form_frame.pack(pady=(0, 20))

# Name
tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#f0f4f8").grid(row=0, column=0, sticky="w", pady=5, padx=10)
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, pady=5, padx=10)

# Date of Birth (using Entry for simplicity, can be customized as needed)
tk.Label(form_frame, text="Date of Birth:", font=("Arial", 12), bg="#f0f4f8").grid(row=1, column=0, sticky="w", pady=5, padx=10)
dob_entry = tk.Entry(form_frame, width=30)
dob_entry.grid(row=1, column=1, pady=5, padx=10)

# Gender
tk.Label(form_frame, text="Gender:", font=("Arial", 12), bg="#f0f4f8").grid(row=2, column=0, sticky="w", pady=5, padx=10)
gender_var = tk.StringVar(value="Male")
gender_frame = tk.Frame(form_frame, bg="#f0f4f8")
gender_frame.grid(row=2, column=1, pady=5, padx=10)
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="#f0f4f8").pack(side="left")
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="#f0f4f8").pack(side="left")
tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other", bg="#f0f4f8").pack(side="left")

# Course (Drop-down list using OptionMenu)
tk.Label(form_frame, text="Course:", font=("Arial", 12), bg="#f0f4f8").grid(row=3, column=0, sticky="w", pady=5, padx=10)
course_var = tk.StringVar(value="Select Course")
course_options = ["Computer Science", "Mechanical Engineering", "Electrical Engineering", "Civil Engineering", "Business"]
course_dropdown = tk.OptionMenu(form_frame, course_var, *course_options)
course_dropdown.config(width=26)
course_dropdown.grid(row=3, column=1, pady=5, padx=10)

# Email
tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="#f0f4f8").grid(row=4, column=0, sticky="w", pady=5, padx=10)
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=4, column=1, pady=5, padx=10)

# Phone
tk.Label(form_frame, text="Phone:", font=("Arial", 12), bg="#f0f4f8").grid(row=5, column=0, sticky="w", pady=5, padx=10)
phone_entry = tk.Entry(form_frame, width=30)
phone_entry.grid(row=5, column=1, pady=5, padx=10)

# Address
tk.Label(form_frame, text="Address:", font=("Arial", 12), bg="#f0f4f8").grid(row=6, column=0, sticky="nw", pady=5, padx=10)
address_text = tk.Text(form_frame, width=23, height=3)
address_text.grid(row=6, column=1, pady=5, padx=10)

# Terms and Conditions (Checkbox)
terms_var = tk.IntVar()
terms_check = tk.Checkbutton(root, text="I accept the Terms and Conditions", variable=terms_var, bg="#f0f4f8")
terms_check.pack(pady=(10, 0))

# Submit and Clear buttons with custom styling
button_frame = tk.Frame(root, bg="#f0f4f8")
button_frame.pack(pady=20)
submit_button = tk.Button(button_frame, text="Submit", command=submit, font=("Arial", 12, "bold"),
                          bg="#005b96", fg="white", width=10, relief="raised")
submit_button.grid(row=0, column=0, padx=10)
clear_button = tk.Button(button_frame, text="Clear", command=clear_fields, font=("Arial", 12, "bold"),
                         bg="#b22222", fg="white", width=10, relief="raised")
clear_button.grid(row=0, column=1, padx=10)

# Run the application
root.mainloop()
