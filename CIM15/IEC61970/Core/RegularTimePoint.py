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

class RegularTimePoint(Element):
    """TimePoints for a schedule where the time between the points is constant.TimePoints for a schedule where the time between the points is constant.
    """

    def __init__(self, value2=0.0, value1=0.0, sequenceNumber=0, IntervalSchedule=None, *args, **kw_args):
        """Initialises a new 'RegularTimePoint' instance.

        @param value2: The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        @param value1: The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
        @param sequenceNumber: The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime. 
        @param IntervalSchedule: A RegularTimePoint belongs to a RegularIntervalSchedule.
        """
        #: The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
        self.value2 = value2

        #: The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
        self.value1 = value1

        #: The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.
        self.sequenceNumber = sequenceNumber

        self._IntervalSchedule = None
        self.IntervalSchedule = IntervalSchedule

        super(RegularTimePoint, self).__init__(*args, **kw_args)

    _attrs = ["value2", "value1", "sequenceNumber"]
    _attr_types = {"value2": float, "value1": float, "sequenceNumber": int}
    _defaults = {"value2": 0.0, "value1": 0.0, "sequenceNumber": 0}
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

