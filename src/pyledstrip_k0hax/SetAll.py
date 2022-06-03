from rpi_ws281x import PixelStrip, Color, ws

def SetAll(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    return strip

