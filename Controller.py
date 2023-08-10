# REQUEST / RESPONSE
# Va a actualizar View
# Va a actualizar Model
import time

from Model import *


import View
import json
import os
# -----------CONSTANTES-----------
HOTKEYPATH = "hotkeys.js"
PATH = os.path.join("data")
PATHJS = os.path.join(PATH,HOTKEYPATH)

# -----------CLASES---------------
class Initialize:
    def __init__(self):
        #Asignar variables

        self.ventana = View.ventana
        self.boton = View.botonAgregar
        self.list = View.botonLista
        self.entryName = View.entryNombre
        self.treeCreador = View.treeviewCreador
        self.botonEliminar = View.botonEliminar
        self.treeLista = View.treeviewLista
        self.textHotkey = View.textHotkey

        # Configuración
        self.boton.configure(command=self.agregar)
        self.botonEliminar.configure(command=self.deleteItem)
        self.listBoton = self.loadData()

        # Crear binds
        # self.treeCreador.bind("<Double-1>",lambda e:self.checkEvents(e))
        self.treeCreador.bind("<1>",lambda e:self.checkEventsTree(e))

        # Variables
        self.num = self.valID() # Para los valores por defecto
        self.time = time.time()
        self.boolTimer = False
        self.segundoClick = time.time()
        self.primerClick = time.time()
        
        #Creado exclusivamente para el método keyBuffer
        self.buffTimeFirst = time.time()
        self.buffTimeSecond = 0
        self.boolbuffer = False
        
        # -----------COMENZAR-----------
    def start(self):
        self.ventana.mainloop()

        # -----------MÉTODO PARA agregar-----------
    def valID(self):
        if self.listBoton == {}:
            return 0
        x = list(self.listBoton.keys())[-1] # Escoger el último valor de los ID
        x = int(str(x)[1:]) # Obtener el número en forma de int del último ID
        return x

        # -----------CALLBACK PARA BOTÓN agregar -----------
    def agregar(self):

        id = self.treeCreador.insert("","end",text=f"default{self.num}",values=[f"prueba{self.num}"])

        self.listBoton[id] = self.treeCreador.item(id)
        # print(self.listBoton)
        print(self.listBoton)
        self.num +=1
        
        # ----------- SALVAR DATOS AL SALIR -----------
    def saveData(self,data):
        with open(PATHJS,"w") as file:
            json.dump(data,file,indent=2) # El indent permite visual appealing


    def updateItem(self):
        pass
        
        #-----------CALLBACK PARA EL DOBLE CLICK-----------
    def checkEventsTree(self,event):
        interval = 0.2# Para el doble click

        if not self.boolTimer: # Primer click
            self.primerClick = time.time()
        if self.boolTimer:  # Segundo click
            self.segundoClick = time.time()
        deltaClick = abs(self.primerClick - self.segundoClick)

        # print("La resta es:", deltaClick)

        if deltaClick < interval: # Doble click
            # print("Doble click")
            column = self.treeCreador.identify_column(event.x)
            region = self.treeCreador.identify_region(event.x,event.y)

            if region == "tree": # Cambiar nombre
                def enter(e):
                    text = e.widget.get()
                    print(text)
                    self.treeCreador.item(item,text=text)
                    self.listBoton[item]["text"]=text
                    e.widget.delete(0,"end")
                    e.widget.place_forget()

                self.entryName.delete(0,"end")
                item = self.treeCreador.focus()
                values = self.treeCreador.item(item)
                if column == "#0":
                    text = values["text"]
                else:
                    text = values["values"]
                bbox = self.treeCreador.bbox(item,column)
                print(text)
                self.entryName.editing_item_iid = item
                self.entryName.place(x=bbox[0], y=(bbox[1] + 21), w=bbox[2], h=bbox[3])
                self.entryName.insert(0,text)
                self.entryName.select_range(0,View.tkinter.END)
                self.entryName.focus()

                self.entryName.bind("<FocusOut>",lambda e: e.widget.place_forget())
                self.entryName.bind("<Return>",enter)

            elif region == "cell": # Crear hotkey
                item = self.treeCreador.focus()
                values = self.treeCreador.item(item)
                bbox = self.treeCreador.bbox(item,column)
                self.textHotkey.place(x=bbox[0],y=(bbox[1]+21),w=bbox[2],h=bbox[3])
                self.textHotkey.focus()
                #Identificar teclas
                self.textHotkey.bind("<Key>",self.keyBuffer)
                self.textHotkey.bind("<FocusOut>", lambda e: e.widget.place_forget())
                self.textHotkey.bind("<FocusIn>",lambda e: print(e))
                self.textHotkey.bind("<Return>", lambda e: e.widget.place_forget())
                
            print(int(column[1:]))
        
        #-----------CAMBIAR EL VALOR DE BOOL UNA VEZ TERMINADA LA FUNCIÓN-----------
        
        self.boolTimer = not self.boolTimer
        print(self.boolTimer)
        print(event)

    #-----------CALLBACK QUE GUARDA LOS VALORES DEL HOTKEY DEL MOMENTO-----------
    def keyBuffer(self,e):
        # El hotkey se registrará con poco tiempo de intervalo dado que se haya presionado
        # El buffer durará 3 segundos, despues de los cuales se borrará el hotkey
        if not self.boolbuffer:
            self.buffTimeFirst = e.time
            
        if self.boolbuffer:
            self.buffTimeSecond = e.time
            
        deltaT = abs(self.buffTimeFirst-self.buffTimeSecond)
            
        print("Keysym:",e.keysym)
        print("State:",e.state)
        print("Char:",e.char)
        print("KeyCode:",e.keycode)
        print("Serial:",e.serial)
        print("Time:",e.time,"ms")
        print("Type:",e.type)
        print("DeltaTime:",deltaT,"ms")
        print(e)
        print("-----------")
        
        if deltaT > 3000: #Mayor a 3 segundos
            pass
        else: # Menor a 3 segundos
            pass
        
        self.boolbuffer = not self.boolbuffer # Se ira cambiando


    def loadData(self):
        try:
            with open(os.path.join(PATHJS),"r") as file:
                hotkeyData = json.load(file)
                for id, data in hotkeyData.items():
                    self.treeCreador.insert("","end",id,text=data["text"],values=data["values"])
                return hotkeyData

        except FileNotFoundError: # NO ENCUENTRA EL PATH
            if not os.path.exists(PATH):
                os.makedirs(PATH) # LO CREA
            with open(os.path.join(PATHJS),"w") as file: # CREA EL .JS
                json.dump({},file)
                return {}


    def itemSelected(self):
        pass

    def deleteItem(self):
        iid = self.treeCreador.focus()
        if iid == "":
            print("No se ha seleccionado celda a eliminar")

        else:
            nombre = self.treeCreador.item(iid,"text")
            self.treeCreador.delete(iid)
            self.listBoton.pop(iid)
            print(f"La celda {nombre} con iid {iid} se eliminó exitosamente")

    def stop(self):
        self.ventana.quit()





class Update:
    def __init__(self):
        pass


# def agregarObjeto():
#     return treeviewCreador.insert("", 0, text="Prueba1")
#
# def eliminarObjeto():
#     pass


if __name__ == '__main__':
    # INICIALIZAR EL PROGRAMA
    Program = Initialize()


    Program.start()
    Program.stop()
    Program.saveData(Program.listBoton)
    print("hola")
