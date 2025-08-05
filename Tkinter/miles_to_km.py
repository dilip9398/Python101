from tkinter import *





def calculate_km():
    def calculate_kms():
        value = km_input.get()
        miles = int(value) * 0.621371
        km_label.config(text=f"is equal {miles} Miles")

    km_input = Entry(width=12)
    km_input.grid(column=0, row=0, pady=0, padx=0)

    km_label = Label(text="km", font=("Courier", 16, "bold"))
    km_label.grid(column=1, row=0)

    miles_label = Label(text=f"is equal {0} Miles", font=("Courier", 16, "bold"))
    miles_label.grid(column=0, row=1, pady=10)

    calculate_button = Button(text="Calculate", command=calculate_kms)
    calculate_button.grid(column=0, row=3, pady=10, padx=10)



window = Tk()
window.minsize(width=400, height=400)
window.title("Miles to KM ")
window.config(padx=100, pady=100)

def calculate_miles():
    def calculate():
        value = miles_input.get()
        km = int(value) * 1.609043
        km_label.config(text=f"is equal {km} KM")
    miles_input  = Entry(width=12)
    miles_input.grid(column=0, row=0, pady=0, padx=0)

    miles_label = Label(text="Miles",font=("Courier", 16, "bold"))
    miles_label.grid(column=1, row=0)

    km_label = Label(text=f"is equal {0} KM", font=("Courier", 16, "bold"))
    km_label.grid(column=0, row=1, pady=10)

    calculate_button = Button(text="Calculate", command=calculate)
    calculate_button.grid(column=0, row=3, pady=10, padx=10)

convert_button = Button(text="To KM", command=calculate_km)
convert_button.grid(column=0, row=5)

convert_button = Button(text="To Miles", command=calculate_miles)
convert_button.grid(column=1, row=5)









window.mainloop()