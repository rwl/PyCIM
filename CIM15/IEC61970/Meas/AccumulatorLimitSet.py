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

from CIM15.IEC61970.Meas.LimitSet import LimitSet

class AccumulatorLimitSet(LimitSet):
    """An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.
    """

    def __init__(self, Limits=None, Measurements=None, *args, **kw_args):
        """Initialises a new 'AccumulatorLimitSet' instance.

        @param Limits: The limit values used for supervision of Measurements.
        @param Measurements: The Measurements using the LimitSet.
        """
        self._Limits = []
        self.Limits = [] if Limits is None else Limits

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        super(AccumulatorLimitSet, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Limits", "Measurements"]
    _many_refs = ["Limits", "Measurements"]

    def getLimits(self):
        """The limit values used for supervision of Measurements.
        """
        return self._Limits

    def setLimits(self, value):
        for x in self._Limits:
            x.LimitSet = None
        for y in value:
            y._LimitSet = self
        self._Limits = value

    Limits = property(getLimits, setLimits)

    def addLimits(self, *Limits):
        for obj in Limits:
            obj.LimitSet = self

    def removeLimits(self, *Limits):
        for obj in Limits:
            obj.LimitSet = None

    def getMeasurements(self):
        """The Measurements using the LimitSet.
        """
        return self._Measurements

    def setMeasurements(self, value):
        for p in self._Measurements:
            filtered = [q for q in p.LimitSets if q != self]
            self._Measurements._LimitSets = filtered
        for r in value:
            if self not in r._LimitSets:
                r._LimitSets.append(self)
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            if self not in obj._LimitSets:
                obj._LimitSets.append(self)
            self._Measurements.append(obj)

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            if self in obj._LimitSets:
                obj._LimitSets.remove(self)
            self._Measurements.remove(obj)

