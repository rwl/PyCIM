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

from CIM14.Element import Element

class RegularTimePoint(Element):
    """TimePoints for a schedule where the time between the points is constant.
    """

    def __init__(self, value1=0.0, sequenceNumber=0, value2=0.0, IntervalSchedule=None, *args, **kw_args):
        """Initialises a new 'RegularTimePoint' instance.

        @param value1: The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        @param sequenceNumber: The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime. 
        @param value2: The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        @param IntervalSchedule: A RegularTimePoint belongs to a RegularIntervalSchedule.
        """
        #: The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
        self.value1 = value1

        #: The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.
        self.sequenceNumber = sequenceNumber

        #: The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
        self.value2 = value2

        self._IntervalSchedule = None
        self.IntervalSchedule = IntervalSchedule

        super(RegularTimePoint, self).__init__(*args, **kw_args)

    _attrs = ["value1", "sequenceNumber", "value2"]
    _attr_types = {"value1": float, "sequenceNumber": int, "value2": float}
    _defaults = {"value1": 0.0, "sequenceNumber": 0, "value2": 0.0}
    _enums = {}
    _refs = ["IntervalSchedule"]
    _many_refs = []

    def getIntervalSchedule(self):
        """A RegularTimePoint belongs to a RegularIntervalSchedule.
        """
        return self._IntervalSchedule

    def setIntervalSchedule(self, value):
        if self._IntervalSchedule is not None:
            filtered = [x for x in self.IntervalSchedule.TimePoints if x != self]
            self._IntervalSchedule._TimePoints = filtered

        self._IntervalSchedule = value
        if self._IntervalSchedule is not None:
            if self not in self._IntervalSchedule._TimePoints:
                self._IntervalSchedule._TimePoints.append(self)

    IntervalSchedule = property(getIntervalSchedule, setIntervalSchedule)

