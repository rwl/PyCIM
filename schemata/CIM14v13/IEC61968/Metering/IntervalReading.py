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

from CIM14v13.IEC61970.Meas.MeasurementValue import MeasurementValue

class IntervalReading(MeasurementValue):
    """Data captured at regular intervals of time. Interval data could be captured as incremental data, absolute data, or relative data. The source for the data is usually a tariff quantity or an engineering quantity. Data is typically captured in time-tagged, uniform, fixed-length intervals of 5 min, 10 min, 15 min, 30 min, or 60 min. Note: Interval Data is sometimes also called 'Interval Data Readings' (IDR).
    """

    def __init__(self, value=0.0, IntervalBlocks=None, ReadingQualities=None, *args, **kw_args):
        """Initializes a new 'IntervalReading' instance.

        @param value: Value of this interval reading. 
        @param IntervalBlocks: All blocks containing this interval reading.
        @param ReadingQualities: Used only if quality of this interval reading value is different than 'Good'.
        """
        #: Value of this interval reading. 
        self.value = value

        self._IntervalBlocks = []
        self.IntervalBlocks = [] if IntervalBlocks is None else IntervalBlocks

        self._ReadingQualities = []
        self.ReadingQualities = [] if ReadingQualities is None else ReadingQualities

        super(IntervalReading, self).__init__(*args, **kw_args)

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

    def getReadingQualities(self):
        """Used only if quality of this interval reading value is different than 'Good'.
        """
        return self._ReadingQualities

    def setReadingQualities(self, value):
        for x in self._ReadingQualities:
            x._IntervalReading = None
        for y in value:
            y._IntervalReading = self
        self._ReadingQualities = value

    ReadingQualities = property(getReadingQualities, setReadingQualities)

    def addReadingQualities(self, *ReadingQualities):
        for obj in ReadingQualities:
            obj._IntervalReading = self
            self._ReadingQualities.append(obj)

    def removeReadingQualities(self, *ReadingQualities):
        for obj in ReadingQualities:
            obj._IntervalReading = None
            self._ReadingQualities.remove(obj)

