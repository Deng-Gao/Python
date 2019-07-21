import tkinter as tk
window = tk.Tk()
window.title('python')
window.geometry('200x100')

l = tk.Label(window, bg='yellow', width=24, text='Please make your choice!')
l.pack()

def print_select():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')
var1=tk.IntVar()
var2=tk.IntVar()
c1=tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0,
                  command=print_select)
c2=tk.Checkbutton(window,text='C++',variable=var2,onvalue=1,offvalue=0,
                  command=print_select)
c1.pack()
c2.pack()
window.mainloop()

