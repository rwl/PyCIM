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

from CIM15.IEC61970.Meas.Measurement import Measurement

class Accumulator(Measurement):
    """Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.
    """

    def __init__(self, maxValue=0, LimitSets=None, AccumulatorValues=None, *args, **kw_args):
        """Initialises a new 'Accumulator' instance.

        @param maxValue: Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values. 
        @param LimitSets: A measurement may have zero or more limit ranges defined for it.
        @param AccumulatorValues: The values connected to this measurement.
        """
        #: Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
        self.maxValue = maxValue

        self._LimitSets = []
        self.LimitSets = [] if LimitSets is None else LimitSets

        self._AccumulatorValues = []
        self.AccumulatorValues = [] if AccumulatorValues is None else AccumulatorValues

        super(Accumulator, self).__init__(*args, **kw_args)

    _attrs = ["maxValue"]
    _attr_types = {"maxValue": int}
    _defaults = {"maxValue": 0}
    _enums = {}
    _refs = ["LimitSets", "AccumulatorValues"]
    _many_refs = ["LimitSets", "AccumulatorValues"]

    def getLimitSets(self):
        """A measurement may have zero or more limit ranges defined for it.
        """
        return self._LimitSets

    def setLimitSets(self, value):
        for p in self._LimitSets:
            filtered = [q for q in p.Measurements if q != self]
            self._LimitSets._Measurements = filtered
        for r in value:
            if self not in r._Measurements:
                r._Measurements.append(self)
        self._LimitSets = value

    LimitSets = property(getLimitSets, setLimitSets)

    def addLimitSets(self, *LimitSets):
        for obj in LimitSets:
            if self not in obj._Measurements:
                obj._Measurements.append(self)
            self._LimitSets.append(obj)

    def removeLimitSets(self, *LimitSets):
        for obj in LimitSets:
            if self in obj._Measurements:
                obj._Measurements.remove(self)
            self._LimitSets.remove(obj)

    def getAccumulatorValues(self):
        """The values connected to this measurement.
        """
        return self._AccumulatorValues

    def setAccumulatorValues(self, value):
        for x in self._AccumulatorValues:
            x.Accumulator = None
        for y in value:
            y._Accumulator = self
        self._AccumulatorValues = value

    AccumulatorValues = property(getAccumulatorValues, setAccumulatorValues)

    def addAccumulatorValues(self, *AccumulatorValues):
        for obj in AccumulatorValues:
            obj.Accumulator = self

    def removeAccumulatorValues(self, *AccumulatorValues):
        for obj in AccumulatorValues:
            obj.Accumulator = None

