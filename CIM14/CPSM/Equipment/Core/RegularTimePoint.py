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

from CIM14.CPSM.Equipment.Element import Element

class RegularTimePoint(Element):
    """TimePoints for a schedule where the time between the points is constant.-  The RegularTimePoint class is used to represent points for various schedules that derive from the RegularIntervalSchedule class.  The schedules defined in this profile are: ConformLoadSchedule NonConformLoadSchedule RegulationSchedule -  The first SequenceNumber for a schedule is 1.  0 is not an allowed value.  The first time point is defined with SequenceNumber = 1. 
    """

    def __init__(self, sequenceNumber=0, value1=0.0, value2=0.0, IntervalSchedule=None, *args, **kw_args):
        """Initialises a new 'RegularTimePoint' instance.

        @param sequenceNumber: The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime. 
        @param value1: The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        @param value2: The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        @param IntervalSchedule: A RegularTimePoint belongs to a RegularIntervalSchedule.
        """
        #: The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.
        self.sequenceNumber = sequenceNumber

        #: The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
        self.value1 = value1

        #: The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
        self.value2 = value2

        self._IntervalSchedule = None
        self.IntervalSchedule = IntervalSchedule

        super(RegularTimePoint, self).__init__(*args, **kw_args)

    _attrs = ["sequenceNumber", "value1", "value2"]
    _attr_types = {"sequenceNumber": int, "value1": float, "value2": float}
    _defaults = {"sequenceNumber": 0, "value1": 0.0, "value2": 0.0}
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

