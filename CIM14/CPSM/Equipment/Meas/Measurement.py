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

from CIM14.CPSM.Equipment.Core.IdentifiedObject import IdentifiedObject

class Measurement(IdentifiedObject):
    """A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
    """

    def __init__(self, measurementType='', Unit=None, Terminal=None, PowerSystemResource=None, *args, **kw_args):
        """Initialises a new 'Measurement' instance.

        @param measurementType: Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. 
        @param Unit: The Unit for the Measurement
        @param Terminal: One or more measurements may be associated with a terminal in the network
        @param PowerSystemResource: The PowerSystemResource that contains the Measurement in the naming hierarchy
        """
        #: Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc.
        self.measurementType = measurementType

        self._Unit = None
        self.Unit = Unit

        self._Terminal = None
        self.Terminal = Terminal

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        super(Measurement, self).__init__(*args, **kw_args)

    _attrs = ["measurementType"]
    _attr_types = {"measurementType": str}
    _defaults = {"measurementType": ''}
    _enums = {}
    _refs = ["Unit", "Terminal", "PowerSystemResource"]
    _many_refs = []

    def getUnit(self):
        """The Unit for the Measurement
        """
        return self._Unit

    def setUnit(self, value):
        if self._Unit is not None:
            filtered = [x for x in self.Unit.Measurements if x != self]
            self._Unit._Measurements = filtered

        self._Unit = value
        if self._Unit is not None:
            if self not in self._Unit._Measurements:
                self._Unit._Measurements.append(self)

    Unit = property(getUnit, setUnit)

    def getTerminal(self):
        """One or more measurements may be associated with a terminal in the network
        """
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            filtered = [x for x in self.Terminal.Measurements if x != self]
            self._Terminal._Measurements = filtered

        self._Terminal = value
        if self._Terminal is not None:
            if self not in self._Terminal._Measurements:
                self._Terminal._Measurements.append(self)

    Terminal = property(getTerminal, setTerminal)

    def getPowerSystemResource(self):
        """The PowerSystemResource that contains the Measurement in the naming hierarchy
        """
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.Measurements if x != self]
            self._PowerSystemResource._Measurements = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            if self not in self._PowerSystemResource._Measurements:
                self._PowerSystemResource._Measurements.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

