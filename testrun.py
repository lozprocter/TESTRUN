from turtle import delay
from gpiozero import LED
import time

led = LED(17)

def blink():
  led.on()
  time.sleep(1)
  led.off()
  time.sleep(1)
  
while True:
  blink()
