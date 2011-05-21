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

class Discrete(Measurement):
    """Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.-  The association to Terminal may not be required depending on how the Measurement is being used.  See section Use of Measurement Class for details. -  The MeasurementType class is used to define the quantity being measured (Voltage, ThreePhaseActivePower, etc.) by a Measurement.  A Measurement must be associated with one and only one measurementType.  The valid values for the MeasurementType name are defined in Normative String Tables. 
    """

    def __init__(self, DiscreteValues=None, *args, **kw_args):
        """Initialises a new 'Discrete' instance.

        @param DiscreteValues: The values connected to this measurement.
        """
        self._DiscreteValues = []
        self.DiscreteValues = [] if DiscreteValues is None else DiscreteValues

        super(Discrete, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["DiscreteValues"]
    _many_refs = ["DiscreteValues"]

    def getDiscreteValues(self):
        """The values connected to this measurement.
        """
        return self._DiscreteValues

    def setDiscreteValues(self, value):
        for x in self._DiscreteValues:
            x.Discrete = None
        for y in value:
            y._Discrete = self
        self._DiscreteValues = value

    DiscreteValues = property(getDiscreteValues, setDiscreteValues)

    def addDiscreteValues(self, *DiscreteValues):
        for obj in DiscreteValues:
            obj.Discrete = self

    def removeDiscreteValues(self, *DiscreteValues):
        for obj in DiscreteValues:
            obj.Discrete = None

