import tkinter as tk
def topla():
    s1 = int(sayi1.get())
    s2 = int(sayi2.get())
    sonuc.configure(text=str(s1 + s2))
def cikarma():
    s1 = int(sayi1.get())
    s2 = int(sayi2.get())
    sonuc.configure(text=str(s1 - s2))
def carpma():
    s1 = int(sayi1.get())
    s2 = int(sayi2.get())
    sonuc.configure(text=str(s1 * s2))
def bolme():
    s1 = int(sayi1.get())
    s2 = int(sayi2.get())
    sonuc.configure(text=str(s1 / s2))

pencere = tk.Tk()
pencere.title("hesap makinesi")
pencere.geometry('320x300')
sonuc = tk.Label(pencere,text="sonuc",font="Courier 16 bold",width=30,justify="center")
sonuc.place(x=50, y=20)
sayi1 = tk.Entry(pencere,font="Courier 16 bold",width=15,justify="right")
sayi1.place(x=70, y=50)
sayi2 = tk.Entry(pencere,font="Courier 16 bold",width=15,justify="right")
sayi2.place(x=70, y=80)
tus1 = tk.Button(pencere, text='+',font="Courier 16 bold", width=10, command=topla)
tus1.place(x=90, y=110)
tus1 = tk.Button(pencere, text='-',font="Courier 16 bold", width=10, command=cikarma)
tus1.place(x=90, y=150)
tus1 = tk.Button(pencere, text='x',font="Courier 16 bold", width=10, command=carpma)
tus1.place(x=90, y=190)
tus1 = tk.Button(pencere, text='/',font="Courier 16 bold", width=10, command=bolme)
tus1.place(x=90, y=230)
sayi1.focus()
pencere.mainloop()