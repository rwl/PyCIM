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

from CIM15.IEC61970.Meas.Measurement import Measurement

class StringMeasurement(Measurement):
    """StringMeasurement represents a measurement with values of type string.StringMeasurement represents a measurement with values of type string.
    """

    def __init__(self, StringMeasurementValues=None, *args, **kw_args):
        """Initialises a new 'StringMeasurement' instance.

        @param StringMeasurementValues: The values connected to this measurement.
        """
        self._StringMeasurementValues = []
        self.StringMeasurementValues = [] if StringMeasurementValues is None else StringMeasurementValues

        super(StringMeasurement, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["StringMeasurementValues"]
    _many_refs = ["StringMeasurementValues"]

    def getStringMeasurementValues(self):
        """The values connected to this measurement.
        """
        return self._StringMeasurementValues

    def setStringMeasurementValues(self, value):
        for x in self._StringMeasurementValues:
            x.StringMeasurement = None
        for y in value:
            y._StringMeasurement = self
        self._StringMeasurementValues = value

    StringMeasurementValues = property(getStringMeasurementValues, setStringMeasurementValues)

    def addStringMeasurementValues(self, *StringMeasurementValues):
        for obj in StringMeasurementValues:
            obj.StringMeasurement = self

    def removeStringMeasurementValues(self, *StringMeasurementValues):
        for obj in StringMeasurementValues:
            obj.StringMeasurement = None

