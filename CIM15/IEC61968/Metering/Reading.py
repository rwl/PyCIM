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

class Reading(MeasurementValue):
    """Specific value measured by a meter or other asset. Each Reading is associated with a specific ReadingType.Specific value measured by a meter or other asset. Each Reading is associated with a specific ReadingType.
    """

    def __init__(self, value=0.0, ReadingType=None, MeterReadings=None, ReadingQualities=None, *args, **kw_args):
        """Initialises a new 'Reading' instance.

        @param value: Value of this reading. 
        @param ReadingType: Type information for this reading value.
        @param MeterReadings: All meter readings (sets of values) containing this reading value.
        @param ReadingQualities: Used only if quality of this reading value is different than 'Good'.
        """
        #: Value of this reading.
        self.value = value

        self._ReadingType = None
        self.ReadingType = ReadingType

        self._MeterReadings = []
        self.MeterReadings = [] if MeterReadings is None else MeterReadings

        self._ReadingQualities = []
        self.ReadingQualities = [] if ReadingQualities is None else ReadingQualities

        super(Reading, self).__init__(*args, **kw_args)

    _attrs = ["value"]
    _attr_types = {"value": float}
    _defaults = {"value": 0.0}
    _enums = {}
    _refs = ["ReadingType", "MeterReadings", "ReadingQualities"]
    _many_refs = ["MeterReadings", "ReadingQualities"]

    def getReadingType(self):
        """Type information for this reading value.
        """
        return self._ReadingType

    def setReadingType(self, value):
        if self._ReadingType is not None:
            filtered = [x for x in self.ReadingType.Readings if x != self]
            self._ReadingType._Readings = filtered

        self._ReadingType = value
        if self._ReadingType is not None:
            if self not in self._ReadingType._Readings:
                self._ReadingType._Readings.append(self)

    ReadingType = property(getReadingType, setReadingType)

    def getMeterReadings(self):
        """All meter readings (sets of values) containing this reading value.
        """
        return self._MeterReadings

    def setMeterReadings(self, value):
        for p in self._MeterReadings:
            filtered = [q for q in p.Readings if q != self]
            self._MeterReadings._Readings = filtered
        for r in value:
            if self not in r._Readings:
                r._Readings.append(self)
        self._MeterReadings = value

    MeterReadings = property(getMeterReadings, setMeterReadings)

    def addMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            if self not in obj._Readings:
                obj._Readings.append(self)
            self._MeterReadings.append(obj)

    def removeMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            if self in obj._Readings:
                obj._Readings.remove(self)
            self._MeterReadings.remove(obj)

    def getReadingQualities(self):
        """Used only if quality of this reading value is different than 'Good'.
        """
        return self._ReadingQualities

    def setReadingQualities(self, value):
        for x in self._ReadingQualities:
            x.Reading = None
        for y in value:
            y._Reading = self
        self._ReadingQualities = value

    ReadingQualities = property(getReadingQualities, setReadingQualities)

    def addReadingQualities(self, *ReadingQualities):
        for obj in ReadingQualities:
            obj.Reading = self

    def removeReadingQualities(self, *ReadingQualities):
        for obj in ReadingQualities:
            obj.Reading = None

