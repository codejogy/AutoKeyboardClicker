# Pure application data
# No logic
# La data será

#Composition
import pynput

class CombinacionTeclas():
    """
    Clase con la lógica del programa para crear objetos
    que permita hacer que con una combinación de teclas
    se haga algo determinado
    """
    def __init__(self):
        """
        Se creará un entorno para una nueva combinación
        """
        self.oMouse = pynput.mouse.Controller()
        self.oKeyboard = pynput.keyboard.Controller()
        self.LEFTCLICK = pynput.mouse.Button.left
        self.RIGHTCLICK = pynput.mouse.Button.right
        self.hotkey = ""


    def getKeyValue(self):
        pass

    def combinacion(self,key:str) -> object:
        # Verificar que sea string
        assert key == str,"Este valor necesita ser un string"
        # Verificar que el string sea compatible
        try:
            key == pynput.keyboard.KeyCode()
        except:
            pass
        if key == "<ctrl>":
            self.hotkey += key
        if key == "<alt>":
            self.hotkey += key
        if key == pynput.keyboard.Key():
            pass



    def listener(self,callback) :
        self.listen = pynput.keyboard.Listener(on_release=callback)
        self.listen.start()

    def stop(self):
        self.listen.stop()

    def __repr__(self):
        pass

if __name__ == '__main__':
    print(pynput.keyboard.KeyCode(char="5").from_char(["7","5"]))


