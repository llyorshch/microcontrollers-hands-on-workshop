import board
import digitalio
import time
import neopixel

# print(dir(board))

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    pixels.fill((16, 0, 8))
    time.sleep(1.5)
    led.value = False
    pixels.fill((0, 0, 0))
    time.sleep(1.5)
    

