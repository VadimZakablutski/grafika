from tkinter import*
klik=0
def kliker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
def kliker_minus(event):
    global klik
    klik-=1
    lbl.configure(text=klik)
def opt(event):
    global klik
    text=txt.get()
    lbl.configure(text=text)
okno=Tk()#создает окно
okno.title("Okno")#изменяет название окна
okno.geometry("400x500")#меняет размеры окна
knopka=Button(okno,text="Mina olen nupp\nValjuta mind!+",font="Arial 20",
fg="blue",bg="lightblue",height=4,width=20,relief=GROOVE)
#RAISED, SUNKEN
lbl=Label(okno,text="...",font="Arial 20",
fg="purple",bg="lightblue",height=4,width=20,relief=GROOVE)
txt=Entry(okno,font="Arial 20",fg="blue",bg="lightblue",width=20,
justify=CENTER)
txt.bind("<Return>",opt)
knopka.bind("<Button-1>",kliker)
knopka.bind("<Button-3>",kliker_minus)
lbl.pack()#side=LEFT,TOP,RIGHT
knopka.pack()
txt.pack()






okno.mainloop()#показывает окно

