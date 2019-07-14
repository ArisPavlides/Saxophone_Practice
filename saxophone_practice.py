import random
import time

notes = ["ντο", "ντο# AKA ρεβ", "ρε", "ρε#", "μι", "φα", "φα#", "σολ", "σολ#", "λα", "λα#", "σι"]
octave = ["medium", "high"]

random.shuffle(notes)

while True:

   print("Give me a: " + random.choice(octave) + " " + random.choice(notes))
   time.sleep(6)