from tkinter import *


root = Tk()
root.title('Inventory Management System Login')
root.configure()
root.state('zoomed')

def get_entry():
    text = e1.get()
    print(text)


l1 = Label(root, text='Welcome to Inventory Management System',background='navy Blue',activebackground = 'Light Blue' ,font=('Times New Roman', 35, 'bold')).place(x = 0,y = 60)

l2 = Label(root, text='User id : ',background='Light pink',activebackground = 'Light Blue' ,font=('Times New Roman', 12)).place(x = 1000,y = 120)

l3 = Label(root, text='Username:',background='Light pink',font=('Times New Roman', 20)).place(x = 1000,y = 200)
e1 = Entry(root,width = 20,font = ('Times New Roman',20))
e1.place(x = 1200,y = 200 )

Password = Label(root, text='Password:',background='Light pink',font=('Times New Roman', 20)).place(x = 1000,y = 300)
e2 = Entry(root,show='*',width = 20,font = ('Times New Roman',20))
e2.place(x = 1200,y = 300 )

forgot_pass = Button(root, text='Forgot Password ?',background = "light Blue",width = 25,font=('Times New Roman', 12)).place(x = 1000,y = 380)

login_button = Button(root, text='LOGIN',width = 30,background = "light Blue",font=('Times New Roman', 22)).place(x = 1000,y =450)

# l4 = Label(root, text="---or---",font=('Times New Roman', 16)).place(x = 1100,y = 530)

l5 = Label(root, text="Don't have an account ?",background='Light pink',font=('Times New Roman', 14)).place(x = 1000,y = 550)

sign_up = Button(root, text='Sign up here',background = "light Blue",font=('Times New Roman', 10)).place(x = 1200,y = 550)


e1 = Entry(root,width = 20,font = ('Times New Roman',20))
e1.place(x=0,y=1)
login_button = Button(root, text='LOGIN',width = 30,command=get_entry,font=('Times New Roman', 22)).place(x = 1000,y =450)

root.mainloop()