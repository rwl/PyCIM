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

from CIM14.IEC61970.Core.EquipmentContainer import EquipmentContainer

class Bay(EquipmentContainer):
    """A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.
    """

    def __init__(self, busBarConfiguration="mainWithTransfer", breakerConfiguration="breakerAndAHalf", bayPowerMeasFlag=False, bayEnergyMeasFlag=False, Substation=None, VoltageLevel=None, *args, **kw_args):
        """Initialises a new 'Bay' instance.

        @param busBarConfiguration: Bus bar configuration. Values are: "mainWithTransfer", "ringBus", "singleBus", "doubleBus"
        @param breakerConfiguration: Breaker configuration. Values are: "breakerAndAHalf", "singleBreaker", "noBreaker", "doubleBreaker"
        @param bayPowerMeasFlag: Indicates the presence/absence of active/reactive power measurements. 
        @param bayEnergyMeasFlag: Indicates the presence/absence of energy measurements. 
        @param Substation: The association is used in the naming hierarchy.
        @param VoltageLevel: The association is used in the naming hierarchy.
        """
        #: Bus bar configuration. Values are: "mainWithTransfer", "ringBus", "singleBus", "doubleBus"
        self.busBarConfiguration = busBarConfiguration

        #: Breaker configuration. Values are: "breakerAndAHalf", "singleBreaker", "noBreaker", "doubleBreaker"
        self.breakerConfiguration = breakerConfiguration

        #: Indicates the presence/absence of active/reactive power measurements.
        self.bayPowerMeasFlag = bayPowerMeasFlag

        #: Indicates the presence/absence of energy measurements.
        self.bayEnergyMeasFlag = bayEnergyMeasFlag

        self._Substation = None
        self.Substation = Substation

        self._VoltageLevel = None
        self.VoltageLevel = VoltageLevel

        super(Bay, self).__init__(*args, **kw_args)

    _attrs = ["busBarConfiguration", "breakerConfiguration", "bayPowerMeasFlag", "bayEnergyMeasFlag"]
    _attr_types = {"busBarConfiguration": str, "breakerConfiguration": str, "bayPowerMeasFlag": bool, "bayEnergyMeasFlag": bool}
    _defaults = {"busBarConfiguration": "mainWithTransfer", "breakerConfiguration": "breakerAndAHalf", "bayPowerMeasFlag": False, "bayEnergyMeasFlag": False}
    _enums = {"busBarConfiguration": "BusbarConfiguration", "breakerConfiguration": "BreakerConfiguration"}
    _refs = ["Substation", "VoltageLevel"]
    _many_refs = []

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

