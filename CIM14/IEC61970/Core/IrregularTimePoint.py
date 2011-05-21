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

from CIM14.Element import Element

class IrregularTimePoint(Element):
    """TimePoints for a schedule where the time between the points varies.
    """

    def __init__(self, time=0.0, value2=0.0, value1=0.0, IntervalSchedule=None, *args, **kw_args):
        """Initialises a new 'IrregularTimePoint' instance.

        @param time: The time is relative the BasicTimeSchedule.startTime. 
        @param value2: The second value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule. 
        @param value1: The first value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule. 
        @param IntervalSchedule: An IrregularTimePoint belongs to an IrregularIntervalSchedule.
        """
        #: The time is relative the BasicTimeSchedule.startTime.
        self.time = time

        #: The second value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
        self.value2 = value2

        #: The first value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
        self.value1 = value1

        self._IntervalSchedule = None
        self.IntervalSchedule = IntervalSchedule

        super(IrregularTimePoint, self).__init__(*args, **kw_args)

    _attrs = ["time", "value2", "value1"]
    _attr_types = {"time": float, "value2": float, "value1": float}
    _defaults = {"time": 0.0, "value2": 0.0, "value1": 0.0}
    _enums = {}
    _refs = ["IntervalSchedule"]
    _many_refs = []

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
            if self not in self._IntervalSchedule._TimePoints:
                self._IntervalSchedule._TimePoints.append(self)

    IntervalSchedule = property(getIntervalSchedule, setIntervalSchedule)

