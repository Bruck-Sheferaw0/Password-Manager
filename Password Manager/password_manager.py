import tkinter
from tkinter import messagebox
from password_maker import PasswordGenerator
import random
import pyperclip

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=40)

canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text='Website:', font=("Arial", 10))
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = tkinter.Label(text="Password:")
pass_label.grid(column=0, row=3)

website_entry = tkinter.Entry(width=52)
website_entry.focus()
website_entry.grid(column=1, columnspan=2, row=1)

email_entry = tkinter.Entry(width=52)
email_entry.grid(column=1, columnspan=2, row=2)

password_entry = tkinter.Entry(width=33)
password_entry.grid(column=1, row=3)


def generate_pass():
    password_entry.delete(0, tkinter.END)
    password = PasswordGenerator(random.randint(4,10),random.randint(4,10),random.randint(4,10))
    password.letters_maker()
    password.numbers_maker()
    password.symbols_maker()
    pyperclip.copy("".join(password.total_password))
    password_entry.insert(tkinter.END, string="".join(password.total_password))


password_btn = tkinter.Button(text="Generate Password",command=generate_pass)
password_btn.grid(column=2, row=3)
def write_info():
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning("Warning", "Make Sure to fill out everything.")
    else:
        confirmation = messagebox.askokcancel(website_entry.get(),message=f"Email: {email_entry.get()}\nPassword: {password_entry.get()} \nAre you sure you want to save?")
        if confirmation:
            with open("accounts.txt","a") as accounts:
                accounts.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                website_entry.delete(0, tkinter.END)
                email_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)
                website_entry.focus()
        else:
            pass

add_btn = tkinter.Button(text="Add", width=44,command=write_info)
add_btn.grid(column=1, columnspan=2, row=4)

window.mainloop()
