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

from CIM14v13.IEC61970.Meas.MeasurementValue import MeasurementValue

class AccumulatorValue(MeasurementValue):
    """AccumulatorValue represents a accumulated (counted) MeasurementValue.
    """

    def __init__(self, value=0, Accumulator=None, **kw_args):
        """Initializes a new 'AccumulatorValue' instance.

        @param value: The value to supervise. The value is positive. 
        @param Accumulator: Measurement to which this value is connected.
        """
        #: The value to supervise. The value is positive.
        self.value = value

        self._Accumulator = None
        self.Accumulator = Accumulator

        super(AccumulatorValue, self).__init__(**kw_args)

    def getAccumulator(self):
        """Measurement to which this value is connected.
        """
        return self._Accumulator

    def setAccumulator(self, value):
        if self._Accumulator is not None:
            filtered = [x for x in self.Accumulator.AccumulatorValues if x != self]
            self._Accumulator._AccumulatorValues = filtered

        self._Accumulator = value
        if self._Accumulator is not None:
            self._Accumulator._AccumulatorValues.append(self)

    Accumulator = property(getAccumulator, setAccumulator)

