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
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer_text)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_marks.config(text="")
    global reps, timer
    reps = 0
    timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    minutes = 60
    if reps % 8 == 0:
        minutes *= LONG_BREAK_MIN
        title.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        minutes *= SHORT_BREAK_MIN
        title.config(text="BREAK", fg=PINK)
    else:
        minutes *= WORK_MIN
        title.config(text="WORK", fg=GREEN)

    countdown(minutes)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec == 0:
        sec = "00"
    elif sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    elif count == 0:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Create a window of 100x50 pixels and a yellow background color
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Create a timer label
title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title.grid(column=1, row=0,)

# Creates an image of a tomato and the timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Create a start and reset button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=3, row=2)


# Create check marks
check_marks = Label(text="", bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)
window.mainloop()
