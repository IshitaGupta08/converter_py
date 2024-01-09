from tkinter import*
top=Tk()
top.title("Converter")
top.geometry("500x400")
def ss():
    a=eval(en.get())
    B=a*0.1
    Mm.set(B)
    A=a*100
    M.set(A)
    C=a*1000
    Km.set(C)
    D=a*0.0009765625
    Kb.set(D)
    E=a*0.0009765625
    Mb.set(E)
    F=a*1024
    Gb.set(F)
    H=a*1048576
    gb.set(H)
    I=a*1024
    mb.set(I)
    J=a*0.0009765625
    GB.set(J)

Mm=StringVar()
M=StringVar()
Km=StringVar()
Kb=StringVar()
Mb=StringVar()
Gb=StringVar()
gb=StringVar()
mb=StringVar()
GB=StringVar()
lb=Label(text="Enter number")
lb.place(x=10,y=20)

en=Entry()
en.place(x=100,y=20)

lb1=Label(text="mm to cm")
lb1.place(x=10,y=80)

en1=Entry(textvariable=Mm)
en1.place(x=10,y=100)

lb2=Label(text="m to cm")
lb2.place(x=170,y=80)

en2=Entry(textvariable=M)
en2.place(x=170,y=100)

lb3=Label(text="km to m")
lb3.place(x=350,y=80)

en3=Entry(textvariable=Km)
en3.place(x=350,y=100)

lb4=Label(text="kb to mb")
lb4.place(x=10,y=150)

en4=Entry(textvariable=Kb)
en4.place(x=10,y=170)

lb5=Label(text="mb to gb")
lb5.place(x=170,y=150)

en5=Entry(textvariable=Mb)
en5.place(x=170,y=170)

lb6=Label(text="gb to mb")
lb6.place(x=350,y=150)

en6=Entry(textvariable=Gb)
en6.place(x=350,y=170)

lb7=Label(text="gb to kb")
lb7.place(x=10,y=230)

en7=Entry(textvariable=gb)
en7.place(x=10,y=250)

lb8=Label(text="mb to kb")
lb8.place(x=170,y=230)

en8=Entry(textvariable=mb)
en8.place(x=170,y=250)

lb9=Label(text="gb to tb")
lb9.place(x=350,y=230)

en9=Entry(textvariable=GB)
en9.place(x=350,y=250)

btn=Button(text="Find all",command=ss)
btn.place(x=260,y=20)
