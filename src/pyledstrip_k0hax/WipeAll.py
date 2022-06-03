from pyledstrip_k0hax.SetAll import SetAll

def WipeAll(strip):
    for a in range(0, 255, 15):
        for b in range(0, 255, 15):
            for c in range(0, 255, 15):
                SetAll(strip, Color(b, a, c, 0))

