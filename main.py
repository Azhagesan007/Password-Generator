from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
FONT = ("Courier", 10, "bold")


def search():
    website_search = web_entry.get()
    website_search = website_search.title()
    try:
        with open(file="data.json", mode="r") as files:
            web = json.load(files)
            inside_web = web[website_search]
            user_name = inside_web["Name"]
            user_password = inside_web["Password"]
        messagebox.showinfo(title=website_search, message=f"Your Username is: {user_name}\n"
                                                          f"Your Password is: {user_password}.\n"
                                                          f"Your password is copied to you clipboard")

        pyperclip.copy(user_password)

    except KeyError:
        messagebox.showwarning(title=website_search, message=f"The website {website_search} "
                                                             f"password is not stored here.")
    except FileNotFoundError:
        messagebox.showwarning(title=website_search, message=f"File not found")

    finally:
        web_entry.delete(0, "end")
        password_entry.delete(0, "end")
        web_entry.focus()

def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_l = [random.choice(letters) for _ in range(nr_letters)]
    password_s = [random.choice(symbols) for _ in range(nr_symbols)]
    password_n = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_l + password_n + password_s

    random.shuffle(password_list)

    password1 = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password1)
    pyperclip.copy(password1)


def save():
    webpage = web_entry.get()
    user_password = password_entry.get()
    user_email = username_entry.get()
    new_pass = {
        webpage.title(): {
            "Name": user_email,
            "Password": user_password
        }
    }
    if len(webpage) == 0 or len(user_password) == 0 or len(user_email) == 0:
        messagebox.showwarning(message="Don't leave the fields empty", title="Oops")

    else:
        data = messagebox.askokcancel(title=webpage,
                                      message=f"These are the details entered:\nYour username: {user_email}\n"
                                              f"Your password: {user_password}")
        if data:
            try:
                with open(file="data.json", mode="r")as file:
                    f_read = json.load(file)
                    f_read.update(new_pass)
                with open(file="data.json", mode="w") as file:
                    json.dump(f_read, file, indent=4)

            except FileNotFoundError:
                with open(file="data.json", mode="w") as file:
                    json.dump(new_pass, file, indent=4)

            finally:
                web_entry.delete(0, "end")
                password_entry.delete(0, "end")
                web_entry.focus()


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=image)
canvas.grid()

website = Label(text="Website:", font=FONT, bg="white")
username = Label(text="Email/Username:", font=FONT, bg="white")
password = Label(text="Password:", font=FONT, bg="white")

web_entry = Entry(width=32, bg="white")
username_entry = Entry(width=51, bg="white")
username_entry.insert(0, "azhagesany@gmail.com")
password_entry = Entry(width=32, bg="white")
web_entry.focus()

generate_password = Button(text="Generate Password", bg="white", command=gen_password)
add = Button(text="Add", bg="white", width=36, command=save)
searches = Button(text="Search", bg="white", width=14, command=search)

canvas.grid(row=0, column=1)
website.grid(row=1, column=0, sticky=E)
web_entry.grid(row=1, column=1, columnspan=2, sticky=W)
username.grid(row=2, column=0, sticky=E)
username_entry.grid(row=2, column=1, columnspan=2, sticky=W)
password.grid(row=3, column=0, sticky=E)
password_entry.grid(row=3, column=1, sticky=W)
generate_password.grid(row=3, column=2, sticky=E)
add.grid(row=4, column=1, columnspan=2)
searches.grid(row=1, column=2, sticky=W)

window.mainloop()
input()
