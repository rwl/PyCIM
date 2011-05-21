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

from CIM14.CPSM.Equipment.Meas.MeasurementValue import MeasurementValue

class AccumulatorValue(MeasurementValue):
    """AccumulatorValue represents a accumulated (counted) MeasurementValue.
    """

    def __init__(self, Accumulator=None, *args, **kw_args):
        """Initialises a new 'AccumulatorValue' instance.

        @param Accumulator: Measurement to which this value is connected.
        """
        self._Accumulator = None
        self.Accumulator = Accumulator

        super(AccumulatorValue, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Accumulator"]
    _many_refs = []

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
            if self not in self._Accumulator._AccumulatorValues:
                self._Accumulator._AccumulatorValues.append(self)

    Accumulator = property(getAccumulator, setAccumulator)

