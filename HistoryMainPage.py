import tkinter as tk
from functools import partial

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, *kwargs)

root = tk.Tk()
root.title("Question generator")

lbl = tk.Label(root, text='History').grid(row=1, column=1)
btn = tk.Button(root, text='Question Bank').grid(row=2, column=1)
btn2 = tk.Button(root, text='Take Quiz').grid(row=4, column=1)
btn3 = tk.Button(root, text='Exit', command=quit).grid(row=5, column=0)
btn4 = tk.Button(root, text='Home').grid(row=0, column=0)

root.mainloop()