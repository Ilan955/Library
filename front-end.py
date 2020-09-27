from tkinter import *
import backend

def delete_command():
    backend.delete(selected_index[0])
    view_command()
def update_command():
    backend.update(selected_index[0],title_text.get(),aoutur_text.get(),year_text.get(),id_text.get())
    view_command()

def get_selected_row(event):
    global selected_index
    if not list1.curselection():
        pass
    else:
        index=list1.curselection()[0]
        selected_index=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_index[1])
        e2.delete(0,END)
        e2.insert(END,selected_index[2])
        e3.delete(0,END)
        e3.insert(END,selected_index[3])
        e4.delete(0,END)
        e4.insert(END,selected_index[4])


def view_command():
    tup=backend.view()
    list1.delete(0,END)
    for i in tup:
        list1.insert(END,i)

def search_command():
    list1.delete(0,END)
    tup=backend.search(title_text.get(),aoutur_text.get(),year_text.get(),id_text.get())
    for i in tup:
        list1.insert(END,i)

def add_command():
    backend.insert(title_text.get(),aoutur_text.get(),year_text.get(),id_text.get())
    list1.delete(0,END)
    list1.insert(END,"Inserted!")





window=Tk()
window.wm_title("Book store")
l1=Label(window,text="Title")
l2=Label(window,text="Aouthor")
l3=Label(window,text="Year")
l4=Label(window,text="Id")

l1.grid(row=0,column=0)
l2.grid(row=0,column=2)
l3.grid(row=1,column=0)
l4.grid(row=1,column=2)

title_text=StringVar()
aoutur_text=StringVar()
year_text=StringVar()
id_text=StringVar()

e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)
e2=Entry(window,textvariable=aoutur_text)
e2.grid(row=0,column=3)
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)
e4=Entry(window,textvariable=id_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)
b2=Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3)
b3=Button(window,text="Add entry",width=12,command=add_command)
b3.grid(row=4,column=3)
b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)
b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)
b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)
window.mainloop()
