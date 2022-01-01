from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

# Entry
entry_1 = Entry(width=10)
entry_1.grid(column=1, row=0)

# Labels
label_1 = Label(text="Miles", font=("Arial", 20))
label_1.grid(column=2, row=0)
label_2 = Label(text="is equal to", font=("Arial", 15))
label_2.grid(column=0, row=1)
label_3 = Label(text="0", font=("Arial", 10))
label_3.grid(column=1, row=1)
label_4 = Label(text="Km", font=("Arial", 20))
label_4.grid(column=2, row=1)


# Button
def convert_km():
    entry_miles = entry_1.get()
    formula = 1.60934
    km = float(entry_miles) * formula
    label_3.config(text=round(km, 2))


button_1 = Button(text="Convert", command=convert_km)
button_1.grid(column=1, row=2)





window.mainloop()
