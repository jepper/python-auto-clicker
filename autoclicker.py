from random import random
from pynput.mouse import Controller, Button
from pynput.keyboard import KeyCode,Listener
from threading import Thread
from time import sleep
delay = .0001
mouse = Controller()

class AutoClicker(Thread):
    clicking = False
    def run(self):
        while True:
            if AutoClicker.clicking:
                mouse.click(Button.left)
            sleep(delay * random() * 0.5 * delay)

def keypress(key):
    if key == KeyCode(char="["):
        AutoClicker.clicking = not AutoClicker.clicking

AutoClicker().start()

with Listener(on_press=keypress) as listener:
    listener.join()

