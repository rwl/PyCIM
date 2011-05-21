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

from CIM14.CPSM.Equipment.Meas.Measurement import Measurement

class Accumulator(Measurement):
    """Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.-  The association to Terminal may not be required depending on how the Measurement is being used.  See section Use of Measurement Class for details. -  The MeasurementType class is used to define the quantity being measured (Voltage, ThreePhaseActivePower, etc.) by a Measurement.  A Measurement must be associated with one and only one measurementType.  The valid values for MeasurementType.name are defined in Normative String Tables. 
    """

    def __init__(self, AccumulatorValues=None, *args, **kw_args):
        """Initialises a new 'Accumulator' instance.

        @param AccumulatorValues: The values connected to this measurement.
        """
        self._AccumulatorValues = []
        self.AccumulatorValues = [] if AccumulatorValues is None else AccumulatorValues

        super(Accumulator, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["AccumulatorValues"]
    _many_refs = ["AccumulatorValues"]

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

