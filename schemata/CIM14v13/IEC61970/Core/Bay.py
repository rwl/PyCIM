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

from CIM14v13.IEC61970.Core.EquipmentContainer import EquipmentContainer

class Bay(EquipmentContainer):
    """A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.
    """

    def __init__(self, breakerConfiguration='noBreaker', busBarConfiguration='ringBus', bayEnergyMeasFlag=False, bayPowerMeasFlag=False, VoltageLevel=None, Substation=None, *args, **kw_args):
        """Initializes a new 'Bay' instance.

        @param breakerConfiguration: Breaker configuration. Values are: "noBreaker", "doubleBreaker", "singleBreaker", "breakerAndAHalf"
        @param busBarConfiguration: Bus bar configuration. Values are: "ringBus", "doubleBus", "mainWithTransfer", "singleBus"
        @param bayEnergyMeasFlag: Indicates the presence/absence of energy measurements. 
        @param bayPowerMeasFlag: Indicates the presence/absence of active/reactive power measurements. 
        @param VoltageLevel: The association is used in the naming hierarchy.
        @param Substation: The association is used in the naming hierarchy.
        """
        #: Breaker configuration. Values are: "noBreaker", "doubleBreaker", "singleBreaker", "breakerAndAHalf"
        self.breakerConfiguration = breakerConfiguration

        #: Bus bar configuration. Values are: "ringBus", "doubleBus", "mainWithTransfer", "singleBus"
        self.busBarConfiguration = busBarConfiguration

        #: Indicates the presence/absence of energy measurements. 
        self.bayEnergyMeasFlag = bayEnergyMeasFlag

        #: Indicates the presence/absence of active/reactive power measurements. 
        self.bayPowerMeasFlag = bayPowerMeasFlag

        self._VoltageLevel = None
        self.VoltageLevel = VoltageLevel

        self._Substation = None
        self.Substation = Substation

        super(Bay, self).__init__(*args, **kw_args)

    def getVoltageLevel(self):
        """The association is used in the naming hierarchy.
        """
        return self._VoltageLevel

    def setVoltageLevel(self, value):
        if self._VoltageLevel is not None:
            filtered = [x for x in self.VoltageLevel.Bays if x != self]
            self._VoltageLevel._Bays = filtered

        self._VoltageLevel = value
        if self._VoltageLevel is not None:
            self._VoltageLevel._Bays.append(self)

    VoltageLevel = property(getVoltageLevel, setVoltageLevel)

    def getSubstation(self):
        """The association is used in the naming hierarchy.
        """
        return self._Substation

    def setSubstation(self, value):
        if self._Substation is not None:
            filtered = [x for x in self.Substation.Bays if x != self]
            self._Substation._Bays = filtered

        self._Substation = value
        if self._Substation is not None:
            self._Substation._Bays.append(self)

    Substation = property(getSubstation, setSubstation)

