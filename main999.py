from tkinter import *
from tkinter import ttk
def comboclick(event):
    z=cb.get()
    prnt = label("enter the value of a \nenter the value of b")
    prnt.pack()

window=Tk()
window.resizable (width="false",height="false")
window.title("PROJECT")
header=Label(window,text="SRMV PTC DIT",bg="red",fg="black",padx=50,pady=25,font=("arial",40,"italic"))
header.pack(fill=X)
window.geometry("800x600")
window.config(bg="lightblue",)
window.title("DIT PROJECT")
cb=ttk.Combobox(window,width=50,height=80,state="readonly")
cb['values']=("(a+b)^2","(a+b)^2","(a+b)^3","(a-b)^3","(a)^3+(b)^3","(a)^3+(b)^3","(a+b+c)^2","(a-b-c)^2")
cb.current(0)
cb.bind("<<comboboxselected>>",comboclick)
cb.pack(pady=50)

window.mainloop()
