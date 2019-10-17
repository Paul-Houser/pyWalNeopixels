# pyWalNeopixels
## BEFORE USE
Before anything in this repo will work for you, you must install CircuitPython libraries on your raspberry pi according to [this guide](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi). After this, in your raspberry pi's terminal run:
```sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel```
This must be done with python 3, as python 2.X will not work. If python3 is your default python, you may need to run the same command with ```pip``` instead.

## Installation
This is the easiest way to wire your LED strip to the raspi, though keep in mind this will only work with very short (<20) strips of LED's, otherwise you need a separate powersupply. I Plugged my pi into a 5v 4amp wall adapter, and got this wiring to work with a strip of 43 LED's.
<img src="https://github.com/Paul-Houser/pyWalNeopixels/blob/master/led_strips_wiring.jpg" width=500>
