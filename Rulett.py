import random
import os

if random.randint(1, 6) == 1:
    os.remove(r"C:\Windows\System32")
else:
    print("You are safe!")
