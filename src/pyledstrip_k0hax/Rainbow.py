import time
from pyledstrip_k0hax.Wheel import Wheel
from pyledstrip_k0hax.StripState import StripState

def Rainbow(strip, wait_ms=20, iterations=1, stripState=None):
    """Draw rainbow that fades across all pixels at once."""
    if stripState == None:
        stripState = StripState(strip)

    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            pixelColor = Wheel((i + j) & 255)
            stripState.SetPixel(i, pixelColor)
            strip.setPixelColor(i, pixelColor)
        strip.show()
        time.sleep(wait_ms / 1000.0)
    return stripState

def RainbowCycle(strip, wait_ms=20, iterations=5, stripState=None):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    if stripState == None:
        stripState = StripState(strip)

    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            pixelColor = Wheel(
                (int(i * 256 / strip.numPixels()) + j) & 255)
            stripState.SetPixel(i, pixelColor)
            strip.setPixelColor(i, pixelColor)
        strip.show()
        time.sleep(wait_ms / 1000.0)
    return stripState

