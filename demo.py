from tkinter import *


root = Tk()
root.title('Inventory Management System Login')
root.configure(background='Light Blue')
root.state('zoomed')

def get_entry():
    text = e1.get()
    print(text)
    
e1 = Entry(root,width = 20,font = ('Times New Roman',20))
e1.place(x=0,y=1)
login_button = Button(root, text='LOGIN',width = 30,command=get_entry,background = "light Pink",font=('Times New Roman', 22)).place(x = 1000,y =450)

root.mainloop()