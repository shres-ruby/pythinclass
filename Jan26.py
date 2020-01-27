import tkinter as tk
import tkinter.messagebox as msg

open_tk = tk.Tk()
open_tk.title('My GUI Application')
my_can = tk.Canvas(width=600,height=400,bg='red')
my_can.pack()

def mymessage():
    msg.showinfo('hello', 'kina click gareko?')

my_btn = tk.Button(open_tk,text='click button', command=mymessage)
my_btn.pack()

open_tk.mainloop()