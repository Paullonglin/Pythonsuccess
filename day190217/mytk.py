#coding=utf-8
import tkinter
top=tkinter.Tk()
lable=tkinter.Label(top,text='在线翻译')
lable.pack()
yuan=tkinter.Text(top)
yuan.pack()
hou=tkinter.Text(top)
hou.pack()
button=tkinter.Button(top,text='百度翻译')
button.pack(side=tkinter.RIGHT)
top.mainloop()