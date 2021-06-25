from gpiozero import Button
from time import sleep
from signal import pause
import os

button = Button(14)

while True:
   if(button.is_pressed):
      os.system("sudo sh -c 'echo 0 > /sys/class/leds/led1/brightness'")
      print("off")
   else:
      os.system("sudo sh -c 'echo 1 > /sys/class/leds/led1/brightness'")
      print("on")
   sleep(0.5)
