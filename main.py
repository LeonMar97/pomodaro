from tkinter import *
from tkinter import ttk
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
custom_button_style = {
    'bg': GREEN,            # Background color
    'fg': 'black',           # Text color
    'relief': 'raised',     # Button border style ('raised', 'sunken', 'flat', 'ridge', 'solid', 'groove')
    'borderwidth': 5,      # Border width
    'font':("Arial", 12, "bold"),
    
    # 'highlightthickness:0,
}

# ---------------------------- TIMER RESET ------------------------------- # 
timer_string="05:00"
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_time(300)
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_time(c):
    min=f'0{c//60}'
    sec=c%60
    sec=f'0{sec}' if sec<10 else str(sec)
    canvas.itemconfig(text_item,text=min+':'+sec)

    if c>0:
        window.after(1000,count_time,c-1)
    
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100,background=YELLOW)
canvas=Canvas(width=250, height=250,background=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(120,120, image=tomato_img)
text_item=canvas.create_text(120, 130, text=timer_string,fill="white",font=(FONT_NAME,35,"bold "))
canvas.grid(row=1,column=1)
start_button=Button(text="Start",**custom_button_style,command=start_timer)
start_button.grid(row=2,column=0)

Reset_button=Button(text="Reset",**custom_button_style,command=window.update)
Reset_button.grid(row=2,column=2)

window.mainloop()