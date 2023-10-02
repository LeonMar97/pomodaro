from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Widget Examples")
window.config(padx=100,pady=100,background=YELLOW)
canvas=Canvas(width=250, height=250,background=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(120,120, image=tomato_img)
canvas.create_text(120, 130, text='00:00',fill="white",font=(FONT_NAME,35,"bold "))

canvas.grid(row=1,column=1)




window.mainloop()