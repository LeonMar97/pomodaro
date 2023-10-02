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
custome_text={
    'fg':GREEN,'background':YELLOW,'font':(FONT_NAME,35,'bold'),
}

# ---------------------------- TIMER RESET ------------------------------- # 
timer=None
def reset():
    global timer
    global number_of_work
    number_of_work=0
    window.after_cancel(timer)
    what_to_do_lable.config(text="Timer",fg=GREEN,background=YELLOW,font=(FONT_NAME,35,'bold'))
    canvas.itemconfig(text_item,text='00:00')
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global number_of_work
    number_of_work+=1
    cur_wait_time=None
    
    if number_of_work%8==0:
        what_to_do_lable.config(text="Long Break",fg=PINK,background=YELLOW,font=(FONT_NAME,35,'bold'))
        cur_wait_time=20*60
    elif number_of_work%2==0:
        what_to_do_lable.config(text="Break",fg=RED,background=YELLOW,font=(FONT_NAME,35,'bold'))
        cur_wait_time=300
    else: 
        what_to_do_lable.config(text="WORK",fg=GREEN,background=YELLOW,font=(FONT_NAME,35,'bold'))
        cur_wait_time=25*60
    count_time(cur_wait_time)
            
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_time(start_time_in_seconds):
    min=start_time_in_seconds//60
    min=f'0{min}' if min<10 else str(min)
    sec=start_time_in_seconds%60
    sec=f'0{sec}' if sec<10 else str(sec)
    canvas.itemconfig(text_item,text=min+':'+sec)

    if start_time_in_seconds>0:
        global timer
        timer=window.after(1000,count_time,start_time_in_seconds-1)
    else:
        start_timer()
    
# ---------------------------- UI SETUP ------------------------------- #
timer_string="00:00"
number_of_work=0
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
what_to_do_lable=Label(text="Timer",fg=GREEN,background=YELLOW,font=(FONT_NAME,35,'bold'))
what_to_do_lable.grid(row=0,column=1)
Reset_button=Button(text="Reset",**custom_button_style,command=reset)
Reset_button.grid(row=2,column=2)

window.mainloop()