from rpi_ws281x import PixelStrip, Color, ws
from pyledstrip_k0hax.StripState import StripState

def SetAll(strip, color, stripState=None):
    if stripState == None:
        stripState = StripState(strip)

    for i in range(strip.numPixels()):
        stripState.SetPixel(i, color)
        strip.setPixelColor(i, color)
    strip.show()
    return stripState

