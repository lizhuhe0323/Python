import tkinter
import os
from game import run_game
from login import *


top = tkinter.Tk()
top.title('1944')
top.geometry('500x300+500+200')
#top.iconbitmap('spider_128px_1169260_easyicon.net.ico')
hello =tkinter.Label(top,text='1944打飞机游戏')
hello.pack()

login = tkinter.Button(text='登陆',command=show_menu,bg='red',fg='white')
login.pack()
score = tkinter.Button(text='最高分数')
score.pack()
quit = tkinter.Button(top,text='退出',
                      command=top.quit,bg='red',fg='white')
quit.pack()

tkinter.mainloop()
