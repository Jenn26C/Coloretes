#maria jennifer carbajal martinez
from tkinter import *
from tkinter import messagebox as messageBox
from tkinter import ttk
from tkinter import colorchooser as colorChooser 
root=Tk()
root.geometry()

def Cam():
    
    print("#"+colorrs.get()+colorrs2.get()+colorrs3.get())
    x=colorrs.get()+colorrs2.get()+colorrs3.get()
    if len(x)>6:
       Bott.config(text=f'Demasiados numeros')

    elif len(x)<6:
       Bott.config(text=f'Muy pocos numeros')
   
    else:
     ventanaPrincipal.config(bg=("#"+colorrs.get()+colorrs2.get()+colorrs3.get()))
    

colorrs=StringVar()
colorrs2=StringVar()
colorrs3=StringVar()
ventanaPrincipal=Frame(root)
ventanaPrincipal.pack(fill="both", expand=1)

Tit=Label(ventanaPrincipal,text="Introduce un valor de 6 digitos\n Colores",font=("Aurora",25))
Tit.grid(row=1,column=2,padx=5,pady=5)

Rojo=Label(ventanaPrincipal,text="Rojo",font=("Aurora",20))
Rojo.grid(row=3,column=1,padx=5,pady=5)
primercolor=Entry(ventanaPrincipal,textvariable=colorrs,font=("Aurora",10))
primercolor.grid(row=3,column=2,padx=5,pady=5)

verde=Label(ventanaPrincipal,text="verde",font=("Aurora",20))
verde.grid(row=6,column=1,padx=5,pady=5)
segundocolor=Entry(ventanaPrincipal,textvariable=colorrs2,font=("Aurora",10))
segundocolor.grid(row=6,column=2,padx=5,pady=5)

Azul=Label(ventanaPrincipal,text="Azul",font=("Aurora",20))
Azul.grid(row=9,column=1,padx=5,pady=5)
tercercolor=Entry(ventanaPrincipal,textvariable=colorrs3,font=("Aurora",10))
tercercolor.grid(row=9,column=2,padx=5,pady=5)


CamColor=Button(ventanaPrincipal,text="Cambiar color",font=("Aurora",15),command=Cam)
CamColor.grid(row=13,column=2,padx=5,pady=5)

Bott = Label(ventanaPrincipal, text="", font=("Aurora",15))
Bott.grid(row=15, column=2, padx=10, pady=10)


root.mainloop()