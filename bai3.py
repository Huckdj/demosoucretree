import tkinter as tk
from tkinter import messagebox

def enter_data():
    if terms_var.get():
        info = f"""
        First Name: {first_name_entry.get()}
        Last Name: {last_name_entry.get()}
        Title: {title_var.get()}
        Age: {age_spinbox.get()}
        Nationality: {nationality_entry.get()}
        Currently Registered: {"Yes" if registered_var.get() else "No"}
        Completed Courses: {courses_spinbox.get()}
        Semesters: {semesters_spinbox.get()}
        """
        info_text.delete(1.0, tk.END)  # Clear previous text
        info_text.insert(tk.END, info)
        messagebox.showinfo("Data Entry", "Data Submitted Successfully!")
    else:
        messagebox.showwarning("Data Entry", "Please accept the terms and conditions.")

# Create the main window
root = tk.Tk()
root.title("Data Entry Form")
root.geometry("500x500")

# Create the User Information frame
user_info_frame = tk.LabelFrame(root, text="User Information", padx=10, pady=10)
user_info_frame.pack(padx=10, pady=10, fill="both", expand=True)

tk.Label(user_info_frame, text="First Name").grid(row=0, column=0)
tk.Label(user_info_frame, text="Last Name").grid(row=0, column=1)
tk.Label(user_info_frame, text="Title").grid(row=0, column=2)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
title_var = tk.StringVar(value="Select")
title_options = ["Mr.", "Ms.", "Dr.", "Prof."]
title_menu = tk.OptionMenu(user_info_frame, title_var, *title_options)

first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)
title_menu.grid(row=1, column=2)

tk.Label(user_info_frame, text="Age").grid(row=2, column=0)
tk.Label(user_info_frame, text="Nationality").grid(row=2, column=1)

age_spinbox = tk.Spinbox(user_info_frame, from_=0, to=100)
nationality_entry = tk.Entry(user_info_frame)

age_spinbox.grid(row=3, column=0)
nationality_entry.grid(row=3, column=1)

# Create the Registration Status frame
registration_frame = tk.LabelFrame(root, text="Registration Status", padx=10, pady=10)
registration_frame.pack(padx=10, pady=10, fill="both", expand=True)

registered_var = tk.BooleanVar()
tk.Checkbutton(registration_frame, text="Currently Registered", variable=registered_var).grid(row=0, column=0)

tk.Label(registration_frame, text="# Completed Courses").grid(row=0, column=1)
tk.Label(registration_frame, text="# Semesters").grid(row=0, column=2)

courses_spinbox = tk.Spinbox(registration_frame, from_=0, to=100)
semesters_spinbox = tk.Spinbox(registration_frame, from_=0, to=10)

courses_spinbox.grid(row=1, column=1)
semesters_spinbox.grid(row=1, column=2)

# Create the Terms & Conditions frame
terms_frame = tk.LabelFrame(root, text="Terms & Conditions", padx=10, pady=10)
terms_frame.pack(padx=10, pady=10, fill="both", expand=True)

terms_var = tk.BooleanVar()
tk.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=terms_var).pack()

# Create the Submit button
submit_button = tk.Button(root, text="Enter data", command=enter_data)
submit_button.pack(pady=10)

# Create the Text widget to display the entered information
info_frame = tk.LabelFrame(root, text="Entered Information", padx=10, pady=10)
info_frame.pack(padx=10, pady=10, fill="both", expand=True)

info_text = tk.Text(info_frame, height=10)
info_text.pack(fill="both", expand=True)

# Run the application
root.mainloop()
