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

class ReadingQuality(Element):
    """Quality of a specific reading value or interval reading value. Note that more than one Quality may be applicable to a given Reading. Typically not used unless problems or unusual conditions occur (i.e., quality for each Reading is assumed to be 'Good' unless stated otherwise in associated ReadingQuality).
    """

    def __init__(self, quality='', Reading=None, IntervalReading=None, *args, **kw_args):
        """Initializes a new 'ReadingQuality' instance.

        @param quality: Quality, to be specified if different than 'Good'. 
        @param Reading: Reading value to which this quality applies.
        @param IntervalReading: Interval reading value to which this quality applies.
        """
        #: Quality, to be specified if different than 'Good'. 
        self.quality = quality

        self._Reading = None
        self.Reading = Reading

        self._IntervalReading = None
        self.IntervalReading = IntervalReading

        super(ReadingQuality, self).__init__(*args, **kw_args)

    def getReading(self):
        """Reading value to which this quality applies.
        """
        return self._Reading

    def setReading(self, value):
        if self._Reading is not None:
            filtered = [x for x in self.Reading.ReadingQualities if x != self]
            self._Reading._ReadingQualities = filtered

        self._Reading = value
        if self._Reading is not None:
            self._Reading._ReadingQualities.append(self)

    Reading = property(getReading, setReading)

    def getIntervalReading(self):
        """Interval reading value to which this quality applies.
        """
        return self._IntervalReading

    def setIntervalReading(self, value):
        if self._IntervalReading is not None:
            filtered = [x for x in self.IntervalReading.ReadingQualities if x != self]
            self._IntervalReading._ReadingQualities = filtered

        self._IntervalReading = value
        if self._IntervalReading is not None:
            self._IntervalReading._ReadingQualities.append(self)

    IntervalReading = property(getIntervalReading, setIntervalReading)

