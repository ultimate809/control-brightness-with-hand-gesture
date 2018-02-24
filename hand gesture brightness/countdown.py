import tkinter as tk
from tkinter import *
import time

def countdown(i):
    label=Label(w, text=str(i))
    label.place(relx=0.45, rely=0.45)
    label.configure(font=("Courier", 40),foreground='blue',background='green')
    

w = tk.Tk()
w.geometry("350x350")
label1=Label(w, text="Shaurya ne banaya hai")
label1.place(relx=0.58, rely=0.95)
w.configure(background='red')

w.after(0, lambda: countdown(3) )
w.after(1000, lambda: countdown(2) )
w.after(2000, lambda: countdown(1) )
w.after(3000, lambda: countdown("GO") )
w.after(3200, lambda: w.destroy() )
w.mainloop()


