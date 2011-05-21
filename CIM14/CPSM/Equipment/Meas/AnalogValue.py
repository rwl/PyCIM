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

from CIM14.CPSM.Equipment.Meas.MeasurementValue import MeasurementValue

class AnalogValue(MeasurementValue):
    """AnalogValue represents an analog MeasurementValue.
    """

    def __init__(self, Analog=None, *args, **kw_args):
        """Initialises a new 'AnalogValue' instance.

        @param Analog: Measurement to which this value is connected.
        """
        self._Analog = None
        self.Analog = Analog

        super(AnalogValue, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Analog"]
    _many_refs = []

    def getAnalog(self):
        """Measurement to which this value is connected.
        """
        return self._Analog

    def setAnalog(self, value):
        if self._Analog is not None:
            filtered = [x for x in self.Analog.AnalogValues if x != self]
            self._Analog._AnalogValues = filtered

        self._Analog = value
        if self._Analog is not None:
            if self not in self._Analog._AnalogValues:
                self._Analog._AnalogValues.append(self)

    Analog = property(getAnalog, setAnalog)

