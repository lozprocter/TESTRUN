from turtle import delay
from gpiozero import LED
import time

led = LED(17)

def blink():
  led.on()
  delay(500)
  led.off()
  delay(500)
  
while True:
  blink()
