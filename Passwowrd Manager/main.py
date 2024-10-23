from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
FONT = ("Roman New Times", 10, "bold")
FONT_2 = ("Roman New Times", 10, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email_username = em_us_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="You unfill any input!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\n Email\\Username: {email_username}"
                                               f"\nPassword: {password}\n\n Arr sure that you wanna save them")
        if is_ok:
            with open("password.txt", mode="a") as file:
                file.write(f"Website: {website} | Email\\Username: {email_username} | Password: {password}\n")
                website_input.delete(0, END)
                em_us_input.delete(0, END)
                em_us_input.insert(0, "example@email.com | Bou-eng")
                password_input.delete(0, END)
# ---------------------------- UI SETUP -------------------------------#


window = Tk()
window.title("Password Manager")
window.config(bg="white", padx=50, pady=50)
canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.config(bg="white", highlightthickness=0)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.config(font=FONT, fg="black", bg="white")
website_label.grid(row=2, column=0, sticky='w')

website_input = Entry()
website_input.config(width=35, bg="lightblue", font=FONT_2)
website_input.grid(column=1, row=2, columnspan=2, sticky='w')
website_input.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.config(font=FONT, fg="black", bg="white")
email_username_label.grid(row=3, column=0, sticky='w')

em_us_input = Entry()
em_us_input.config(width=35, bg="lightblue", font=FONT_2)
em_us_input.grid(row=3, column=1, columnspan=2, sticky='w')
em_us_input.insert(0, "example@email.com | Bou-eng")

password_label = Label(text="Password:")
password_label.config(font=FONT, fg="black", bg="white")
password_label.grid(row=4, column=0, sticky='w')

password_input = Entry()
password_input.config(width=20, bg="lightblue", font=FONT_2)
password_input.grid(column=1, row=4, sticky='w')


generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.config(font=FONT, fg="black", bg="white")
generate_pass_button.grid(column=2, row=4, sticky='e')

add_button = Button(text="Add", command=save)
add_button.config(font=FONT, fg="black", bg="white", highlightthickness=0, width=35)
add_button.grid(row=5, column=1, columnspan=2, sticky='w')

window.mainloop()
