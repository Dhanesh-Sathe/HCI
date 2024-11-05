import tkinter as tk
from tkinter import messagebox, ttk

def submit_form():
    # Fetch all input values
    name = name_entry.get()
    dob = dob_entry.get()
    gender = gender_var.get()
    grade = grade_var.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_text.get("1.0", tk.END).strip()
    cet_marks = cet_entry.get()
    caste = caste_var.get()
    income = income_entry.get()
    accept_terms = terms_var.get()

    # Check if all required fields are filled
    if not all([name, dob, gender, grade, email, phone, address, cet_marks, caste, income]):
        messagebox.showwarning("Incomplete Data", "Please fill in all fields.")
        return
    if not accept_terms:
        messagebox.showwarning("Terms and Conditions", "You must accept the terms and conditions.")
        return

    # Display the submitted data
    messagebox.showinfo("Admission Form Submission", f"Name: {name}\nDOB: {dob}\nGender: {gender}\n"
                                                     f"Grade: {grade}\nEmail: {email}\n"
                                                     f"Phone: {phone}\nCET Marks: {cet_marks}\n"
                                                     f"Caste: {caste}\nAnnual Income: {income}\n"
                                                     f"Address: {address}")

def clear_fields():
    name_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_text.delete("1.0", tk.END)
    cet_entry.delete(0, tk.END)
    income_entry.delete(0, tk.END)
    gender_var.set("Male")
    grade_var.set("Select Grade")
    caste_var.set("Select Caste")
    terms_var.set(0)

# Initialize main window
root = tk.Tk()
root.title("Student Admission Form")
root.geometry("500x800")
root.configure(bg="#f0f4f8")

# Title label
title_label = tk.Label(root, text="Student Admission Form", font=("Helvetica", 18, "bold"), bg="#005b96", fg="white")
title_label.pack(fill=tk.X, pady=(10, 20))

# Form frame
form_frame = tk.Frame(root, bg="#f0f4f8")
form_frame.pack(pady=(0, 20))

# Name
tk.Label(form_frame, text="Full Name:", font=("Arial", 12), bg="#f0f4f8").grid(row=0, column=0, sticky="w", pady=5, padx=10)
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, pady=5, padx=10)

# Date of Birth
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

# Grade
tk.Label(form_frame, text="Grade:", font=("Arial", 12), bg="#f0f4f8").grid(row=3, column=0, sticky="w", pady=5, padx=10)
grade_var = tk.StringVar(value="Select Grade")
grade_options = ["Kindergarten", "1st Grade", "2nd Grade", "3rd Grade", "4th Grade", "5th Grade", "6th Grade", "7th Grade", "8th Grade", "9th Grade", "10th Grade", "11th Grade", "12th Grade"]
grade_dropdown = tk.OptionMenu(form_frame, grade_var, *grade_options)
grade_dropdown.config(width=26)
grade_dropdown.grid(row=3, column=1, pady=5, padx=10)

# CET Marks
tk.Label(form_frame, text="CET Marks:", font=("Arial", 12), bg="#f0f4f8").grid(row=4, column=0, sticky="w", pady=5, padx=10)
cet_entry = tk.Entry(form_frame, width=30)
cet_entry.grid(row=4, column=1, pady=5, padx=10)

# Caste
tk.Label(form_frame, text="Caste:", font=("Arial", 12), bg="#f0f4f8").grid(row=5, column=0, sticky="w", pady=5, padx=10)
caste_var = tk.StringVar(value="Select Caste")
caste_options = ["General", "OBC", "SC", "ST", "Other"]
caste_dropdown = tk.OptionMenu(form_frame, caste_var, *caste_options)
caste_dropdown.config(width=26)
caste_dropdown.grid(row=5, column=1, pady=5, padx=10)

# Annual Income
tk.Label(form_frame, text="Annual Income (INR):", font=("Arial", 12), bg="#f0f4f8").grid(row=6, column=0, sticky="w", pady=5, padx=10)
income_entry = tk.Entry(form_frame, width=30)
income_entry.grid(row=6, column=1, pady=5, padx=10)

# Email
tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="#f0f4f8").grid(row=7, column=0, sticky="w", pady=5, padx=10)
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=7, column=1, pady=5, padx=10)

# Phone
tk.Label(form_frame, text="Phone:", font=("Arial", 12), bg="#f0f4f8").grid(row=8, column=0, sticky="w", pady=5, padx=10)
phone_entry = tk.Entry(form_frame, width=30)
phone_entry.grid(row=8, column=1, pady=5, padx=10)

# Address
tk.Label(form_frame, text="Address:", font=("Arial", 12), bg="#f0f4f8").grid(row=9, column=0, sticky="nw", pady=5, padx=10)
address_text = tk.Text(form_frame, width=23, height=3)
address_text.grid(row=9, column=1, pady=5, padx=10)

# Terms and Conditions
terms_var = tk.IntVar()
terms_check = tk.Checkbutton(root, text="I accept the Terms and Conditions", variable=terms_var, bg="#f0f4f8")
terms_check.pack(pady=(10, 0))

# Buttons
button_frame = tk.Frame(root, bg="#f0f4f8")
button_frame.pack(pady=20)
submit_button = tk.Button(button_frame, text="Submit", command=submit_form, font=("Arial", 12, "bold"),
                          bg="#005b96", fg="white", width=10, relief="raised")
submit_button.grid(row=0, column=0, padx=10)
clear_button = tk.Button(button_frame, text="Clear", command=clear_fields, font=("Arial", 12, "bold"),
                         bg="#b22222", fg="white", width=10, relief="raised")
clear_button.grid(row=0, column=1, padx=10)

# Run the application
root.mainloop()
