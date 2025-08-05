from  tkinter import *

window = Tk()
window.title("PlayGround")
window.minsize(width=500, height=500)

# Label

my_label = Label(text="Hello, world")
my_label.grid(column=0, row=0)# show the info to the screen


def button_clicked():
    new_entry = entry.get()
    # my_label.config(text="Clicked on it")
    my_label["text"] = new_entry

# Button

button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

button1 = Button(text="Don't click")
button1.grid(column=3, row=0)

#Entry

entry = Entry(width=10)
entry.grid(column=4, row=3)



window.mainloop()