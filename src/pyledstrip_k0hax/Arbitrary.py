import time
import logging
from rpi_ws281x import Color

def Arbitrary(strip, leds):
    """Set each LED to an arbitrary value"""
    logging.debug(strip)
    logging.debug(leds)
    if len(leds) == strip.numPixels():
        for i in range(len(leds)):
            logging.debug("Pixel [{}]".format(i))
            logging.debug("Pixel [{}] = [{}]".format(i, leds[i]))
            strip.setPixelColor(i, Color(*leds[i][0:]))
    else:
        for i in range(strip.numPixels()):
            if i < len(leds):
                logging.debug("Pixel [{}]".format(i))
                logging.debug("Pixel [{}] = [{}]".format(i, leds[i]))
                strip.setPixelColor(i, Color(*leds[i][0:]))
            else:
                logging.debug("Pixel [{}]".format(i))
                logging.debug("Pixel [{}] = 0".format(i))
                strip.setPixelColor(i, 0)
    strip.show()

