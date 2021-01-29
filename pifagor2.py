from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import fileinput

root=Tk()
root.geometry("400x300")
root.title("Elemendid Tkinteris")

N=6
tabs=ttk.Notebook(root)
texts=["Esimene","Teine","Kolmas","Neljas","Viies","Kuues"]

def funktion(a):
    tabs.select(a)
def open_():
    file=askopenfilename()
    for text in fileinput.input(file):
        txt_box.insert(0.0,text)

def save_():
    file=asksaveasfile(mode="w",defaultextension=((".txt"),(".docx")),filetypes=(("Notepad",".txt"),("Word",".docx")))
    t=txt_box.get(0.0,END)
    file.whrite(t)
    file.close()

def exit_():
    if askyesno("Exit","Yes/No"):
        showinfo("Exit","Message: Yes")
        root.destroy()
    else:
        showinfo("No")

def image_phone(name):
    global img
    tabs.select(1)
    img=PhotoImage(file=name).subsample(4)
    can.create_image(10,10,image=img,anchor=NW)




#for i in range(6):
#    tab=Frame(tabs)
#    tabs.add(tab,text=texts[i])


tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tabs.add(tab1,text="Esimene")
tabs.add(tab2,text="Teine")
tabs.add(tab3,text="Kolmas")
tabs.add(tab4,text="Neljas")

M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="tabs",menu=m1)
m1.add_command(label="Tab1",accelerator="Command+V",command=lambda:function(0))
m1.add_separator()
m1.add_command(label="Tab2",command=lambda:function(1))
m1.add_command(label="Tab3",command=lambda:function(2))
m1.add_command(label="Tab4",command=lambda:function(3))   

m2=Menu(M,tearoff=0)
M.add_cascade(label="BG Colors",menu=m2)
m2.add_command(label="Yellow",command=lambda:root.config(bg="yellow"))
m2.add_command(label="Orange",command=lambda:root.config(bg="orange"))
m2.add_command(label="Brown",command=lambda:root.config(bg="brown"))
m2.add_command(label="Blue",command=lambda:root.config(bg="blue"))

m3=Menu(M,tearoff=0)
M.add_cascade(label="Image",menu=m2)
m2.add_command(label="dawg")
m2.add_command(label="adios")
m2.add_command(label="eggman")
m2.add_command(label="...")

btn_open=Button(tab1,text="Open",command=open_)
btn_save=Button(tab1,text="Save",command=save_)
btn_exit=Button(tab1,text="Exit",command=exit_)
txt_box=scrolledtext.ScrolledText(tab1,width=40,height=5)
txt_box.grid(row=0,column=0,columnspan=3)
btn_open.grid(row=1,column=0)
btn_open.grid(row=1,column=1)
btn_open.grid(row=1,column=2)

can=Canvas(tab2,width=300,height=200)
img=PhotoImage(file="dawg.png").subsample(4)
can.create_image(10,10,image=img,anchor=NW)

can=Canvas(tab2,width=300,height=200)
img=PhotoImage(file="adios.png").subsample(4)
can.create_image(10,10,image=img,anchor=NW)




can.pack()


tabs.pack(fill="both")
root.mainloop()
