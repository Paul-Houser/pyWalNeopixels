# pyWalNeopixels
## BEFORE USE
Before anything in this repo will work for you, you must install CircuitPython libraries on your raspberry pi according to [this guide](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)(I used a raspberry pi 3b+). After this, in your raspberry pi's terminal run:
```sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel```
This must be done with python 3, as python 2.X will not work. If python3 is your default python, you may need to run the same command with ```pip``` instead.

## Installation
This is the easiest way to wire your LED strip to your raspberry pi. Keep in mind that using a standard iphone wall charger (5v 1a) this will only work with very short (<20) strips of LED's, otherwise you need a separate powersupply. When I Plugged my raspberry pi 3b+ into a 5v 4amp wall adapter, it was enough to power a strip of 43 LED's, though from my research this might be pushing the limits a little bit.

<img src="https://github.com/Paul-Houser/pyWalNeopixels/blob/master/led_strips_wiring.jpg" alt="Diagram taken from https://cdn-learn.adafruit.com/assets/assets/000/063/929/large1024/led_strips_raspi_NeoPixel_bb.jpg?1539981142" width=500>

After you've installed CircuitPython, rpi_ws281x, and adafruit-circuitpython-neopixel as directed in the before use section,
clone this git repository onto your PC. Make sure your raspberry pi and PC are on the same network. Change directory into ```pyWalNeopixels/PC_files``` and open ```startLEDS``` in your favorite editor. Make the following adjustments:
  * Line 6, ```COLORS_DIR```: This is set to the default colors.json file generated by pywal. If your path is different, place it here. Your file should be named ```colors.json```.
  * Line 9, ```REPO_DIR```: Set this to the path of your cloned pyWalNeopixels repo. The default is ```"$HOME/Documents/GitHub/pyWalNeopixels"```.
  * Line 11, ```USER```: This is the user of your pi. In my case, since I just use the pi's default user 'pi', I set USER to "pi"
  * Line 12, ```IP```: This is the IP address of your pi. In my case, it's ```192.168.0.25```.

Now, open ```stopLEDS``` and make the following adjustments:
  * Line 5, ```REPO_DIR```: Same as in ```startLEDS```.
  * Line 7, ```USER```: Same as in ```startLEDS```.
  * Line 8, ```IP```: same as in ```startLEDS```.

I know these changes are redundant, I'm just not well versed in scripts like these. If there's some way to make a header file so that all these changes can be made only once in one file, please let me know!

After these changes, run ```chmod 700 startLEDS``` and ```chmod 700 stopLEDS```. You can copy these to anywhere you like on your PC and they should run just fine. I added them to my path so I can have them execute when i3 starts.

To run these scripts, run ```./path/to/repo/PC_files/startLEDS```. Same thing but replace with ```stopLEDS``` to turn them off.
