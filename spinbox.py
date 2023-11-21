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

value_1 = tk.StringVar()
month =[month_name[i] for i in range(1, 13)]

spb_1 = ttk.Spinbox(main, values=month, textvariable=value_1)
spb_1.pack()

label_1 = ttk.Label(main,textvariable=value_1)
label_1.pack()

spb_2 = ttk.Spinbox(main, from_=5,to=20,increment=3)
spb_2.pack()
tk.mainloop()