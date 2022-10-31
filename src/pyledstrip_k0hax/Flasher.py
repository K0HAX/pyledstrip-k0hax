import time
import logging
from pyledstrip_k0hax.Wheel import Wheel, Color
from pyledstrip_k0hax.StripState import StripState

def Flasher(strip, color1, color2, wait_ms=125, iterations=10, stripState=None):
    """Flash LED animation."""
    if stripState == None:
        stripState = StripState(strip)

    runNumber = 0
    for j in range(iterations):
        if runNumber == 0:
            runNumber = 1
            firstColor = color1
            secondColor = color2
        else:
            runNumber = 0
            firstColor = color2
            secondColor = color1
        modColor = False
        for i in range(0, strip.numPixels()):
            if i % 15 == 0:
                modColor = not modColor
            if modColor:
                stripState.SetPixel(i, secondColor)
                strip.setPixelColor(i, secondColor)
            else:
                stripState.SetPixel(i, firstColor)
                strip.setPixelColor(i, firstColor)
        strip.show()
        time.sleep(wait_ms / 1000.0)
    return stripState

