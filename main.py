from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import database

db = database("employee.db")

root = Tk()
root.title("Employee Management System")
root.geometry("1366x768+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

iconImage = PhotoImage(file="22.png")
root.iconphoto(False,iconImage)

# global var
name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

# Entry Frame
entry_frame = Frame(root,bg="#2F4F4F") #2F4F4F
entry_frame.pack(side=TOP,fill=X )

title = Label(entry_frame,text="Employee Management System",font=("century",20,"bold"),bg ="#2F4F4F",fg="white")
title.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="w")

label_name = Label(entry_frame,text="Name",font=("calibri",16,),bg ="#2F4F4F",fg="white")
label_name.grid(row=1,column=0,padx=5,pady=5,sticky="w")
txtName = Entry(entry_frame,textvariable=name,font=("calibri",16,),width=20)
txtName.grid(row=1,column=1,padx=5,pady=5,sticky="w")

label_age = Label(entry_frame,text="Age",font=("calibri",16,),bg ="#2F4F4F",fg="white")
label_age.grid(row=1,column=2,padx=5,pady=5,sticky="w")
txtage = Entry(entry_frame,textvariable=age,font=("calibri",16,),width=20)
txtage.grid(row=1,column=3,padx=5,pady=5,sticky="w")

label_doj = Label(entry_frame,text="D.O.J",font=("calibri",16,),bg ="#2F4F4F",fg="white")
label_doj.grid(row=2,column=0,padx=5,pady=5,sticky="w")
txtdoj = Entry(entry_frame,textvariable=doj,font=("calibri",16,),width=20)
txtdoj.grid(row=2,column=1,padx=5,pady=5,sticky="w")

label_Email = Label(entry_frame,text="Email",font=("calibri",16,),bg ="#2F4F4F",fg="white")
label_Email.grid(row=2,column=2,padx=5,pady=5,sticky="w")
txtEmail = Entry(entry_frame,textvariable=email,font=("calibri",16,),width=20)
txtEmail.grid(row=2,column=3,padx=5,pady=5,sticky="w")

label_Gender = Label(entry_frame,text="Gender",font=("calibri",16,),bg ="#2F4F4F",fg="white")
label_Gender.grid(row=3,column=0,padx=5,pady=5,sticky="w")
ComboBoxGender = ttk.Combobox(entry_frame,textvariable=gender,font=("calibri",16,),width=15,state="readonly")
ComboBoxGender['values'] = ('Male','Female')
ComboBoxGender.grid(row=3,column=1,padx=5,pady=5,sticky="w")

label_Contact = Label(entry_frame,text="Contact",font=("calibri",16,),bg ="#2F4F4F",fg="white")
label_Contact.grid(row=3,column=2,padx=5,pady=5,sticky="w")
txtContact = Entry(entry_frame,textvariable=contact,font=("calibri",16,),width=20)
txtContact.grid(row=3,column=3,padx=5,pady=5,sticky="w")

label_Address = Label(entry_frame,text="Address",font=("calibri",16,),bg ="#2F4F4F",fg="white")
label_Address.grid(row=4,column=0,padx=5,pady=5,sticky="w")
txtAddress = Text(entry_frame,width=75,height=5,font=("calibri",16,))
txtAddress.grid(row=5,column=0,padx=5,pady=5,sticky="w",columnspan=4)

def getData(event):
    selectedRow = treeView.focus()
    data = treeView.item(selectedRow)
    global row
    row = data['values']
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0,END)
    txtAddress.insert(END,row[7])


def displayAll():
    treeView.delete(*treeView.get_children())
    for row in db.fetch() :
        treeView.insert("",END,values=row)

def add_employee():
    if txtName.get() =="" or  txtage.get() == "" or txtdoj.get() == "" or  txtEmail.get() == "" or ComboBoxGender.get() == "" or  txtContact.get() == "" or txtAddress.get(1.0,END) == "":
        messagebox.showerror("Error in Input","Please Fill all the details !" )
    else :
        db.insert( txtName.get() , txtage.get() , txtdoj.get() , txtEmail.get() , ComboBoxGender.get() , txtContact.get(),  txtAddress.get(1.0,END))
        messagebox.showinfo("Success","Record Inserted")
    clear_all()
    displayAll()

def update_employee():
    if txtName.get() == "" or txtage.get() == "" or txtdoj.get() == "" or txtEmail.get() == "" or ComboBoxGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input", "Please Fill all the details !")
    else:
        db.update(row[0]  ,txtName.get(), txtage.get(), txtdoj.get(), txtEmail.get(), ComboBoxGender.get(), txtContact.get(),
                  txtAddress.get(1.0, END))
        messagebox.showinfo("Success", "Record updated")
    clear_all()
    displayAll()


def delete_employee():
    db.remove(row[0])
    clear_all()
    displayAll()



def clear_all():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0,END)


# Btn Frame

btnFrame = Frame(entry_frame,bg ="#2F4F4F")
btnFrame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")
btnAdd = Button(btnFrame,command=add_employee,text="Add Details",width=15,bd=0,fg="white",font=("calibri",16,"bold"),bg="#16a085")\
    .grid(row=0,column=0)
btnEdit = Button(btnFrame,command=update_employee,text="Update Details",width=15,bd=0,font=("calibri",16,"bold"),bg="#2980b9")\
    .grid(row=0,column=1,padx=10)
btnDelete = Button(btnFrame,command=delete_employee,text="Delete Details",width=15,bd=0,font=("calibri",16,"bold"),bg="#FF4500")\
    .grid(row=0,column=2,padx=10) #c0392b
btnClear = Button(btnFrame,command=clear_all,text="Clear Details",width=15,bd=0,font=("calibri",16,"bold"),bg="#f39c12")\
    .grid(row=0,column=3,padx=10)


# Table Frame

tree_frame = Frame(root,bg="#ecf0f1")
tree_frame.place(x=0,y=420,width=1366,height=500)

style = ttk.Style()
style.configure("mystyle.Treeview",font=("calibri",18),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=("calibri",18))

treeView = ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
treeView.heading("1",text="ID")
treeView.column("1",width=25)
treeView.heading("2",text="Name")
treeView.column("2",width=80)
treeView.heading("3",text="Age")
treeView.column("3",width=30)
treeView.heading("4",text="D.O.J")
treeView.column("4",width=80)
treeView.heading("5",text="Email")
treeView.column("5",width=250)
treeView.heading("6",text="Gender")
treeView.column("6",width=50)
treeView.heading("7",text="Contact")
treeView.column("7",width=80)
treeView.heading("8",text="Address")
treeView.bind("<ButtonRelease-1>", getData)
treeView['show'] = 'headings'
treeView.pack(fill=X)


displayAll()
root.mainloop()