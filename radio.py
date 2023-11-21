import tkinter as tk
from tkinter import ttk
import win32api
from win32api import GetSystemMetrics
from tkinter import font

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

frame_1=tk.LabelFrame(main,text="select",padx=30, pady=10)
frame_1.pack()
radio_1 = ttk.Radiobutton(frame_1, text="python", value="Python" , variable=value_1)
radio_1.pack(anchor="w", pady=5)

radio_2 = ttk.Radiobutton(frame_1, text="java", value="Java", variable=value_1 )
radio_2.pack(anchor="w", pady=5)

radio_3 = ttk.Radiobutton(frame_1, text="C++", value="c++", variable=value_1)
radio_3.pack(anchor="w", pady=5)

label_1 = ttk.Label(frame_1, textvariable=value_1)
label_1.pack()

tk.mainloop()