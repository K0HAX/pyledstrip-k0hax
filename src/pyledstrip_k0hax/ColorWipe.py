import time
from rpi_ws281x import PixelStrip, Color, ws
from pyledstrip_k0hax.StripState import StripState

def ColorWipe(strip, color, wait_ms=50, stripState=None):
    """Wipe color across display a pixel at a time."""
    if stripState == None:
        stripState = StripState(strip)
    else:
        for i in range(len(stripState.LedArray)):
            strip.setPixelColor(i, stripState.LedArray[i])
    for i in range(strip.numPixels()):
        stripState.SetPixel(i, color)
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)
    return stripState
