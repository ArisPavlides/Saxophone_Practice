import random
import time

notes = ["ντο", "ρε", "μι", "φα", "σολ", "λα", "σι"]
octave = ["medium", "high"]

random.shuffle(notes)

while True:

   print("Give me a:" + random.choice(octave) + " " + random.choice(notes))
   time.sleep(6)