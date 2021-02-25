import pyautogui as pg
import time
import sys
import os
from time import strftime
import pyperclip

recent_value = ""

D = time.strftime("%D")
r = time.strftime("%r")

while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        print("Value changed: %s" % str(recent_value))
        time.sleep(5)
        pg.write(str(recent_value))
