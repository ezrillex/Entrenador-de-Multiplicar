import tkinter
import numpy
import random
import winsound
import time


# CARGA DE LOS ARCHIVOS .DAT

# Creacion de matriz 12*12 con las respuestas de las tablas de multiplicar.
tablas_de_multiplicar = numpy.zeros((12,12),int)
for x in range (12):
    for y in range (12):
        tablas_de_multiplicar[x][y] = (x+1)*(y+1)

# Cargar el numero de aciertos y si no encuentra el archivo lo crea y lo establece en 0
try:
    aciertos = numpy.load("aciertos.dat")
except FileNotFoundError:
    aciertos = numpy.zeros(1,int)
    aciertos.dump("aciertos.dat")

# Cargar el numero de fallos y si no existe crearlo con el valor de 0
try:
    fallos = numpy.load("fallos.dat")
except FileNotFoundError:
    fallos = numpy.zeros(1,int)
    fallos.dump("fallos.dat")

# cargar matriz previa de confidence y si no existe crearlo
try:
    confianza = numpy.load("confianza.dat")
except FileNotFoundError:
    confianza = numpy.full((12, 12), 1, int)
    confianza.dump("confianza.dat")

# Carga de el valor historico ( numero de ejercicios ) y si no existe crearlo.
try:
    historico = numpy.load("historico.dat")
except FileNotFoundError:
    historico = numpy.zeros(1,int)
    historico.dump("historico.dat")

# DEFINICION DE FUNCIONES DE LA LOGICA DEL PROGRAMA (LOS CALCULOS)

# funcion para verificar la respuesta y contar el acierto
def revisar(respuesta,checkX,checkY):
    if respuesta == tablas_de_multiplicar[checkX][checkY]:
        confianza[checkX][checkY] = confianza[checkX][checkY] + 1
        print("CORRECTO!")
        winsound.PlaySound("ding.wav", winsound.SND_ASYNC)
        global aciertos
        aciertos = aciertos + 1

        randomness = random.randint(1, 10000)
        global ejercicio
        global x
        global y
        ejercicio = ""
        if randomness <= highlight:

            # random exercise
            x = random.randint(1, 12)
            y = random.randint(1, 12)

            print(" ")
            print(x, " * ", y, " = ?")

            ejercicio = "     " + ejercicio + str(x) + " * " + str(y) + " = ?"
            salida_ejercicio.delete(0.0, tkinter.END)
            salida_ejercicio.insert(tkinter.END, ejercicio)

        else:
            # review exercise
            factores = numpy.unravel_index(numpy.argmin(confianza), confianza.shape)

            print(" ")
            print(factores[0] + 1, " * ", factores[1] + 1, " = ?")

            ejercicio = "     " + ejercicio + str(factores[0] + 1) + " * " + str(factores[1] + 1) + " = ?"
            salida_ejercicio.delete(0.0, tkinter.END)
            salida_ejercicio.insert(tkinter.END, ejercicio)
    else:
        print("NOO! ERA ", tablas_de_multiplicar[checkX][checkY])
        winsound.PlaySound("buzz.wav", winsound.SND_ASYNC)
        if confianza[checkX][checkY] > 1:
            confianza[checkX][checkY] = confianza[checkX][checkY] - 1
        global fallos
        fallos = fallos + 1

        randomness = random.randint(1, 10000)
        ejercicio
        ejercicio = ""
        if randomness <= highlight:

            # random exercise
            x = random.randint(1, 12)
            y = random.randint(1, 12)

            print(" ")
            print(x, " * ", y, " = ?")

            ejercicio = "     " + ejercicio + str(x) + " * " + str(y) + " = ?"
            salida_ejercicio.delete(0.0, tkinter.END)
            salida_ejercicio.insert(tkinter.END, ejercicio)

        else:
            # review exercise
            factores = numpy.unravel_index(numpy.argmin(confianza), confianza.shape)

            print(" ")
            print(factores[0] + 1, " * ", factores[1] + 1, " = ?")

            ejercicio = "     " + ejercicio + str(factores[0] + 1) + " * " + str(factores[1] + 1) + " = ?"
            salida_ejercicio.delete(0.0, tkinter.END)
            salida_ejercicio.insert(tkinter.END, ejercicio)
    #borrar el entry para que no tenga que hacerlo el usuario
    entrada_respuesta.delete(0, tkinter.END)


# hacemos que el historico determine highlight, es decir la probabilidad para randomness que sea aleatorio o de repaso
if historico >= 0 or historico < 288:
    highlight = 10000
