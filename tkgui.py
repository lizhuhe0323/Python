import tkinter
import os
from game import run_game

top = tkinter.Tk()
hello =tkinter.Label(top,text='Hello World!')
hello.pack()

login = tkinter.Button(text='登陆',command=run_game,bg='red',fg='white')
login.pack()
quit = tkinter.Button(top,text='QUIT',
                      command=top.quit,bg='red',fg='white')
quit.pack(fill=tkinter.X,expand=1)

tkinter.mainloop()
