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

from CIM14.IEC61970.Meas.MeasurementValue import MeasurementValue

class AnalogValue(MeasurementValue):
    """AnalogValue represents an analog MeasurementValue.
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

