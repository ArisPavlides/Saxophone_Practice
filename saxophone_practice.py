import random
import ctypes
import time

notes = ["ντο", "ρε", "μι", "φα", "σολ", "λα", "σι"]
random.shuffle(notes)

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

while True:

   print("Give me a:" + random.choice(notes))
   time.sleep(6)