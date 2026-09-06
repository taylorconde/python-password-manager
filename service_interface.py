import tkinter as tk
from tkinter import messagebox


# ---------------------------- LOGIN INTERFACE ------------------------------- #
class LoginInterface:
    def __init__(self, root, login_callback):
        self.root = root
        self.login_callback = login_callback # Funcao chamada ao logar

        self.root.title("Master Login")
        self.root.resizable(False, False)
        self.root.config(padx=50, pady=50)

        #Label
        self.label = tk.Label(text="Enter Master Passkey:", font=("Arial", 12, "bold"))
        self.label.pack(pady=10)

        # Entry (Campo de senha)
        self.password_entry = tk.Entry(show="*", width=30, font=("Arial", 12))
        self.password_entry.pack(pady=10)
        self.password_entry.focus()

        # Button
        self.login_button = tk.Button(text="Login", width=20, command=self.handle_login)
        self.login_button.pack(pady=20)

    def handle_login(self):
        password = self.password_entry.get()
        if password: self.login_callback(password)
        else: messagebox.showerror("Error", "Please enter your master passkey.")

# ---------------------------- UI SETUP ------------------------------- #
class UserInterface:
    def __init__(self, root,password_generator,save_data, search_data):
        #window
        self.root = root
        self.root.title("Password Manager")
        self.pass_generator = password_generator
        self.save = save_data
        self.root.resizable(False,False)
        self.root.config(padx=50,pady=50)
        self.search = search_data

    #image
        self.canvas = tk.Canvas(height=200,width=200)
        self.logo_img = tk.PhotoImage(file="logo.png")
        self.canvas.create_image(100,100,image=self.logo_img)
        self.canvas.grid(column=1,row=0)

    #labels
        self.website_label = tk.Label(text="Website: ")
        self.website_label.config(font=("Arial", 10,"bold"))
        self.website_label.grid(column=0,row=1, sticky='e')

        self.email_username_label = tk.Label(text="Email/Username: ")
        self.email_username_label.config(font=("Arial", 10,"bold"))
        self.email_username_label.grid(column=0,row=2, sticky='e')

        self.password_label = tk.Label(text="Password: ")
        self.password_label.config(font=("Arial", 10,"bold"))
        self.password_label.grid(column=0,row=3, sticky='e')

    #entries
        self.website_entry = tk.Entry(width=32)
        self.website_entry.grid(column=1,row=1, columnspan=2,sticky='w')
        self.website_entry.focus()

        self.email_username_entry = tk.Entry(width=50)
        self.email_username_entry.grid(column=1,row=2, columnspan=2, sticky='w')
        self.email_username_entry.insert(tk.END, string="useremail@mail.com")

        self.password_entry = tk.Entry(width=32)
        self.password_entry.grid(column=1,row=3, columnspan=2 ,sticky='w')

    #button
        self.password_button = tk.Button(text="Generate Password", width=16,font=("Arial", 8), command=self.pass_generator)
        self.password_button.grid(column=2,row=3, sticky='e')

        self.add_button = tk.Button(text="Add", width=47, command=self.save)
        self.add_button.grid(column=1,row=4, columnspan=2)

        self.search_button = tk.Button(text="Search", width=14, command=self.search)
        self.search_button.grid(column=2, row=1,sticky='e')