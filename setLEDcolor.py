import board
import neopixel
from getColor import get_hex_code

PIXEL_PIN = board.D18
NUM_PIXELS = 43
ORDER = neopixel.GRB
FILEPATH = '/home/pi/Neopixel/colors.json'

pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=0.8, auto_write=False, pixel_order=ORDER)

hexcode = get_hex_code('color10', FILEPATH)

# hexcode is in the form #5E4E58, so converting to rgb starts at 1 instead of 0 to remove the hashtag.
rgb = tuple(int(hexcode[i:i+2], 16) for i in (1, 3, 5))


pixels.fill(rgb)
pixels.show()
