from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as messagebox

def nextPage():
    root.destroy()
    import demo
    
def check_credentials():
    # check if the entered username and password match the correct credentials
    if e1.get() == 'Harsh' and e2.get() == 'hmc':
        nextPage()
    else:
        messagebox.showerror("Error", "Invalid Username or password")
        e1.set('')
        e2.set('')



# create a new Tkinter window
root = Tk()
root.title('Inventory Management System Login')
root.configure(background='Light pink')
root.state('zoomed')

# image = PhotoImage(file='inventory.png')
# image = image.zoom(1, 1)
# label = Label(root, image=image).place(x=0, y=0)


# create a label for the username field
l1 = Label(root, text='Login',background='Light pink',activebackground = 'Light Blue' ,font=('Times New Roman', 35, 'bold')).place(x = 1000,y = 60)

l2 = Label(root, text='Welcome! login to use this exciting Inventory Management System',background='Light pink',activebackground = 'Light Blue' ,font=('Times New Roman', 12)).place(x = 1000,y = 120)

l3 = Label(root, text='Username:',background='Light pink',font=('Times New Roman', 20)).place(x = 1000,y = 200)
e1 = Entry(root,width = 20,font = ('Times New Roman',20))
e1.place(x = 1200,y = 200 )

Password = Label(root, text='Password:',background='Light pink',font=('Times New Roman', 20)).place(x = 1000,y = 300)
e2 = Entry(root,show='*',width = 20,font = ('Times New Roman',20))
e2.place(x = 1200,y = 300 )

forgot_pass = Button(root, text='Forgot Password ?',background = "light Blue",width = 25,font=('Times New Roman', 12)).place(x = 1000,y = 380)

login_button = Button(root, text='LOGIN',width = 30,command=check_credentials,background = "light Blue",font=('Times New Roman', 22)).place(x = 1000,y =450)

# l4 = Label(root, text="---or---",font=('Times New Roman', 16)).place(x = 1100,y = 530)

l5 = Label(root, text="Don't have an account ?",background='Light pink',font=('Times New Roman', 14)).place(x = 1000,y = 550)

sign_up = Button(root, text='Sign up here',background = "light Blue",font=('Times New Roman', 10)).place(x = 1200,y = 550)





#c.pack()
# # create an entry field for the username
# username = tk.Entry(root,width = 200,bg = '#fff',background = "light Blue",font = ('Times New Roman',25)).place(x = 1400,y = 400 )
#
# # create a label for the password field
# password_label = tk.Label(root, text='Password:')
# password_label.grid(row=1, column=0)
#
# # create an entry field for the password, with the show='*' option to hide the characters
# password = tk.Entry(root, show='*')
# password.grid(row=1, column=1)
#
# # create a label for the role field
# role_label = tk.Label(root, text='Role:')
# role_label.grid(row=2, column=0)
#
# # create a combobox for the role
# role = ttk.Combobox(root, values=['admin', 'manager', 'employee'])
# role.grid(row=2, column=1)
#
# # create a login button
# login_button = tk.Button(root, text='Login', command=check_credentials)
root.mainloop()
