from tkinter import*
klik=0
def kliker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
    okno.geometry(str(okno.winfo_width()+10)+"x"+str(okno.winfo_height()+10))
def kliker_minus(event):
    global klik
    klik-=1
    lbl.configure(text=klik)
    okno.geometry(str(okno.winfo_width()-10)+"x"+str(okno.winfo_height()-10))
def kliks(event):
    global klik
    klik=0
    lbl.configure(text=klik)
def opt(event):
    global klik
    text=txt.get()
    lbl.configure(text=text)
    txt.delete(0,END)
def valik(event):
    valik=var.get()
    lbl.configure(text=valik)
    txt.delete(0,valik)
    txt.insert(0,valik)
def Destroy(event):
    okno.destroy()
okno=Tk()#создает окно
okno.title("Okno")#изменяет название окна
okno.geometry("400x500")#меняет размеры окна
knopka=Button(okno,text="Mina olen nupp\nValjuta mind!",font="Arial 20",
fg="blue",bg="lightblue",height=4,width=20,relief=GROOVE)
#RAISED, SUNKEN
knopka2=Button(okno,text="Сброс",font="Arial 20",
fg="red",bg="lightblue",height=4,width=20,relief=RAISED)
knopka3=Button(okno,text="Выход",font="Arial 20",
fg="pink",bg="lightblue",height=4,width=20,relief=RAISED)
lbl=Label(okno,text="...",font="Arial 20",
fg="purple",bg="lightblue",height=4,width=20,relief=GROOVE)
txt=Entry(okno,font="Arial 20",fg="blue",bg="lightblue",width=20,
justify=CENTER)
i1=PhotoImage(file="1.png")
i2=PhotoImage(file="2.png")
i3=PhotoImage(file="3.png")
r1=Radiobutton(okno,image=i1)
r2=Radiobutton(okno,image=i2)
r3=Radiobutton(okno,image=i3)
txt.bind("<Return>",opt)
knopka2.bind("<Button-1>",kliks)
knopka3.bind("<Button-1>",Destroy)
knopka.bind("<Button-1>",kliker)
knopka.bind("<Button-3>",kliker_minus)
lbl.pack()#side=LEFT,TOP,RIGHT
knopka.pack()
knopka2.pack()
knopka3.pack()
txt.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)






okno.mainloop()#показывает окно

