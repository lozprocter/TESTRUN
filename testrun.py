from turtle import delay
from gpiozero import LED
import time

led = LED(17)

def blink():
  led.on()
  time.sleep(500)
  led.off()
  time.sleep(500)
  
while True:
  blink()
