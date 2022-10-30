import time
import logging
from pyledstrip_k0hax.Wheel import Wheel, Color
from pyledstrip_k0hax.StripState import StripState

def TheaterChase(strip, color, wait_ms=50, iterations=10, stripState=None):
    """Movie theater light style chaser animation."""
    logging.debug("TheaterChase type: {}".format(type(strip)))
    logging.debug("Color: {}".format(color))
    if stripState == None:
        stripState = StripState(strip)

    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                stripState.SetPixel(i + q, color)
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                pixelColor = Color(0, 0, 0, 0)
                stripState.SetPixel(i + q, pixelColor)
                strip.setPixelColor(i + q, pixelColor)
    return stripState

def TheaterChaseDual(strip, color1, color2, wait_ms=50, iterations=10, stripState=None):
    """Movie theater light style chaser animation."""
    logging.debug("TheaterChase type: {}".format(type(strip)))
    logging.debug("Color1: {}".format(color1))
    logging.debug("Color2: {}".format(color2))
    if stripState == None:
        stripState = StripState(strip)

    for j in range(iterations):
        for q in range(3):
            for i in reversed(range(0, strip.numPixels(), 3)):
                stripState.SetPixel(i + q, color1)
                strip.setPixelColor(i + q, color1)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in reversed(range(0, strip.numPixels(), 3)):
                #pixelColor = Color(0, 0, 0, 0)
                pixelColor = color2
                stripState.SetPixel(i + q, pixelColor)
                strip.setPixelColor(i + q, pixelColor)
    return stripState

def TheaterChaseRainbow(strip, wait_ms=50, stripState=None):
    """Rainbow movie theater light style chaser animation."""
    if stripState == None:
        stripState = StripState(strip)

    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                pixelColor = Wheel((i + j) % 255)
                stripState.SetPixel(i + q, pixelColor)
                strip.setPixelColor(i + q, pixelColor)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                pixelColor = Color(0, 0, 0, 0)
                stripState.SetPixel(i + q, pixelColor)
                strip.setPixelColor(i + q, pixelColor)
    return stripState

