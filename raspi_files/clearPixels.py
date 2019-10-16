import board
import neopixel

PIXEL_PIN = board.D18
NUM_PIXELS = 43
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=0.7, auto_write=False, pixel_order=ORDER)

def clearPixels():
    pixels.fill((0, 0, 0))
    pixels.show()

if __name__ == '__main__':
    clearPixels()
