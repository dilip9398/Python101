import json
from  tkinter import *
from tkinter import messagebox
import random
import pyperclip
import os




# ---------------------------- PASSWORD FINDER ------------------------------- #
def find_pass():
    web = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="No file", message="No file created and no data")
    else:
        if web in data:
            email = data[web]["Email"]
            pd = data[web]["Password"]
            messagebox.showinfo(title=web, message=f"E-mail: {email}\n Password : {pd}")
        else:
            messagebox.showinfo(title="no data", message=f"{web} is not found in the data")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    lt = [random.choice(letters) for _ in range(random.randint(8,10))]
    nr = [random.choice(numbers) for _ in range(random.randint(4, 6))]
    sl = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    pd_list = lt + nr + sl
    random.shuffle(pd_list)
    pd = "".join(pd_list)
    password_input.delete(0, END)
    password_input.insert(0,pd)

    pyperclip.copy(pd)

    print(pd)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    wb = website_input.get()
    us = user_name_input.get()
    pwd = password_input.get()

    new_data = {
        wb:{
            "Email" : us,
            "Password" : pwd,
        }
    }

    if len(wb)  == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Opps", message="Enter the details")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()






# ---------------------------- UI SETUP ------------------------------- #

#set window icon
script_dir = os.path.dirname(os.path.abspath("D:\Python100\password-manager-start\password_manager.py"))
logo_path = os.path.join(script_dir, "logo.png")
icon_path = os.path.join(script_dir, "icon.ico")

window = Tk()
window.title("Password Manager")

# Use a try-except block for robustness
try:
    window.iconbitmap(icon_path) # <-- 3. Use the full path
except TclError:
    print("icon.ico not found.")

window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

# Use a try-except block for the logo as well
try:
    lock_img = PhotoImage(file=logo_path) # <-- 4. Use the full path for the logo
    canvas.create_image(100, 100, image=lock_img)
except TclError:
    print(f"Could not open '{logo_path}': no such file or directory.")

canvas.grid(row=0, column=1)

# Setting up the Layout of the Input and buttons

#Website link
website_links = Label(text="Website:" )
website_links.grid(row=1, column=0)

website_button = Button(text="Search",  background="blue", command=find_pass)
website_button.grid(row=1, column=2)

website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

#username and email
user_name = Label(text="Username/Email:" )
user_name.grid(row=2, column=0)

user_name_input = Entry()
user_name_input.config(width=35)
# user_name_input.insert(END, "")
user_name_input.grid(row=2, column=1, columnspan=2)

# password
password = Label(text="Password:" )
password.grid(row=3, column=0)

password_input = Entry()
password_input.config(width=21)


password_input.grid(row=3, column=1)

#Generate button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)


#Add button
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()