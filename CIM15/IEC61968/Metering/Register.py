# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Register(IdentifiedObject):
    """Display for quantity that is metered on an end device such as a meter.Display for quantity that is metered on an end device such as a meter.
    """

    def __init__(self, leftDigitCount=0, rightDigitCount=0, ReadingType=None, EndDeviceFunction=None, *args, **kw_args):
        """Initialises a new 'Register' instance.

        @param leftDigitCount: Number of digits (dials on a mechanical meter) to the left of the decimal place; default is 5. 
        @param rightDigitCount: Number of digits (dials on a mechanical meter) to the right of the decimal place. 
        @param ReadingType: Reading type for values displayed by this register.
        @param EndDeviceFunction: End device function metering quantities displayed by this register.
        """
        #: Number of digits (dials on a mechanical meter) to the left of the decimal place; default is 5.
        self.leftDigitCount = leftDigitCount

        #: Number of digits (dials on a mechanical meter) to the right of the decimal place.
        self.rightDigitCount = rightDigitCount

        self._ReadingType = None
        self.ReadingType = ReadingType

        self._EndDeviceFunction = None
        self.EndDeviceFunction = EndDeviceFunction

        super(Register, self).__init__(*args, **kw_args)

    _attrs = ["leftDigitCount", "rightDigitCount"]
    _attr_types = {"leftDigitCount": int, "rightDigitCount": int}
    _defaults = {"leftDigitCount": 0, "rightDigitCount": 0}
    _enums = {}
    _refs = ["ReadingType", "EndDeviceFunction"]
    _many_refs = []

    def getReadingType(self):
        """Reading type for values displayed by this register.
        """
        return self._ReadingType

    def setReadingType(self, value):
        if self._ReadingType is not None:
            self._ReadingType._Register = None

        self._ReadingType = value
        if self._ReadingType is not None:
            self._ReadingType.Register = None
            self._ReadingType._Register = self

    ReadingType = property(getReadingType, setReadingType)

    def getEndDeviceFunction(self):
        """End device function metering quantities displayed by this register.
        """
        return self._EndDeviceFunction

    def setEndDeviceFunction(self, value):
        if self._EndDeviceFunction is not None:
            filtered = [x for x in self.EndDeviceFunction.Registers if x != self]
            self._EndDeviceFunction._Registers = filtered

        self._EndDeviceFunction = value
        if self._EndDeviceFunction is not None:
            if self not in self._EndDeviceFunction._Registers:
                self._EndDeviceFunction._Registers.append(self)

    EndDeviceFunction = property(getEndDeviceFunction, setEndDeviceFunction)

