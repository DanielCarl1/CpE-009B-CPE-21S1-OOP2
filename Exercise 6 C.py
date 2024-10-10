from tkinter import*

class MyWindow():
    def __init__(self, win):

        self.Label1 = Label(win, fg='Black', text='Simple Calculator', font=25)
        self.Label1.place(x=150, y=50)
        self.Label2 = Label(win, text='Digit 1: ')

        self.Label2.place(x=70, y=80)
        self.Entry1 = Entry(win, bd=3)
        self.Entry1.place(x=150, y=80)

        self.Label3 = Label(win, text='Digit 2: ')
        self.Label3.place(x=70, y=120)
        self.Entry2 = Entry(win, bd=3)
        self.Entry2.place(x=150, y=120)

        self.Label4 = Label(win, text='Result:')
        self.Label4.place(x=70, y=160)
        self.Entry3 = Entry(win, bd=3)
        self.Entry3.place(x=150, y=160)

        self.Button1 = Button(win, fg='Blue',text='Add', command=self.add)
        self.Button1.place(x=80, y=200)
        self.Button1.bind('<Button-1>', self.add)

        self.Button1 = Button(win, fg='Red', text='Subtract', command=self.sub)
        self.Button1.place(x=135, y=200)

        self.Button1 = Button(win, fg='Green', text='Multiply', command=self.mul)
        self.Button1.place(x=210, y=200)

        self.Button1 = Button(win, fg='Black', text='Divide', command=self.div)
        self.Button1.place(x=285, y=200)

        self.Button1 = Button(win, fg='Purple',text='Clear',height='1',width='20', command=self.clear)
        self.Button1.place(x=130, y=240)

    def add(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def sub(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def mul(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def div(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        if num2 !=0:
            result = num1 / num2
        else:
            result = "Error"
        self.Entry3.insert(END, str(result))

    def clear(self):
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)
        self.Entry3.delete(0, END)

window = Tk()
MyWin = MyWindow(window)
window.title('Calculator')

window.geometry('400x300+10+10')
window.configure(bg='Gray')
window.mainloop()