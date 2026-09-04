import tkinter as tk
from tkinter import messagebox

from password import strong_password
from service_interface import UserInterface, LoginInterface

from encryption_service import EncryptionService
from cryptography.fernet import InvalidToken
import pyperclip
import re


root = tk.Tk()

# ---------------------------- HANDLE LOGIN ------------------------------- #
def handle_login(password):
    global encryption_service, interface

    encryption_service = EncryptionService(password)

    for widget in root.winfo_children():
        widget.destroy() # Remove todos os widgets da tela de login

    interface = UserInterface(root, password_generator, save_data,search_data)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    new_pass = strong_password()
    interface.password_entry.delete(0, 'end')
    interface.password_entry.insert(tk.END, string=new_pass)
    pyperclip.copy(new_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def clear_entry():
    #cleaning entry text area
    interface.website_entry.delete(0,'end')
    interface.password_entry.delete(0,'end')

def validate_data():
    mail_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if not re.match(mail_regex, interface.email_username_entry.get()):
        messagebox.showerror("Error","Please, input a valid mail.")
        return False
    if len(interface.password_entry.get()) < 6:
        messagebox.showerror("Error", "Password must have at least 6 digits.")
        return False

    return True

def save_data():

    website_data = interface.website_entry.get()
    email_username_data = interface.email_username_entry.get()
    password_data = interface.password_entry.get()

    if validate_data():
        is_ok=messagebox.askokcancel(
            title=website_data,
            message=f"These are the details entered: "
                    f"\nEmail:{email_username_data}"
                    f"\nPassword:{password_data}"
                    f"\nIs it ok to save?")

        if is_ok:
            encrypted_pass = encryption_service.encrypt(password_data)
            with open("data.csv", "a") as data:
                data.writelines(f"{website_data} | {email_username_data} | {encrypted_pass}\n")
            clear_entry()


def search_data():
    target_website = interface.website_entry.get()

    if not target_website:
        messagebox.showerror("Error", "Please enter a website name to search.")
        return

    try:
        with open("data.csv", "r") as data:
            for line in data:
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    site, email, encrypted_pass = parts

                    if target_website == site:
                        try:
                            decrypted_pass = encryption_service.decrypt(encrypted_pass)
                            messagebox.showinfo("Password Found",
                                                f"Website: {site}\nEmail: {email}\nPassword: {decrypted_pass}")
                            return
                        except InvalidToken:
                            messagebox.showerror("Error",
                                                 "Could not decrypt this password. Check your master passkey.")
                            return
            messagebox.showinfo("Not Found", "No entry found for this website.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found, Add a password first!")






login_ui = LoginInterface(root, handle_login)

root.mainloop()
