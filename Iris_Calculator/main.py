from tkinter import *

from math import sqrt


def key(event):
    print('Pressed', repr(event.char))


def Hover_leave(event):
    text = event.widget.cget('text')
    if text.isdigit() or text == '.' or text == 'C':
        event.widget['background'] = 'gray1'
    elif text == '=':
        event.widget['background'] = 'brown4'
    else:
        event.widget['background'] = 'gray7'


def Hover_enter(event):
    text = event.widget.cget('text')
    if text.isdigit() or text == '.' or text == 'C':
        event.widget['background'] = 'gray15'
    elif text == '=':
        event.widget['background'] = 'red3'
    else:
        event.widget['background'] = 'gray13'


def Click(event):
    global scrval
    text = event.widget.cget("text")
    if text == '=':
        if text.isdigit():
            scrval.set(scrval.get())
            screen.update()
        else:
            scrval.set(eval(scrval.get()))
            screen.update()
    else:
        if scrval.get() == '0' and text != '.':
            scrval.set('')
        if text == 'C':
            scrval.set('0')
            screen.update()
        else:
            if text == 'x':
                scrval.set(scrval.get() + '*')
            elif text == '÷':
                scrval.set(scrval.get() + '/')
            elif text == '√x':
                scrval.set(sqrt(int(scrval.get())))
                screen.update()
            elif text == 'Sq':
                scrval.set((int(scrval.get()) ** 2))
            else:
                scrval.set(scrval.get() + text)
                screen.update()


root = Tk()

root.geometry('315x490')

root.title('Iris Calculator')
root.iconbitmap('Icon.ico')

scrval = StringVar()
scrval.set('0')

screen = Entry(root, textvar=scrval, font='segoe 40 bold', justify=RIGHT, bg='gray11', borderwidth=0,
               foreground='white')
screen.pack(fill=X)

fn = Frame(root, bg='gray11')
fn.pack(padx=0, pady=0)


# Making the numpad
b = Button(fn, text='7', font='segoe 25 bold', borderwidth=0, padx=15, pady=2.5, bg='gray1', foreground='white')
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)
b.grid(row=1, column=0, padx=1, pady=1)

b = Button(fn, text='8', font='segoe 25 bold', borderwidth=0, padx=15, pady=2.5, bg='gray1', foreground='white')
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)
b.grid(row=1, column=1, padx=1, pady=1)

b = Button(fn, text='9', font='segoe 25 bold', borderwidth=0, padx=15, pady=2.5, bg='gray1', foreground='white')
b.grid(row=1, column=2, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='4', font='segoe 25 bold', borderwidth=0, padx=15, pady=2.5, bg='gray1', foreground='white')
b.grid(row=2, column=0, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='5', font='segoe 25 bold', borderwidth=0, padx=15, pady=2.5, bg='gray1', foreground='white')
b.grid(row=2, column=1, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='6', font='segoe 25 bold', borderwidth=0, padx=15, pady=2.5, bg='gray1', foreground='white')
b.grid(row=2, column=2, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='1', font='segoe 25 bold', borderwidth=0, padx=15, pady=2.5, bg='gray1', foreground='white')
b.grid(row=3, column=0, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='2', font='segoe 25 bold', borderwidth=0, padx=15, pady=2.5, bg='gray1', foreground='white')
b.grid(row=3, column=1, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='3', font='segoe 25 bold', borderwidth=0, padx=15, pady=2.5, bg='gray1', foreground='white')
b.grid(row=3, column=2, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='0', font='segoe 25 bold', borderwidth=0, padx=15, pady=2.5, bg='gray1', foreground='white')
b.grid(row=4, column=1, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='C', font='segoe 25 bold', borderwidth=0, padx=12, pady=2.5, bg='gray1', foreground='white')
b.grid(row=4, column=0, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)


b = Button(fn, text='.', font='segoe 25 bold', borderwidth=0, padx=19.3, pady=2.5, bg='gray1', foreground='white',
           activebackground='gray11')
b.grid(row=4, column=2, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='=', font='segoe 25 bold', borderwidth=0, padx=126, pady=2.5, bg='brown4', justify=CENTER)
b.grid(row=5, column=0, padx=1, pady=1, columnspan=4, sticky='e')
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='÷', font='segoe 25 bold', borderwidth=0, padx=15, pady=2.5, bg='gray7', foreground='white')
b.grid(row=1, column=3, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='x', font='segoe 25 bold', borderwidth=0, padx=14.7, pady=2.5, bg='gray7', foreground='white')
b.grid(row=2, column=3, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='-', font='segoe 25 bold', borderwidth=0, padx=18.5, pady=2.5, justify=CENTER, bg='gray7',
           foreground='white')
b.grid(row=3, column=3, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='+', font='segoe 25 bold', borderwidth=0, padx=15, pady=2.5, bg='gray7', foreground='white')
b.grid(row=4, column=3, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='%', font='segoe 25 bold', borderwidth=0, padx=48, pady=2.5, bg='gray7', foreground='white')
b.grid(row=0, column=0, padx=1, pady=1, columnspan=2)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='√x', font='segoe 25 bold', borderwidth=0, padx=6, pady=2.5, bg='gray7', foreground='white',
           justify=CENTER)
b.grid(row=0, column=2, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)

b = Button(fn, text='Sq', font='segoe 23 bold', borderwidth=0, padx=4.5, pady=5, bg='gray7', foreground='white',
           justify=CENTER)
b.grid(row=0, column=3, padx=1, pady=1)
b.bind('<Button-1>', Click)
b.bind('<Enter>', Hover_enter)
b.bind('<Leave>', Hover_leave)


root.attributes('-alpha', 0.989)
root.configure(bg='gray11')

root.minsize(317, 475)
root.maxsize(315, 490)
root.mainloop()
