import math
import tkinter
from tkinter import *
import matplotlib
import numpy
class SStu():
    def __init__(self):
        matplotlib.use("TkAgg")
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        from matplotlib.figure import Figure
        win = Tk()
        f = Figure(figsize=(4, 3), dpi=100)
        a = f.add_subplot(111)
        x=numpy.arange(0,20,1)
        y=numpy.arange(0,20,1)
        a.plot(x,y)
        canvas = FigureCanvasTkAgg(f, win)
        canvas.draw()
        canvas.get_tk_widget().pack()
        canvas._tkcanvas.pack()
        win.mainloop()
#         self.winst=tkinter.Tk()
#         self.winst.title("ss")
#         self.winst.geometry("800x700")
#         # labelstuid=tkinter.Label(self.winst,"stuid")
#         # self.stuid=tkinter.Entry(self.winst)
#         userlabel1 = tkinter.Label(self.winst, text="学号", font=10)
#         userlabel1.grid(row=0, column=0, padx=15, pady=15)
#         self.entry1= tkinter.Entry(self.winst)
#         self.entry1.grid(row=0, column=1)
#         pwdlabel2 = tkinter.Label(self.winst, text="姓名:", font=10)
#         pwdlabel2.grid(row=0, column=2, padx=15, pady=5)
#         self.entry3= tkinter.Entry(self.winst, width=20, show='*')
#         self.entry3.grid(row=0, column=3)
#         pwdlabel4 = tkinter.Label(self.winst, text="电话:", font=10)
#         pwdlabel4.grid(row=0, column=6, padx=15, pady=5)
#         self.entry5 = tkinter.Entry(self.winst)
#         self.entry5.grid(row=0, column=7)
#         self.okbutton = tkinter.Button(self.winst, text='提交', font=10,padx=20)
#         self.okbutton.grid(row=0, column=8)
#         self.winst.mainloop()


