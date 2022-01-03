import tkinter as tk
from functools import partial

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, *kwargs)

root = tk.Tk()
root.title("Question generator")

lbl = tk.Label(root, text='Select a subject to start').grid(row=1, column=1)
btn = tk.Button(root, text='Sports (Cricket)', fg='blue', bg='white').grid(row=2, column=1)
btn2 = tk.Button(root, text='Media (Avengers movie)', fg='blue', bg='white').grid(row=3, column=1)
btn3 = tk.Button(root, text='History', fg='blue', bg='white').grid(row=4, column=1)
btn4 = tk.Button(root, text='Exit', command=quit, fg='white', bg='red').grid(row=5, column=0)

root.mainloop() # This will close the
