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

from CIM14v13.IEC61970.Meas.Measurement import Measurement

class Accumulator(Measurement):
    """Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.
    """

    def __init__(self, maxValue=0, AccumulatorValues=None, LimitSets=None, **kw_args):
        """Initializes a new 'Accumulator' instance.

        @param maxValue: Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values. 
        @param AccumulatorValues: The values connected to this measurement.
        @param LimitSets: A measurement may have zero or more limit ranges defined for it.
        """
        #: Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
        self.maxValue = maxValue

        self._AccumulatorValues = []
        self.AccumulatorValues = [] if AccumulatorValues is None else AccumulatorValues

        self._LimitSets = []
        self.LimitSets = [] if LimitSets is None else LimitSets

        super(Accumulator, self).__init__(**kw_args)

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

