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
REPS = 1
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(TIMER)
    header_label.config(text="Timer")
    checker_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        header_label.config(text="Break", font=(FONT_NAME, 35, "bold"), fg=RED)
        checker_label.config(text="")
        print("Long Break")
    else:
        if REPS % 2 == 0:
            count_down(short_break_sec)
            header_label.config(text="Break", font=(FONT_NAME, 35, "bold"), fg=PINK)
        else:
            count_down(work_sec)
            header_label.config(text="Work", font=(FONT_NAME, 35, "bold"), fg=GREEN)

        # count_down(10 * 1)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global REPS
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        if count == 0:
            REPS += 1
            start_timer()
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        check_symbol = ""
        work_session = math.floor(REPS/2)

        for _ in range(work_session):

            check_symbol += "✔"
        checker_label.config(text=check_symbol)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


header_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN)
header_label.grid(column=1, row=0)

checker_label = Label(font=(FONT_NAME, 10), fg=GREEN)
checker_label.grid(column=1, row=3)

button_start = Button(text="Start", font=(FONT_NAME, ), command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", font=(FONT_NAME, ), command=reset_timer)
button_reset.grid(column=2, row=2)



window.mainloop()
