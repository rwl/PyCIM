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

class AnalogValue(MeasurementValue):
    """AnalogValue represents an analog MeasurementValue.
    """

    def __init__(self, value=0.0, AltTieMeas=None, Analog=None, AltGeneratingUnit=None, **kw_args):
        """Initializes a new 'AnalogValue' instance.

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

        super(AnalogValue, self).__init__(**kw_args)

    def getAltTieMeas(self):
        """The usage of the measurement within the control area specification.
        """
        return self._AltTieMeas

    def setAltTieMeas(self, value):
        for x in self._AltTieMeas:
            x._AnalogValue = None
        for y in value:
            y._AnalogValue = self
        self._AltTieMeas = value

    AltTieMeas = property(getAltTieMeas, setAltTieMeas)

    def addAltTieMeas(self, *AltTieMeas):
        for obj in AltTieMeas:
            obj._AnalogValue = self
            self._AltTieMeas.append(obj)

    def removeAltTieMeas(self, *AltTieMeas):
        for obj in AltTieMeas:
            obj._AnalogValue = None
            self._AltTieMeas.remove(obj)

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
            self._Analog._AnalogValues.append(self)

    Analog = property(getAnalog, setAnalog)

    def getAltGeneratingUnit(self):
        """The alternate generating unit for which this measurement value applies.
        """
        return self._AltGeneratingUnit

    def setAltGeneratingUnit(self, value):
        for x in self._AltGeneratingUnit:
            x._AnalogValue = None
        for y in value:
            y._AnalogValue = self
        self._AltGeneratingUnit = value

    AltGeneratingUnit = property(getAltGeneratingUnit, setAltGeneratingUnit)

    def addAltGeneratingUnit(self, *AltGeneratingUnit):
        for obj in AltGeneratingUnit:
            obj._AnalogValue = self
            self._AltGeneratingUnit.append(obj)

    def removeAltGeneratingUnit(self, *AltGeneratingUnit):
        for obj in AltGeneratingUnit:
            obj._AnalogValue = None
            self._AltGeneratingUnit.remove(obj)

