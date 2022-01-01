from tkinter import *
from tkinter import messagebox
import random
import pyperclip


#   -----SAVE INPUT------   #
def save_data():

    if len(entry_1.get()) <= 0 or len(entry_2.get()) <= 0 or len(entry_3.get()) <= 0:
        messagebox.showinfo(title="Blank Fields", message="Please do not leave any information blank")

    else:
        is_ok = messagebox.askokcancel(title="Save information", message=f"These are the details entered: \n"
                                                            f"Website: {entry_1.get()}\n"
                                                            f"Email: {entry_2.get()}\n"
                                                            f"Password: {entry_3.get}\n"
                                                            f"Is it ok to save? ")

        if is_ok:
            with open("data.txt", mode="a") as file:

                file.write(f"------------------------\n"
                           f"Website: {entry_1.get()}\n"
                           f"Email: {entry_2.get()}\n"
                           f"Password: {entry_3.get()}\n"
                           f"------------------------\n")
                entry_1.delete(0, END)
                entry_2.delete(0, END)
                entry_3.delete(0, END)
                entry_1.focus()


#   --------PASSWORD GENERATOR-----------   #
#   Password Generator Project
def gen_random_password():
    entry_3.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]

    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)

    entry_3.insert(0, password)
    pyperclip.copy(password)
    
    
#   --------UI-----------   #
windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50, bg="black")

canvas = Canvas(width=180, height=180, bg="black", highlightthickness=0)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0, column=1)

label_1 = Label(text="Website:", bg="black", fg="white")
label_1.grid(row=1, column=0, sticky=W, pady=10)

label_2 = Label(text="Email/Username:", bg="black", fg="white")
label_2.grid(row=2, column=0, sticky=W, pady=10)

label_3 = Label(text="Password:", bg="black", fg="white")
label_3.grid(row=3, column=0, sticky=W, pady=10)

entry_1 = Entry(width=35)
entry_1.grid(row=1, column=1, columnspan=2, sticky=W)
entry_1.focus()
entry_2 = Entry(width=35)
entry_2.grid(row=2, column=1, columnspan=2, sticky=W)
entry_2.insert(0, "dummyemail@gmai.com")
entry_3 = Entry(width=35)
entry_3.grid(row=3, column=1, sticky=W)

button_generate = Button(text="Generate Password", command=gen_random_password)

button_generate.grid(row=3, column=2, sticky=W, padx=10, pady=10)

button_add = Button(text="Add", width=30, command=save_data)
button_add.grid(row=4, column=1, columnspan=2, sticky=W)

windows.mainloop()