elif historico >=288 or historico > 576:
    highlight = 9000
elif historico >= 576 or historico < 1152:
    highlight = 8000
elif historico >= 1152 or historico < 2304:
    highlight = 7000
elif historico >= 2304 or historico < 4608:
    highlight = 6000
elif historico >= 4608 or historico < 9216:
    highlight = 5000
elif historico >= 9216 or historico < 18432:
    highlight = 4000
elif historico >= 18432 or historico < 36864:
    highlight = 3000
elif historico >= 36864:
    highlight = 2000
else:
    print("Error en la logica interna, el valor historico no es valido! ¿Será negativo?")


# para poder sacar el ejercicio de la funcion necesito inicializar ejercicio y agarrarlo con global
ejercicio = ""

# CODIGO DE LA GUI

def click_1():
    print("clic 1")
    winsound.PlaySound("click_single.wav", winsound.SND_ASYNC)
    frame_1.forget()
    frame_2.pack()

    randomness = random.randint(1, 10000)
    global ejercicio
    global x
    global y
    ejercicio = ""
    if randomness <= highlight:

        # random exercise
        x = random.randint(1, 12)
        y = random.randint(1, 12)

        print(" ")
        print(x, " * ", y, " = ?")

        ejercicio = "     " + ejercicio + str(x) + " * " + str(y) + " = ?"
        salida_ejercicio.delete(0.0,tkinter.END)
        salida_ejercicio.insert(tkinter.END, ejercicio)

    else:
        # review exercise
        factores = numpy.unravel_index(numpy.argmin(confianza), confianza.shape)

        print(" ")
        print(factores[0] + 1, " * ", factores[1] + 1, " = ?")

        ejercicio = "     " + ejercicio + str(factores[0]+1) + " * " + str(factores[1]+1) + " = ?"
        salida_ejercicio.delete(0.0,tkinter.END)
        salida_ejercicio.insert(tkinter.END, ejercicio)


def revisar_enter(event):
    print("revisando enter")
    temporal = entrada_respuesta.get()
    temporal = float(temporal)
    temporal = int(temporal)
    respuesta = temporal
    revisar(respuesta,x-1,y-1)
    historico[0] = historico[0] + 1


def revisar_click():
    print("revisando clic")
    temporal = entrada_respuesta.get()
    print(temporal)
    temporal = int(temporal)
    print(temporal)
    respuesta = temporal
    revisar(respuesta, x - 1, y - 1)
    historico[0] = historico[0] + 1

def click_2():
    print("clic 2")
    confianza.dump("confianza.dat")
    historico.dump("historico.dat")
    aciertos.dump("aciertos.dat")
    fallos.dump("fallos.dat")

    label_3 = tkinter.Label(frame_3, text=historico, bg="black", fg="white", font="none 24 bold").grid(column=0, row=2)
    label_5 = tkinter.Label(frame_3, text=aciertos, bg="black", fg="white", font="none 24 bold").grid(column=1, row=2)
    label_7 = tkinter.Label(frame_3, text=fallos, bg="black", fg="white", font="none 24 bold").grid(column=2, row=2)
    label_9 = tkinter.Label(frame_3, text=confianza, bg="black", fg="white", font="none 15 normal").grid(column=1, row=5)

    winsound.PlaySound("click_single.wav", winsound.SND_ASYNC)
    frame_1.forget()
    frame_3.pack()
    # Guarda si entra a ver las estadisticas para que se actualizen



def click_3():
    print("clic 3")
    winsound.PlaySound("click_single.wav", winsound.SND_ASYNC)
    frame_3.forget()
    frame_1.pack()

def click_4():
    print("clic 4")
    winsound.PlaySound("click_single.wav",winsound.SND_ASYNC)
    confianza.dump("confianza.dat")
    historico.dump("historico.dat")
    aciertos.dump("aciertos.dat")
    fallos.dump("fallos.dat")
    time.sleep(1)
    ventana.destroy()
    exit()

def click_5():
    print("clic 5")
    winsound.PlaySound("click_single.wav", winsound.SND_ASYNC)
    frame_2.forget()
    frame_1.pack()

# Creacion de la ventana, y algunas configuraciones iniciales.
ventana = tkinter.Tk()
ventana.title("Entrenador de Tablas de Multiplicar v.1.3 ALPHA")
ventana.configure(bg="black")
windowframe = tkinter.Frame(ventana,bg="black")

frame_1 = tkinter.Frame(windowframe,bg="black")
frame_1.pack()

