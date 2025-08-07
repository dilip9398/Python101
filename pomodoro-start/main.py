from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_font = "DS-Digital"
timer_process = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global  reps, timer_process
    window.after_cancel(timer_process)
    timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="25:00")
    check_mark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:

        count_down(long_break)
        timer.config(text="Long break", fg=RED)
    elif reps % 2 == 0:

        count_down(short_break)
        timer.config(text="break", fg=PINK)
    else:

        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_process
        timer_process = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✅"

        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer.grid(row=0, column=1)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 133, text="00:00", fill="white", font=(timer_font, 24, "bold"))
canvas.grid(row=1, column=1)

# Adding the start and Reset buttons
start_button = Button(text="Start", font=(FONT_NAME, 8, "bold"), highlightthickness=0)
start_button.config(command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 8, "bold"), highlightthickness=0)
reset_button.config(command=reset_timer)
reset_button.grid(row=2, column=2)

#check Mark
check_mark = Label(text="", fg=GREEN, background=YELLOW, font=(FONT_NAME, 12,))
check_mark.grid(row=3, column=1)

window.mainloop()
