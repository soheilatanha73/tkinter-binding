from tkinter import *
def func1(event,a,b):
    print('enter button',a,b)#a,b able us to give amount variable with bind
def func2(event,b):
    print('enter label')
def func3(event):
    print('enter to windows')
def func4(event):
    print('leave windows')

win = Tk()

win.geometry('300x200+900+150')
win.resizable(False, False)
win.configure(bg='pink')
win.iconbitmap('icon2.ico')
win.title('*** soheila ***')

lbl = Label(win,
            text='salam',
            height=2,
            width=9,
            bg='yellow',
            font=('Tahoma', 15,'bold'))

btn=Button(win,
           text='press me!',
           height=2,
           width=8,
           bg='lightgreen',
           font=('Tahoma',12),
           command= lambda:print('hellllllooo'),
           relief='raised',
           cursor='dot')
btn.place(x=100,y=80)
lbl.place(x=80,y=5)
btn.bind('<Enter>', lambda event:func1(event,5,6))#this par I enter some value with bind
#btn.bind('<Enter>', lambda event:func1(event,'button'))
lbl.bind('<Enter>',lambda event:func2(event,'bind'))
win.bind('<Enter>',func3)
win.bind('<Leave>',func4)
           
           

win.mainloop()
