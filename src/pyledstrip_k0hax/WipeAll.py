from pyledstrip_k0hax.SetAll import SetAll
from pyledstrip_k0hax.StripState import StripState

def WipeAll(strip, stripState=None):
    if stripState == None:
        stripState = StripState(strip)

    for a in range(0, 255, 15):
        for b in range(0, 255, 15):
            for c in range(0, 255, 15):
                stripState = SetAll(strip, Color(b, a, c, 0), stripState)
    return stripState

