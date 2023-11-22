import tkinter as tk
from tkinter import ttk
import win32api
from win32api import GetSystemMetrics
from tkinter import font
from calendar import month_name


main = tk.Tk()
main.title("Tution payment Calculator")
#main.iconbitmap("logo.ico")
screen_width = GetSystemMetrics(0)  #/screen_width = root.winfo_screenwidth()
screen_height = GetSystemMetrics(1) #screen_height = root.winfo_screenwidth()
window_width = 300
window_height = 300
x_position = (screen_width/2 ) - (window_width/2)
y_position = (screen_height/2) - (window_height/2)

#print(screen_height)
#print(screen_width)
main.geometry(f'{window_width}x{window_height}+{int(x_position)}+{int(y_position)}')
main.resizable(False,False)

scale_var = tk.IntVar(value=50)
scale = ttk.Scale(main, from_=0,to=100, orient="horizontal", variable=scale_var)
scale.pack()

progress = ttk.Progressbar(main, variable=scale_var)
progress.pack()

label_1 = ttk.Label(main, textvariable=scale_var)
label_1.pack()
tk.mainloop()