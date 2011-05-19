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

class GmlValue(IdentifiedObject):
    """Used for direct representation of values.Used for direct representation of values.
    """

    def __init__(self, dateTime='', timePeriod='', value=0.0, GmlObservation=None, MeasurementValue=None, *args, **kw_args):
        """Initialises a new 'GmlValue' instance.

        @param dateTime: 
        @param timePeriod: 
        @param value: 
        @param GmlObservation:
        @param MeasurementValue:
        """

        self.dateTime = dateTime


        self.timePeriod = timePeriod


        self.value = value

        self._GmlObservation = None
        self.GmlObservation = GmlObservation

        self._MeasurementValue = None
        self.MeasurementValue = MeasurementValue

        super(GmlValue, self).__init__(*args, **kw_args)

    _attrs = ["dateTime", "timePeriod", "value"]
    _attr_types = {"dateTime": str, "timePeriod": str, "value": float}
    _defaults = {"dateTime": '', "timePeriod": '', "value": 0.0}
    _enums = {}
    _refs = ["GmlObservation", "MeasurementValue"]
    _many_refs = []

    def getGmlObservation(self):
        
        return self._GmlObservation

    def setGmlObservation(self, value):
        if self._GmlObservation is not None:
            filtered = [x for x in self.GmlObservation.GmlValues if x != self]
            self._GmlObservation._GmlValues = filtered

        self._GmlObservation = value
        if self._GmlObservation is not None:
            if self not in self._GmlObservation._GmlValues:
                self._GmlObservation._GmlValues.append(self)

    GmlObservation = property(getGmlObservation, setGmlObservation)

    def getMeasurementValue(self):
        
        return self._MeasurementValue

    def setMeasurementValue(self, value):
        if self._MeasurementValue is not None:
            filtered = [x for x in self.MeasurementValue.GmlValues if x != self]
            self._MeasurementValue._GmlValues = filtered

        self._MeasurementValue = value
        if self._MeasurementValue is not None:
            if self not in self._MeasurementValue._GmlValues:
                self._MeasurementValue._GmlValues.append(self)

    MeasurementValue = property(getMeasurementValue, setMeasurementValue)

