import microcontroller          #The pin definitions are in this library
import neopixel                 #Though it is a regular RGB LED, for circuitpython it is accesed as a WS2812 neopixel.
import time

p0 = microcontroller.pin.TOUCH1 #based on circuitpython-v0.1.2-fomu, where it doesnt matter which of the touch pins you pick.
rgb = neopixel.NeoPixel(p0,1,brightness=1)

while True:
    rgb[0]=(255,0,0)
    time.sleep(1)
    rgb[0]=(0,255,0)
    time.sleep(1)
    rgb[0]=(0,0,255)
    time.sleep(1)
