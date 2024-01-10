"""
autoscreen.py

Automatizacion de clics
Creacion de metodos para la automatizacion de procesos en la 
recoleccion de datos del Remote Sense SCADA Enercon
"""
import pyautogui
import time


def screen(captura):
    """
    Metodo para localizar el mouse y el click segun
    la captura de imagen
    """
    posicion = pyautogui.locateOnScreen(captura)
    icon = list(posicion)
    pyautogui.moveTo(icon)
    pyautogui.click(clicks=2)

def move(capturaM):
    """
    Metodo para localizar el mouse en la captura
    """
    posicion = pyautogui.locateOnScreen(capturaM)
    # posicion = pyautogui.center(posicion)
    pyautogui.moveTo(list(posicion))
    pyautogui.click(clicks=2)

def write_text( texto):
    """
    Metodo para escribir texto
    """
    pyautogui.write(texto, interval=0.25)

def push_enter():
    """
    Metodo para presionar enter
    """
    pyautogui.press("enter")

def wait( segundos):
    """
    Metodo para esperar X segundos
    """
    time.sleep(segundos)
