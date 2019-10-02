import board
import neopixel
import time
from getColor import get_hex_code

PIXEL_PIN = board.D18
NUM_PIXELS = 43
ORDER = neopixel.GRB
FILEPATH = '/home/pi/Documents/GitHub/pyWalNeopixels/colors.json'

pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=0.7, auto_write=False, pixel_order=ORDER)


def getColor(colorName):
    hexcode = get_hex_code(colorName, FILEPATH)
    
    # hexcode is in the form #5E4E58, so converting to rgb starts at 1 instead of 0 to remove the hashtag.
    rgb = tuple(int(hexcode[i:i+2], 16) for i in (1, 3, 5))
    return rgb


def adjustColor(cur, new):
    if cur < new:
        return cur + 1
    elif cur > new:
        return cur - 1
    else:
        return cur


def fadeToColor(cur_RGB, new_RGB):
    cur_r = cur_RGB[0]
    cur_g = cur_RGB[1]
    cur_b = cur_RGB[2]

    new_r = new_RGB[0]
    new_g = new_RGB[1]
    new_b = new_RGB[2]

    while cur_r != new_r or cur_g != new_g or cur_b != new_b:
        cur_r = adjustColor(cur_r, new_r)
        cur_g = adjustColor(cur_g, new_g)
        cur_b = adjustColor(cur_b, new_b)

        pixels.fill((cur_r, cur_g, cur_b))
        pixels.show()
        time.sleep(0.01)


def colorsList():
    colors = []
    for i in range(16):
        new_color_name = 'color' + str(i)
        new_RGB = getColor(new_color_name)

        # this if statement is here because some colors that pywal generates are so dark/dim that they just look like crap on the LED's. 
        # comment out this if statement if you want your LEDs to faithfully try to recreate any color, including black.
        if (new_RGB[0] + new_RGB[1] + new_RGB[2]) >= 255:
            colors.append(new_RGB)
            
    return colors


def cycleColors(colors, curr_RGB = (0, 0, 0)):
    for color in colors:
        fadeToColor(curr_RGB, color)
        curr_RGB = color
        time.sleep(15)


if __name__ == "__main__":
    colors = colorsList()
    
    if len(colors) <= 0:
        print("No colors were bright enough for the LED's to properly display")
        exit(1)

    cycleColors(colors)
    while True:
        cycleColors(colors, colors[-1])

