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

from CIM14.IEC61970.Meas.Measurement import Measurement

class Accumulator(Measurement):
    """Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.
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
            x._Accumulator = None
        for y in value:
            y._Accumulator = self
        self._AccumulatorValues = value

    AccumulatorValues = property(getAccumulatorValues, setAccumulatorValues)

    def addAccumulatorValues(self, *AccumulatorValues):
        for obj in AccumulatorValues:
            obj._Accumulator = self
            self._AccumulatorValues.append(obj)

    def removeAccumulatorValues(self, *AccumulatorValues):
        for obj in AccumulatorValues:
            obj._Accumulator = None
            self._AccumulatorValues.remove(obj)

