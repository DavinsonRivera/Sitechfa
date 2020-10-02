#Importaciones
from tkinter import *
import tkinter
from tkinter import scrolledtext
from PIL import ImageTk, Image
from tkinter import messagebox

#Crea la ventana principal
ventana = Tk()
ventana.geometry("1095x615")#Tamaño de ventana
ventana.resizable(width=0, height=0)#Bloquea expansion de ventana
ventana.title("SiTechFa")

#Carga imagen de fondo, e imprime en ventana
img1 = PhotoImage(file="Fondo.png")
img2 = PhotoImage(file="Fondo2.png")
fondo = Label(ventana, image=img1)
fondo.pack()#Ubicacion de fondo

#Caja de Usuario
caja_usuario = tkinter.Entry(ventana, width=22)
caja_usuario.place(x=475, y=267)#Ubicacion
caja_usuario.focus()

#Caja de Contraseña
contrasena = tkinter.Entry(ventana, width=22)
contrasena.place(x=475, y=330)#Ubicacion

#Funcion De Inicio. Se activa con el boton Inicio
def Inicio ():
    print("Iniciando")

    #Captura Usuario y Contraseña
    usuario = caja_usuario.get()
    contraseña = contrasena.get()

    print(usuario)
    print(contraseña)

    fondo.configure(image=img2)
    caja_usuario.destroy()
    contrasena.destroy()
    boton_inicio.destroy()

    boton_inventario = tkinter.Button(ventana, text="Inventario")
    boton_inventario.place(x=50, y=200)
    boton_inventario.config(width=15, height=1, bg = "gray")

    boton_inventario = tkinter.Button(ventana, text="Facturacion")
    boton_inventario.place(x=50, y=250)
    boton_inventario.config(width=15, height=1, bg = "gray")

    boton_inventario = tkinter.Button(ventana, text="Reportes")
    boton_inventario.place(x=50, y=300)
    boton_inventario.config(width=15, height=1, bg = "gray")


#Boton inicio
boton_inicio = tkinter.Button(ventana, text="Inicio", command= Inicio)
boton_inicio.place(x=498, y=367)
boton_inicio.config(width=10, height=1, bg = "gray")

ventana.mainloop()
