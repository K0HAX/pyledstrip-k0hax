import time
import logging
from rpi_ws281x import Color

def SingleLed(strip, stripState, ledIndex, ledValue):
    if type(ledValue) != type([0, 0, 0, 0]):
        logging.critical("[SingleLed] type(ledValue) = {}".format(type(ledValue)))
        raise TypeError
    m_ledValue = Color(*ledValue)

    logging.debug("[SingleLed] Strip State: {}".format(stripState))
    logging.debug("[SingleLed] LED Index: {}".format(ledIndex))
    logging.debug("[SingleLed] LED Value: {}".format(m_ledValue))
    tmpState = stripState.LedArray
    tmpState[ledIndex] = m_ledValue
    stripState.LedArray = tmpState
    strip.setPixelColor(ledIndex, m_ledValue)
    strip.show()
    return stripState

