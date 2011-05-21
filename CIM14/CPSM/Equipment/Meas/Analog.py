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

class Analog(Measurement):
    """Analog represents an analog Measurement.-  The positiveFlowIn attribute is only required if the Measurement measures a directional flow of power. -  The association to Terminal may not be required depending on how the Measurement is being used.  See section Use of Measurement Class for details. -  The MeasurementType class is used to define the quantity being measured (Voltage, ThreePhaseActivePower, etc.) by a Measurement.  A Measurement must be associated with one and only one measurementType.  The valid values for MeasurementType.name are defined in Normative String Tables. 
    """

    def __init__(self, positiveFlowIn=False, AnalogValues=None, *args, **kw_args):
        """Initialises a new 'Analog' instance.

        @param positiveFlowIn: If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource. 
        @param AnalogValues: The values connected to this measurement.
        """
        #: If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.
        self.positiveFlowIn = positiveFlowIn

        self._AnalogValues = []
        self.AnalogValues = [] if AnalogValues is None else AnalogValues

        super(Analog, self).__init__(*args, **kw_args)

    _attrs = ["positiveFlowIn"]
    _attr_types = {"positiveFlowIn": bool}
    _defaults = {"positiveFlowIn": False}
    _enums = {}
    _refs = ["AnalogValues"]
    _many_refs = ["AnalogValues"]

    def getAnalogValues(self):
        """The values connected to this measurement.
        """
        return self._AnalogValues

    def setAnalogValues(self, value):
        for x in self._AnalogValues:
            x.Analog = None
        for y in value:
            y._Analog = self
        self._AnalogValues = value

    AnalogValues = property(getAnalogValues, setAnalogValues)

    def addAnalogValues(self, *AnalogValues):
        for obj in AnalogValues:
            obj.Analog = self

    def removeAnalogValues(self, *AnalogValues):
        for obj in AnalogValues:
            obj.Analog = None

