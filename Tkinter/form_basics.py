from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox

def quit():
    exit()

def abt():
    tkinter.messagebox.showinfo("About","Demo")

def show():
    first = fn.get()
    last = ln.get()
    born = dob.get()
    country = var.get()
    lang = lang1.get()
    lang = lang2.get()
    sex =  m.get()
    print("Full Name: {} {}".format(first,last))
    print("DOB: ", born)
    print("Country: ",country)
    print("Languages: ", lang)
    print("Gender: ", sex)

def nextwin():
    newwin = Tk()
    newwin.title("Login")
    newwin.geometry("250x250")
    l1 = Label(newwin, text="Registration Completed!", relief="solid",font=("arial",12,"bold"))
    l1.place(x=30, y=70)
    bt1 = Button(newwin, text="Demo",width=12, bg="brown", fg="white",command=quit)
    bt1.place(x=80, y=110)

window = Tk()
window.geometry("500x600")
window.title("Registration Form")

image = Image.open("images/logo1.png")
photo = ImageTk.PhotoImage(image)
imlab = Label(image=photo)
imlab.pack()

menu = Menu(window)
window.config(menu=menu)
sub1 = Menu(menu)
menu.add_cascade(label="File", menu=sub1)
sub1.add_command(label="Exit", command=quit)
sub2 = Menu(menu)
menu.add_cascade(label="Options", menu=sub2)
sub2.add_command(label="About", command=abt)

fn = StringVar()
ln = StringVar()
dob = StringVar()
var = StringVar()
lang1 = StringVar()
lang2 = StringVar()
m = StringVar()

head = Label(window, text="Registration Form", relief="solid", width=20, font=("arial",19,"bold"))
head.place(x=90, y=220)

label1 = Label(window, text="First Name :", width=20, font=("arial",10,"bold"))
label1.place(x=80, y=260)

entry1 = Entry(window, textvar=fn)
entry1.place(x=260,y=262)

label2 = Label(window, text="Last Name :", width=20, font=("arial",10,"bold"))
label2.place(x=80, y=300)

entry2 = Entry(window, textvar=ln)
entry2.place(x=260,y=302)

label3 = Label(window, text="DOB :", width=20, font=("arial",10,"bold"))
label3.place(x=60, y=340)

entry3 = Entry(window, textvar=dob)
entry3.place(x=260,y=342)

label4 = Label(window, text="Country :", width=20, font=("arial",10,"bold"))
label4.place(x=70, y=380)

list1 = ['India','Nepal','Chaina','America','Japan','Indoneshia','Bangladesh']
droplist = OptionMenu(window, var, *list1)
var.set("Select Country")
droplist.config(width=15)
droplist.place(x=260, y=382)

label5 = Label(window, text="Prog Lang :", width=20, font=("arial",10,"bold"))
label5.place(x=80, y=420)
ch1 = Checkbutton(window, text="Java", variable=lang1)
ch1.place(x=260, y=420)
ch1 = Checkbutton(window, text="Python", variable=lang2)
ch1.place(x=340, y=420)

label6 = Label(window, text="Gender :", width=20, font=("arial",10,"bold"))
label6.place(x=70, y=460)
rb1 = Radiobutton(window, text="Male", variable=m, value="Male")
rb1.place(x=260, y=460)
rb2 = Radiobutton(window, text="Female",variable=m, value="Female")
rb2.place(x=260, y=480)

b1 = Button(window, text="Signup", width=12, bg="brown", fg="white", command=show)
b1.place(x=150, y=520)

b2 = Button(window, text="Login", width=12, bg="brown", fg="white", command=nextwin)
b2.place(x=280, y=520)

b3 = Button(window, text="Quit", width=12, bg="brown", fg="white", command=quit)
b3.place(x=220, y=560)

window.mainloop()