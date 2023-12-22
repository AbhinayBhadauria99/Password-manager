from tkinter import *
from tkinter import messagebox
import random
import json
#below paperclip python project is used so that we need not to copy password
# it will get copied automatically and ready to use whereever you want
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []

  for char in range(nr_letters):
    password_list.append(random.choice(letters))

  for char in range(nr_symbols):
    password_list += random.choice(symbols)

  for char in range(nr_numbers):
    password_list += random.choice(numbers)

  random.shuffle(password_list)

  password = ""
  for char in password_list:
    password += char

  password_entry.insert(0,password)
  pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data={
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any field empty.")
    else:
        try:
            with open("data.json","r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
            with open("data.json","w") as data_file:
                #saving updated data
                json.dump(data,data_file,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=30)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")  # pehle variable me img ko define karna padega canvas ke liye.
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username : ")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.insert(0, "dummy@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password : ")
password_label.grid(column=0, row=3)

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

gen_pass_button = Button(text="Generate Password",command=generate_password)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="ADD", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()