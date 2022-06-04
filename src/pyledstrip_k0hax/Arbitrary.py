import time
import logging
from rpi_ws281x import Color
from pyledstrip_k0hax.StripState import StripState

def Arbitrary(strip, leds, stripState=None):
    """Set each LED to an arbitrary value"""
    logging.debug(strip)
    logging.debug(leds)
    if stripState == None:
        stripState = StripState(strip)

    if len(leds) == strip.numPixels():
        for i in range(len(leds)):
            logging.debug("Pixel [{}]".format(i))
            logging.debug("Pixel [{}] = [{}]".format(i, leds[i]))
            pixelColor = Color(*leds[i])
            logging.debug("[Arbitrary] pixelColor = {}".format(pixelColor))
            stripState.SetPixel(i, pixelColor)
            strip.setPixelColor(i, pixelColor)
    else:
        for i in range(strip.numPixels()):
            if i < len(leds):
                logging.debug("Pixel [{}]".format(i))
                logging.debug("Pixel [{}] = [{}]".format(i, leds[i]))
                pixelColor = Color(*leds[i])
                logging.debug("[Arbitrary] pixelColor = {}".format(pixelColor))
                stripState.SetPixel(i, pixelColor)
                strip.setPixelColor(i, pixelColor)
            else:
                logging.debug("Pixel [{}]".format(i))
                pixelColor = Color(0, 0, 0, 0)
                logging.debug("[Arbitrary] pixelColor = {}".format(pixelColor))
                stripState.SetPixel(i, pixelColor)
                strip.setPixelColor(i, pixelColor)
    strip.show()
    return stripState

