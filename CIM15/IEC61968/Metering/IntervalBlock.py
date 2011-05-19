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

from CIM15.Element import Element

class IntervalBlock(Element):
    """Time sequence of Readings of the same ReadingType. Contained IntervalReadings may need conversion through the application of an offset and a scalar defined in associated Pending.Time sequence of Readings of the same ReadingType. Contained IntervalReadings may need conversion through the application of an offset and a scalar defined in associated Pending.
    """

    def __init__(self, ReadingType=None, IntervalReadings=None, MeterReading=None, PendingCalculation=None, *args, **kw_args):
        """Initialises a new 'IntervalBlock' instance.

        @param ReadingType: Type information for interval reading values contained in this block.
        @param IntervalReadings: Interval reading contained in this block.
        @param MeterReading: Meter reading containing this interval block.
        @param PendingCalculation: Pending conversion to apply to interval reading values contained by this block (after which the resulting reading type is different than the original because it reflects the conversion result).
        """
        self._ReadingType = None
        self.ReadingType = ReadingType

        self._IntervalReadings = []
        self.IntervalReadings = [] if IntervalReadings is None else IntervalReadings

        self._MeterReading = None
        self.MeterReading = MeterReading

        self._PendingCalculation = None
        self.PendingCalculation = PendingCalculation

        super(IntervalBlock, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ReadingType", "IntervalReadings", "MeterReading", "PendingCalculation"]
    _many_refs = ["IntervalReadings"]

    def getReadingType(self):
        """Type information for interval reading values contained in this block.
        """
        return self._ReadingType

    def setReadingType(self, value):
        if self._ReadingType is not None:
            filtered = [x for x in self.ReadingType.IntervalBlocks if x != self]
            self._ReadingType._IntervalBlocks = filtered

        self._ReadingType = value
        if self._ReadingType is not None:
            if self not in self._ReadingType._IntervalBlocks:
                self._ReadingType._IntervalBlocks.append(self)

    ReadingType = property(getReadingType, setReadingType)

    def getIntervalReadings(self):
        """Interval reading contained in this block.
        """
        return self._IntervalReadings

    def setIntervalReadings(self, value):
        for p in self._IntervalReadings:
            filtered = [q for q in p.IntervalBlocks if q != self]
            self._IntervalReadings._IntervalBlocks = filtered
        for r in value:
            if self not in r._IntervalBlocks:
                r._IntervalBlocks.append(self)
        self._IntervalReadings = value

    IntervalReadings = property(getIntervalReadings, setIntervalReadings)

    def addIntervalReadings(self, *IntervalReadings):
        for obj in IntervalReadings:
            if self not in obj._IntervalBlocks:
                obj._IntervalBlocks.append(self)
            self._IntervalReadings.append(obj)

    def removeIntervalReadings(self, *IntervalReadings):
        for obj in IntervalReadings:
            if self in obj._IntervalBlocks:
                obj._IntervalBlocks.remove(self)
            self._IntervalReadings.remove(obj)

    def getMeterReading(self):
        """Meter reading containing this interval block.
        """
        return self._MeterReading

    def setMeterReading(self, value):
        if self._MeterReading is not None:
            filtered = [x for x in self.MeterReading.IntervalBlocks if x != self]
            self._MeterReading._IntervalBlocks = filtered

        self._MeterReading = value
        if self._MeterReading is not None:
            if self not in self._MeterReading._IntervalBlocks:
                self._MeterReading._IntervalBlocks.append(self)

    MeterReading = property(getMeterReading, setMeterReading)

    def getPendingCalculation(self):
        """Pending conversion to apply to interval reading values contained by this block (after which the resulting reading type is different than the original because it reflects the conversion result).
        """
        return self._PendingCalculation

    def setPendingCalculation(self, value):
        if self._PendingCalculation is not None:
            filtered = [x for x in self.PendingCalculation.IntervalBlocks if x != self]
            self._PendingCalculation._IntervalBlocks = filtered

        self._PendingCalculation = value
        if self._PendingCalculation is not None:
            if self not in self._PendingCalculation._IntervalBlocks:
                self._PendingCalculation._IntervalBlocks.append(self)

    PendingCalculation = property(getPendingCalculation, setPendingCalculation)

