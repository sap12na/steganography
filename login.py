# from cProfile import label
# from cgitb import text
from tkinter import *
from tkinter import messagebox as mb
from turtle import heading
import mysql.connector


root = Tk()

def login():
    conn=mysql.connector.connect(host='localhost',user='root',password='',database='minor')
    cr=conn.cursor()
    username=user.get()
    psw=pas.get()
    cr.execute("select * from admin where username='"+username+"'and psw='"+psw+"'")
    if user.get()== "" or pas.get()=="":
        mb.showerror("Error","You need to fill the form")
    elif(cr.fetchone()):
        mb.showinfo("success","Welcome")
        root.destroy()
        import data_hide 
    else:
        mb.showerror("Error","your data not found")    

root.title("Login")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)

img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame= Frame(root, width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text='Login in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

###################################------------------------------------------
def on_enter(e):
    user.delete(0, 'end')
    
def on_leave(e):
    name=user.get()
    if name == '':
        user.insert(0, 'Email id')    
user = Entry(frame,width=25,fg='black',border=0,bg='white', font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Email id')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295,height=2,bg='black').place(x=25,y=107)

###################################------------------------------------------


def on_enter(e):
    pas.delete(0, 'end')
    
def on_leave(e):
    name=pas.get()
    if name == '':
        pas.insert(0, 'Password')
        
pas = Entry(frame,width=25,fg='black',border=0,bg='white', font=('Microsoft YaHei UI Light',11))
pas.place(x=30,y=150)
pas.insert(0,'Password')
pas.config(show="*")
pas.bind('<FocusIn>', on_enter)
pas.bind('<FocusOut>', on_leave)

Frame(frame, width=295,height=2,bg='black').place(x=25,y=177)

###################################------------------------------------------

Button(frame,width=39,pady=7,text='Login', bg='#57a1f8', fg='white', border=0,command=login).place(x=35 ,y=214 )


root.mainloop()