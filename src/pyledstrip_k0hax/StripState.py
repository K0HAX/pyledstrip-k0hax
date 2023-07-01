import logging
import inspect
import json
import copy
from threading import Lock
from rpi_ws281x import Color

class AttributeSetError(Exception):
    def __init__(self, message="Can not set attributes of this class."):
        self.message = message
        super().__init__(self.message)

class ArrayLengthError(Exception):
    def __init__(self, Expected, Passed):
        self.Expected = Expected
        self.Passed = Passed
        self.message = "Passed length was {}, expected length is {}.".format(len(self.Passed), len(self.Expected))
        super().__init__(self.message)

class StripState():
    def __init__(self, strip):
        self._lock = Lock()
        self._LedArray = [Color(0, 0, 0, 0)] * strip.numPixels()

    # Thread safety
    def lock(self):
        self._lock.acquire()

    def release(self):
        self._lock.release()

    def SetPixel(self, pixel, value):
        if type(self._LedArray[pixel]) != int:
            if len(value) != len(self._LedArray[pixel]):
                raise ArrayLengthError(self._LedArray[pixel], value)
            self._LedArray[pixel] = list(value)
        elif type(self._LedArray[pixel]) == int:
            self._LedArray[pixel] = int(value)
        else:
            raise TypeError

    @property
    def LedArray(self):
        retval = copy.deepcopy(self._LedArray)
        return retval

    @LedArray.setter
    def LedArray(self, value):
        if len(value) != len(self._LedArray):
            raise ArrayLengthError(self._LedArray, value)
        for i in range(len(value)):
            self.SetPixel(i, value[i])
        #    if len(value[i]) != len(self._LedArray[i]):
        #        raise ArrayLengthError(self._LedArray[pixel], value)

    def getStack(self):
        return inspect.stack()

    def __setattr__(self, name, value):
        if name == 'LedArray':
            super().__setattr__(name, value)
            return

        stack = inspect.stack()
        if "self" not in stack[1][0].f_locals.keys():
            logging.critical("This class does not allow setting attributes externally.")
            raise AttributeSetError

        caller = stack[1][0].f_locals["self"].__class__.__name__

        if caller != "StripState" and name != 'LedArray':
            logging.critical("Nice try!")
            print(json.dumps(stack[1][0].f_locals["self"].__class__.__name__, indent=2, default=str))
            print("----")
            print(json.dumps(stack, indent=2, default=str))
            raise AttributeSetError
        else:
            super().__setattr__(name, value)

