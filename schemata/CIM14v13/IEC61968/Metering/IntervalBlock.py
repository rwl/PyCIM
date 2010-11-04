# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.Element import Element

class IntervalBlock(Element):
    """Time sequence of Readings of the same ReadingType. Contained IntervalReadings may need conversion through the application of an offset and a scalar defined in associated Pending.
    """

    def __init__(self, IntervalReadings=None, MeterReading=None, ReadingType=None, Pending=None, **kw_args):
        """Initializes a new 'IntervalBlock' instance.

        @param IntervalReadings: Interval reading contained in this block.
        @param MeterReading: Meter reading containing this interval block.
        @param ReadingType: Type information for interval reading values contained in this block.
        @param Pending: Pending conversion to apply to interval reading values contained by this block (after which the resulting reading type is different than the original because it reflects the conversion result).
        """
        self._IntervalReadings = []
        self.IntervalReadings = [] if IntervalReadings is None else IntervalReadings

        self._MeterReading = None
        self.MeterReading = MeterReading

        self._ReadingType = None
        self.ReadingType = ReadingType

        self._Pending = None
        self.Pending = Pending

        super(IntervalBlock, self).__init__(**kw_args)

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
            self._MeterReading._IntervalBlocks.append(self)

    MeterReading = property(getMeterReading, setMeterReading)

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
            self._ReadingType._IntervalBlocks.append(self)

    ReadingType = property(getReadingType, setReadingType)

    def getPending(self):
        """Pending conversion to apply to interval reading values contained by this block (after which the resulting reading type is different than the original because it reflects the conversion result).
        """
        return self._Pending

    def setPending(self, value):
        if self._Pending is not None:
            filtered = [x for x in self.Pending.IntervalBlocks if x != self]
            self._Pending._IntervalBlocks = filtered

        self._Pending = value
        if self._Pending is not None:
            self._Pending._IntervalBlocks.append(self)

    Pending = property(getPending, setPending)

