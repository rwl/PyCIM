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

from CIM15.IEC61970.Meas.MeasurementValue import MeasurementValue

class StringMeasurementValue(MeasurementValue):
    """StringMeasurementValue represents a measurement value of type string.StringMeasurementValue represents a measurement value of type string.
    """

    def __init__(self, value='', StringMeasurement=None, *args, **kw_args):
        """Initialises a new 'StringMeasurementValue' instance.

        @param value: The value to supervise. 
        @param StringMeasurement: Measurement to which this value is connected.
        """
        #: The value to supervise.
        self.value = value

        self._StringMeasurement = None
        self.StringMeasurement = StringMeasurement

        super(StringMeasurementValue, self).__init__(*args, **kw_args)

    _attrs = ["value"]
    _attr_types = {"value": str}
    _defaults = {"value": ''}
    _enums = {}
    _refs = ["StringMeasurement"]
    _many_refs = []

    def getStringMeasurement(self):
        """Measurement to which this value is connected.
        """
        return self._StringMeasurement

    def setStringMeasurement(self, value):
        if self._StringMeasurement is not None:
            filtered = [x for x in self.StringMeasurement.StringMeasurementValues if x != self]
            self._StringMeasurement._StringMeasurementValues = filtered

        self._StringMeasurement = value
        if self._StringMeasurement is not None:
            if self not in self._StringMeasurement._StringMeasurementValues:
                self._StringMeasurement._StringMeasurementValues.append(self)

    StringMeasurement = property(getStringMeasurement, setStringMeasurement)

