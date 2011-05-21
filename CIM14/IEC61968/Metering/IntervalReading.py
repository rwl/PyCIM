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

from CIM14.IEC61970.Meas.MeasurementValue import MeasurementValue

class IntervalReading(MeasurementValue):
    """Data captured at regular intervals of time. Interval data could be captured as incremental data, absolute data, or relative data. The source for the data is usually a tariff quantity or an engineering quantity. Data is typically captured in time-tagged, uniform, fixed-length intervals of 5 min, 10 min, 15 min, 30 min, or 60 min. Note: Interval Data is sometimes also called 'Interval Data Readings' (IDR).
    """

    def __init__(self, value=0.0, ReadingQualities=None, IntervalBlocks=None, *args, **kw_args):
        """Initialises a new 'IntervalReading' instance.

        @param value: Value of this interval reading. 
        @param ReadingQualities: Used only if quality of this interval reading value is different than 'Good'.
        @param IntervalBlocks: All blocks containing this interval reading.
        """
        #: Value of this interval reading.
        self.value = value

        self._ReadingQualities = []
        self.ReadingQualities = [] if ReadingQualities is None else ReadingQualities

        self._IntervalBlocks = []
        self.IntervalBlocks = [] if IntervalBlocks is None else IntervalBlocks

        super(IntervalReading, self).__init__(*args, **kw_args)

    _attrs = ["value"]
    _attr_types = {"value": float}
    _defaults = {"value": 0.0}
    _enums = {}
    _refs = ["ReadingQualities", "IntervalBlocks"]
    _many_refs = ["ReadingQualities", "IntervalBlocks"]

    def getReadingQualities(self):
        """Used only if quality of this interval reading value is different than 'Good'.
        """
        return self._ReadingQualities

    def setReadingQualities(self, value):
        for x in self._ReadingQualities:
            x.IntervalReading = None
        for y in value:
            y._IntervalReading = self
        self._ReadingQualities = value

    ReadingQualities = property(getReadingQualities, setReadingQualities)

    def addReadingQualities(self, *ReadingQualities):
        for obj in ReadingQualities:
            obj.IntervalReading = self

    def removeReadingQualities(self, *ReadingQualities):
        for obj in ReadingQualities:
            obj.IntervalReading = None

    def getIntervalBlocks(self):
        """All blocks containing this interval reading.
        """
        return self._IntervalBlocks

    def setIntervalBlocks(self, value):
        for p in self._IntervalBlocks:
            filtered = [q for q in p.IntervalReadings if q != self]
            self._IntervalBlocks._IntervalReadings = filtered
        for r in value:
            if self not in r._IntervalReadings:
                r._IntervalReadings.append(self)
        self._IntervalBlocks = value

    IntervalBlocks = property(getIntervalBlocks, setIntervalBlocks)

    def addIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            if self not in obj._IntervalReadings:
                obj._IntervalReadings.append(self)
            self._IntervalBlocks.append(obj)

    def removeIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            if self in obj._IntervalReadings:
                obj._IntervalReadings.remove(self)
            self._IntervalBlocks.remove(obj)