# Logo del entrenador (Placeholder, no definitivo)
logo_object = tkinter.Label(frame_1,text="ENTRENADOR DE TABLAS\nDE MULTIPLICAR",bg="black",fg="white",font="none 48 bold").grid(column=0,row=0)
frame_1.grid_rowconfigure(1,minsize=25)
tkinter.Button(frame_1,text=">PRACTICAR<",command=click_1,bg="black",fg="white",relief=tkinter.FLAT,font="none 36 bold").grid(row=2,column=0)

# Icons made by http://www.freepik.com | www.flaticon.com is licensed by Creative Commons 3.0
# https://www.flaticon.com/free-icon/business-statistics-graphic_39915
imagen_estadistica_boton = tkinter.PhotoImage(file="estadistica.png")
tkinter.Button(frame_1,image=imagen_estadistica_boton,command=click_2,bg="black",relief=tkinter.FLAT).grid(row=3,column=0,sticky=tkinter.SW)
imagen_guardar = tkinter.PhotoImage(file="save_icon.png")
tkinter.Button(frame_1,image=imagen_guardar,bg="black",fg="white",relief=tkinter.FLAT,command=click_4).grid(row=3,column=0,sticky=tkinter.SE)

frame_2 = tkinter.Frame(windowframe, bg="black")

frame_2.rowconfigure(1,minsize=30)
frame_2.rowconfigure(4,minsize=30)

#tkinter.Label(frame_2,text="ejercicio aqui",bg="black",fg="white",font="none 48 bold").grid(column=0,row=0)

salida_ejercicio = tkinter.Text(frame_2,width=12,height=0,background="black",fg="white",font="none 48 bold",relief=tkinter.FLAT)
salida_ejercicio.grid(row=0,column=0,sticky=tkinter.N)

# salida_ejercicio.insert(tkinter.END,ejercicio)
print(" ejercicio : ", ejercicio)
# salida_ejercicio.config(state=tkinter.DISABLED)

entrada_respuesta = tkinter.Entry(frame_2,width=5,bg="white",fg="black",font="none 36 bold")
entrada_respuesta.grid(row=2,column=0,sticky=tkinter.S)

tkinter.Button(frame_2,text="REVISAR",command=revisar_click,bg="black",fg="white",font="none 24 bold").grid(row=5,column=0,sticky=tkinter.S)
ventana.bind('<Return>',revisar_enter)

imagen_atras_boton = tkinter.PhotoImage(file="flecha_atras.png")
tkinter.Button(frame_2,image=imagen_atras_boton,command=click_5,bg="black",relief=tkinter.FLAT).grid(row=6,column=0,sticky=tkinter.SW)


frame_3 = tkinter.Frame(windowframe,bg="black")
frame_3.grid_rowconfigure(3,minsize=27)
# imagen_atras_boton = tkinter.PhotoImage(file="flecha_atras.png")
tkinter.Button(frame_3,image=imagen_atras_boton,command=click_3,bg="black",relief=tkinter.FLAT).grid(row=6,column=0,sticky=tkinter.SW)

label_1 = tkinter.Label(frame_3,text="ESTADISTICAS",bg="black",fg="white",font="none 48 bold").grid(column=1,row=0)
label_2 = tkinter.Label(frame_3,text="Ejercicios",bg="black",fg="white",font="none 24 bold").grid(column=0,row=1)
label_3 = tkinter.Label(frame_3,text=historico,bg="black",fg="white",font="none 24 bold").grid(column=0,row=2)
label_4 = tkinter.Label(frame_3,text="Aciertos",bg="black",fg="white",font="none 24 bold").grid(column=1,row=1)
label_5 = tkinter.Label(frame_3,text=aciertos,bg="black",fg="white",font="none 24 bold").grid(column=1,row=2)
label_6 = tkinter.Label(frame_3,text="Fallos",bg="black",fg="white",font="none 24 bold").grid(column=2,row=1)
label_7 = tkinter.Label(frame_3,text=fallos,bg="black",fg="white",font="none 24 bold").grid(column=2,row=2)
label_8 = tkinter.Label(frame_3,text="ACIERTOS POR TABLA",bg="black",fg="white",font="none 30 bold").grid(column=1,row=4)
label_9 = tkinter.Label(frame_3,text=confianza, bg="black",fg="white",font="none 15 normal").grid(column=1,row=5)

# Version text
texto_upper_left = "Version 1.3 ALPHA"
tkinter.Label(ventana,text=texto_upper_left,bg="black",fg="white").pack(anchor=tkinter.NW)
windowframe.pack()
ventana.minsize(width=1000,height=700)
ventana.mainloop()