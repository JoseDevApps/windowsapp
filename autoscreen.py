"""
autoscreen.py

Automatizacion de clics
Creacion de metodos para la automatizacion de procesos en la 
recoleccion de datos del Remote Sense SCADA Enercon
"""
import pyautogui
import time


class ScadaAuto:
    def __init__(self) -> None:
        pyautogui.FAILSAFE = True
        pass

    def screen(self, captura):
        """
        Metodo para localizar el mouse y el click segun
        la captura de imagen
        """
        self.captura = captura
        posicion = pyautogui.locateAllOnScreen(self.captura, confidence=0.8)
        icon = list(posicion[0])
        pyautogui.moveTo(icon)
        pyautogui.click(clicks=2)

    def move(self, capturaM):
        """
        Metodo para localizar el mouse en la captura
        """
        self.capturaM = capturaM
        posicion = pyautogui.locateAllOnScreen(self.capturaM, confidence=0.8)
        icon = list(posicion[0])
        pyautogui.moveTo(icon)
        pyautogui.click(clicks=1)

    def write_text(self, texto):
        """
        Metodo para escribir texto
        """
        self.texto = texto
        pyautogui.write(self.texto, interval=0.25)

    def push_enter(self):
        """
        Metodo para presionar enter
        """
        pyautogui.press("enter")

    def wait(self, segundos):
        """
        Metodo para esperar X segundos
        """
        self.segundos = segundos
        time.sleep(self.segundos)
