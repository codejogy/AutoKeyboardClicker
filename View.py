# Capa de presentación
# Actualiza Model
import tkinter
import tkinter.ttk as ttk

# ---------------CONSTANTES--------------

HEADINGNAMES = ["Nombre", "HotKey"]
NAMETITLE = "AutoKeyboardClicker"
USE = "En uso"
MADE = "Creados"
ADD = "Agregar"
LIST = "Lista"
DELETE = "Eliminar"
LISTACOLUMNAS = ["hotkey"]
HEIGHTXWIDTH = [200, 300]
LABELTL = "Ingresa HotKey para activar y desactivar"

# ---------------VARIABLES---------------

# Ventana
ventana = tkinter.Tk()
ventana.minsize(HEIGHTXWIDTH[0], HEIGHTXWIDTH[1])
ventana.title(NAMETITLE)
ventana.columnconfigure(0, weight=1)
# ventana.columnconfigure(1,weight=1)
ventana.columnconfigure(2, weight=1)
ventana.rowconfigure(0, weight=1, minsize=100)
ventana.rowconfigure(1, weight=10)


# Ventana TopLevel

ventanaTopLevel = tkinter.Toplevel(ventana)

# Frames secundarios
frame00 = tkinter.LabelFrame(ventana)
frame01 = tkinter.LabelFrame(ventana)  # BOTONES Y TITULO
frame02 = tkinter.LabelFrame(ventana)
frame10 = tkinter.LabelFrame(ventana)  # EN USO / LISTA
frame11 = tkinter.LabelFrame(ventana)  # ENTRE 10 y 12
frame12 = tkinter.LabelFrame(ventana)  # CREADOS

# Frames secundarios TopLevel
frameTL00 = tkinter.LabelFrame(ventanaTopLevel) # Frame de arriba
frameTL01 = tkinter.LabelFrame(ventanaTopLevel) # Frame de abajo

# FRAMES PARA LISTA EN USO Y CREADO
frameLista = tkinter.LabelFrame(ventana, relief="groove")
frameCreado = tkinter.LabelFrame(ventana, relief="groove")
frame10 = frameLista  # DEFINIENDO QUE ES LO MISMO pero inutil
frame12 = frameCreado  # DEFINIENDO QUE ES LO MISMO pero inutil

# LABELS
labelName = tkinter.Label(frame01, text=NAMETITLE)
labelUso = tkinter.Label(frameLista, text=USE)
labelCreados = tkinter.Label(frameCreado, text=MADE)
labelTopLevel = ttk.Label(frameTL00, text=LABELTL)

# BOTONES
botonAgregar = tkinter.Button(frame01, text=ADD)
botonLista = tkinter.Button(frame01, text=LIST)
botonEliminar = tkinter.Button(frame01, text=DELETE)

# LISTBOX
# listBoxLista = tkinter.Listbox(frameLista,height=10)
# listBoxCreados = tkinter.Listbox(frameCreado,height=10)

# TREEVIEW
treeviewLista = ttk.Treeview(frameLista, columns=LISTACOLUMNAS)
treeviewCreador = ttk.Treeview(frameCreado, columns=LISTACOLUMNAS)

# ENTRIES
entryNombre = ttk.Entry(frameCreado)

# TEXT
textHotkey = tkinter.Label(frameCreado)
textTL = ttk.Label(frameTL01)


# ---------------GRIDS[VENTANA]---------------

# FRAMES
frame00.grid(row=0, column=0, sticky="NSEW")
frame00.columnconfigure(0, weight=1)

frame01.grid(row=0, column=1, sticky="NSEW")
frame01.columnconfigure(0, weight=1, minsize="100")

frame02.grid(row=0, column=2, sticky="NSEW")
frame02.columnconfigure(2, weight=1)

frameLista.grid(row=1, column=0, sticky="NSEW")  # LISTA 10
frameLista.columnconfigure(0, weight=1)
frameLista.rowconfigure(1, weight=1)

frame11.grid(row=1, column=1, sticky="NSEW")
frame11.columnconfigure(0, weight=1)

frameCreado.grid(row=1, column=2, sticky="NSEW")  # LISTA 12
frameCreado.columnconfigure(0, weight=1)
frameCreado.rowconfigure(1, weight=1)

# ---------------GRIDS[VENTANATOPLEVEL]---------------

#
frameTL00.grid(row=0,column=0,sticky="NSEW")
frameTL01.grid(row=1,column=0,sticky="NSEW")

# ---------------GRIDS[FRAMES]---------------

# LABELS FRAME01
labelName.grid(row=0, column=0, )

# BOTONES FRAME01
botonAgregar.grid(row=1, column=0, pady=5, )
botonLista.grid(row=2, column=0, pady=5, )
botonEliminar.grid(row=3, column=0, pady=5, )

# LABELS IN FRAMES

labelUso.grid(row=0, column=0)  # FRAME10
labelCreados.grid(row=0, column=0)  # FRAME12

# LISTBOX IN FRAMES

# listBoxLista.grid(row=1,column=0)
# listBoxCreados.grid(row=1,column=0)

# TREEVIEW IN FRAMES

treeviewLista.grid(row=1, column=0, sticky="NSEW")
treeviewCreador.grid(row=1, column=0, sticky="NSEW")

# ---------------GRIDS[VENTANATOPLEVEL]---------------

labelTopLevel.grid(row=0,column=0,sticky="NSEW")
textTL.grid(row=0,column=0,sticky="NSEW")

#---------------TREEVIEW CONFIG [FRAMES]---------------
# Titulos
treeviewLista.heading("#0", text=HEADINGNAMES[0])
treeviewLista.heading(0, text=HEADINGNAMES[1])
treeviewCreador.heading("#0", text=HEADINGNAMES[0])
treeviewCreador.heading(0, text=HEADINGNAMES[1])

# ---------------GRIDS[TOPLEVEL]---------------
ventanaTopLevel.minsize(200,100)
ventanaTopLevel.withdraw() # Hace que no aparezca directamente, sino hasta que iconify sea declarado

# Boton ADD para insertar un item en treeview


# treeviewCreador.insert("","end","widgets",text="Widget tour",values=(["15KB", "CTRL+t"]))
# treeviewCreador.insert("",0,"gallery",text="Applications")
#
# id = treeviewCreador.insert('',"end","tut",text="Tutorial")
#
# treeviewCreador.insert("widgets","end",text="Canvas")
# treeviewCreador.insert(id,"end",text="Tree")
#
# treeviewCreador.move("widgets","gallery","end")
# treeviewCreador.detach("widgets")
# treeviewCreador.move("widgets","",0)
# treeviewCreador.column(0,minwidth=20,)
# treeviewCreador.heading("#0",text="Nombre")
# treeviewCreador.heading("nombre",text="Nombre")
# treeviewCreador.heading("hotkey",text="HotKey")
#
# treeviewCreador.insert("","end",text="button",tags=("ttk","simple"))
# treeviewCreador.tag_configure("ttk",foreground="yellow")
# treeviewCreador.tag_configure("simple",background="green")




# def agregarObjeto():
#
#     return treeviewCreador.insert("",0,text="Prueba1")
# botonAgregar.config(command=agregarObjeto)
