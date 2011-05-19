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

from CIM15.IEC61970.Meas.MeasurementValue import MeasurementValue

class AnalogValue(MeasurementValue):
    """AnalogValue represents an analog MeasurementValue.AnalogValue represents an analog MeasurementValue.
    """

    def __init__(self, value=0.0, AltTieMeas=None, Analog=None, AltGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'AnalogValue' instance.

        @param value: The value to supervise. 
        @param AltTieMeas: The usage of the measurement within the control area specification.
        @param Analog: Measurement to which this value is connected.
        @param AltGeneratingUnit: The alternate generating unit for which this measurement value applies.
        """
        #: The value to supervise.
        self.value = value

        self._AltTieMeas = []
        self.AltTieMeas = [] if AltTieMeas is None else AltTieMeas

        self._Analog = None
        self.Analog = Analog

        self._AltGeneratingUnit = []
        self.AltGeneratingUnit = [] if AltGeneratingUnit is None else AltGeneratingUnit

        super(AnalogValue, self).__init__(*args, **kw_args)

    _attrs = ["value"]
    _attr_types = {"value": float}
    _defaults = {"value": 0.0}
    _enums = {}
    _refs = ["AltTieMeas", "Analog", "AltGeneratingUnit"]
    _many_refs = ["AltTieMeas", "AltGeneratingUnit"]

    def getAltTieMeas(self):
        """The usage of the measurement within the control area specification.
        """
        return self._AltTieMeas

    def setAltTieMeas(self, value):
        for x in self._AltTieMeas:
            x.AnalogValue = None
        for y in value:
            y._AnalogValue = self
        self._AltTieMeas = value

    AltTieMeas = property(getAltTieMeas, setAltTieMeas)

    def addAltTieMeas(self, *AltTieMeas):
        for obj in AltTieMeas:
            obj.AnalogValue = self

    def removeAltTieMeas(self, *AltTieMeas):
        for obj in AltTieMeas:
            obj.AnalogValue = None

    def getAnalog(self):
        """Measurement to which this value is connected.
        """
        return self._Analog

    def setAnalog(self, value):
        if self._Analog is not None:
            filtered = [x for x in self.Analog.AnalogValues if x != self]
            self._Analog._AnalogValues = filtered

        self._Analog = value
        if self._Analog is not None:
            if self not in self._Analog._AnalogValues:
                self._Analog._AnalogValues.append(self)

    Analog = property(getAnalog, setAnalog)

    def getAltGeneratingUnit(self):
        """The alternate generating unit for which this measurement value applies.
        """
        return self._AltGeneratingUnit

    def setAltGeneratingUnit(self, value):
        for x in self._AltGeneratingUnit:
            x.AnalogValue = None
        for y in value:
            y._AnalogValue = self
        self._AltGeneratingUnit = value

    AltGeneratingUnit = property(getAltGeneratingUnit, setAltGeneratingUnit)

    def addAltGeneratingUnit(self, *AltGeneratingUnit):
        for obj in AltGeneratingUnit:
            obj.AnalogValue = self

    def removeAltGeneratingUnit(self, *AltGeneratingUnit):
        for obj in AltGeneratingUnit:
            obj.AnalogValue = None

