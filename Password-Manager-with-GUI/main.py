from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import json
import pyperclip

FONT = ("Liberation Mono", 16, "bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password__letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password__letters + password_symbols + password_numbers

    shuffle(password_list)

    new_password = "".join(password_list)

    password_input.delete(0, END)

    password_input.insert(0, new_password)
    pyperclip.copy(new_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_data():
    website = web_site_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
   
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Field", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # The file doesn't exist or is empty/corrupted
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", 'w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            web_site_input.delete(0, END)
            web_site_input.focus()
            password_input.delete(0, END)


# Find password
def search_password():
    site = web_site_input.get()
    if len(site) == 0:
        messagebox.showinfo(title="Empty Field", message="Please enter an email address.")
    else:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
                if site in data:
                    messagebox.showinfo(title=f"{site}", message=f"Email: {data[site]["email"]}\nPassword: {data[site]["password"]}")
                else:
                    messagebox.showinfo(title=f"{site}", message=f"No info on {site} has been saved.")
        except(FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror(title="No Data", message="You do not have any passwords saved.")
        finally:
            web_site_input.delete(0, END)
            web_site_input.focus()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Local Password Manager")
window.config(padx=50, pady=50)
# Display the logo image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website input field
web_site = Label(text="website: ", font=FONT)
web_site.grid(row=1, column=0)
web_site_input = Entry(width=21)
web_site_input.focus()
web_site_input.grid(row=1, column=1)

# Search Button
search_btn = Button(text="Search", font=FONT, command=search_password, width=16)
search_btn.grid(row=1, column=2)

# Email/Username input field
email = Label(text="Email/Username: ", font=FONT)
email.grid(row=2, column=0)
email_input = Entry(width=43)
email_input.insert(END, "mark@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

# Password input field
password = Label(text="Password: ", font=FONT)
password.grid(row=3, column=0)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)
generate_password_btn = Button(text="Generate Password", font=FONT, command=generate_password, width=16)
generate_password_btn.grid(row=3, column=2)

# Add password info to the Manager
add_btn = Button(text="Add", width=36, font=FONT, command=write_data)
add_btn.grid(row=4, column=1, columnspan=2)
window.mainloop()
