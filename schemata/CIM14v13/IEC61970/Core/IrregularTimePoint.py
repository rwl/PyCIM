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

class IrregularTimePoint(Element):
    """TimePoints for a schedule where the time between the points varies.
    """

    def __init__(self, time=0.0, value1=0.0, value2=0.0, IntervalSchedule=None, *args, **kw_args):
        """Initializes a new 'IrregularTimePoint' instance.

        @param time: The time is relative the BasicTimeSchedule.startTime. 
        @param value1: The first value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule. 
        @param value2: The second value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule. 
        @param IntervalSchedule: An IrregularTimePoint belongs to an IrregularIntervalSchedule.
        """
        #: The time is relative the BasicTimeSchedule.startTime.
        self.time = time

        #: The first value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
        self.value1 = value1

        #: The second value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
        self.value2 = value2

        self._IntervalSchedule = None
        self.IntervalSchedule = IntervalSchedule

        super(IrregularTimePoint, self).__init__(*args, **kw_args)

    def getIntervalSchedule(self):
        """An IrregularTimePoint belongs to an IrregularIntervalSchedule.
        """
        return self._IntervalSchedule

    def setIntervalSchedule(self, value):
        if self._IntervalSchedule is not None:
            filtered = [x for x in self.IntervalSchedule.TimePoints if x != self]
            self._IntervalSchedule._TimePoints = filtered

        self._IntervalSchedule = value
        if self._IntervalSchedule is not None:
            self._IntervalSchedule._TimePoints.append(self)

    IntervalSchedule = property(getIntervalSchedule, setIntervalSchedule)

