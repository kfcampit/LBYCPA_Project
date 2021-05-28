import tkinter as tk
import tkinter as ttk
import time as tm
from tkinter import messagebox
global setalarm
setalarm="hh:mm:ss:nn"
def display_time():
    global setalarm
    global current_time
    current_time=tm.strftime('%I:%M:%S:%p')
    if setalarm in current_time:
        messagebox.askquestion("Confirm","Are you sure?")
    clock_label ['text'] = current_time
    clock_label.after(200,display_time)

my_window = tk.Tk()
my_window.title('Current Time')
clock_label=tk.Label(my_window,font='ariel 80', bg='black',fg='red')
clock_label.grid(row=0,column=0)

def pogimatt():
    global setalarm
    global current_time
    setalarm=alarm.get()
    pass
ttk.Button(my_window, text = "Covid Tracker", command = pogimatt, width = 16).grid(column = 2, row = 2, pady = 4, padx = 8)
alarm = tk.StringVar()
tk.Entry(my_window, textvariable=alarm).grid(column=2, row=3)

display_time()
my_window.mainloop()
