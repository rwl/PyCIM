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

from CIM15.IEC61970.Meas.Limit import Limit

class AccumulatorLimit(Limit):
    """Limit values for Accumulator measurementsLimit values for Accumulator measurements
    """

    def __init__(self, value=0, LimitSet=None, *args, **kw_args):
        """Initialises a new 'AccumulatorLimit' instance.

        @param value: The value to supervise against. The value is positive. 
        @param LimitSet: The set of limits.
        """
        #: The value to supervise against. The value is positive.
        self.value = value

        self._LimitSet = None
        self.LimitSet = LimitSet

        super(AccumulatorLimit, self).__init__(*args, **kw_args)

    _attrs = ["value"]
    _attr_types = {"value": int}
    _defaults = {"value": 0}
    _enums = {}
    _refs = ["LimitSet"]
    _many_refs = []

    def getLimitSet(self):
        """The set of limits.
        """
        return self._LimitSet

    def setLimitSet(self, value):
        if self._LimitSet is not None:
            filtered = [x for x in self.LimitSet.Limits if x != self]
            self._LimitSet._Limits = filtered

        self._LimitSet = value
        if self._LimitSet is not None:
            if self not in self._LimitSet._Limits:
                self._LimitSet._Limits.append(self)

    LimitSet = property(getLimitSet, setLimitSet)

