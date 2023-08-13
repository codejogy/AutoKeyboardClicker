# Pure application data
# No logic
# La data será

# Composition

import pynput
import json


class TecladoControlar(pynput.keyboard.Controller):
    """Clase que hereda de keyboard y controla el teclado"""

    def pressKey(self):
        pass


class TecladoEscuchar(pynput.keyboard.Listener):
    """Clase que hereda del keyboard y detecta el teclado"""

    def __init__(self) -> None:
        super().__init__(self.on_Press)
        self.listStrings = []

    def readString(self, s):
        self.listStrings.append(s)

    def on_Press(self, k):
        return k


pass

if __name__ == "__main__":
    print("hola")
    stringTest = "Shif_L+W"
    stringToggle = "+"
    t = TecladoEscuchar()
    t.readString(stringTest)
    print(t)
    t.run()
