import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import json
import os

# File to store passwords
PASSWORD_FILE = "passwords.json"

# Ensure the file exists
if not os.path.exists(PASSWORD_FILE):
    with open(PASSWORD_FILE, "w") as file:
        json.dump({}, file)

# Function to generate a password
def generate_password():
    try:
        length = int(length_var.get())
        if length < 1:
            raise ValueError
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

# Function to save a password
def save_password():
    service = service_entry.get().strip()
    password = password_entry.get().strip()
    if not service or not password:
        messagebox.showwarning("Missing Information", "Please fill in both the service name and password.")
        return
    with open(PASSWORD_FILE, "r") as file:
        data = json.load(file)
    data[service] = password
    with open(PASSWORD_FILE, "w") as file:
        json.dump(data, file, indent=4)
    messagebox.showinfo("Success", "Password saved successfully!")
    service_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Function to view saved passwords
def view_passwords():
    with open(PASSWORD_FILE, "r") as file:
        data = json.load(file)
    if not data:
        messagebox.showinfo("No Data", "No passwords saved yet.")
        return
    passwords = "\n".join(f"{service}: {password}" for service, password in data.items())
    messagebox.showinfo("Saved Passwords", passwords)

# GUI Setup
root = tk.Tk()
root.title("Password Generator & Manager")
root.geometry("400x400")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Password Generator & Manager", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Service Entry
service_frame = tk.Frame(root)
service_frame.pack(pady=5)
service_label = tk.Label(service_frame, text="Service Name:", font=("Arial", 12))
service_label.pack(side=tk.LEFT, padx=5)
service_entry = ttk.Entry(service_frame, width=25)
service_entry.pack(side=tk.LEFT)

# Length Entry
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 12))
length_label.pack(side=tk.LEFT, padx=5)
length_var = tk.StringVar()
length_entry = ttk.Entry(length_frame, textvariable=length_var, width=5)
length_entry.pack(side=tk.LEFT)

# Password Entry
password_frame = tk.Frame(root)
password_frame.pack(pady=5)
password_label = tk.Label(password_frame, text="Generated Password:", font=("Arial", 12))
password_label.pack(side=tk.LEFT, padx=5)
password_entry = ttk.Entry(password_frame, width=25)
password_entry.pack(side=tk.LEFT)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
generate_button = ttk.Button(button_frame, text="Generate Password", command=generate_password)
generate_button.pack(side=tk.LEFT, padx=5)
save_button = ttk.Button(button_frame, text="Save Password", command=save_password)
save_button.pack(side=tk.LEFT, padx=5)
view_button = ttk.Button(button_frame, text="View Passwords", command=view_passwords)
view_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()
