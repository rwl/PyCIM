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

from CIM14.IEC61970.Core.Curve import Curve

class FuelAllocationSchedule(Curve):
    """The amount of fuel of a given type which is allocated for consumption over a specified period of time
    """

    def __init__(self, fuelType="lignite", minFuelAllocation=0.0, fuelAllocationStartDate='', maxFuelAllocation=0.0, fuelAllocationEndDate='', FossilFuel=None, ThermalGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'FuelAllocationSchedule' instance.

        @param fuelType: The type of fuel, which also indicates the corresponding measurement unit Values are: "lignite", "coal", "oil", "gas"
        @param minFuelAllocation: The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract 
        @param fuelAllocationStartDate: The start time and date of the fuel allocation schedule 
        @param maxFuelAllocation: The maximum amount fuel that is allocated for consumption for the scheduled time period 
        @param fuelAllocationEndDate: The end time and date of the fuel allocation schedule 
        @param FossilFuel: A fuel allocation schedule must have a fossil fuel
        @param ThermalGeneratingUnit: A thermal generating unit may have one or more fuel allocation schedules
        """
        #: The type of fuel, which also indicates the corresponding measurement unit Values are: "lignite", "coal", "oil", "gas"
        self.fuelType = fuelType

        #: The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract
        self.minFuelAllocation = minFuelAllocation

        #: The start time and date of the fuel allocation schedule
        self.fuelAllocationStartDate = fuelAllocationStartDate

        #: The maximum amount fuel that is allocated for consumption for the scheduled time period
        self.maxFuelAllocation = maxFuelAllocation

        #: The end time and date of the fuel allocation schedule
        self.fuelAllocationEndDate = fuelAllocationEndDate

        self._FossilFuel = None
        self.FossilFuel = FossilFuel

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(FuelAllocationSchedule, self).__init__(*args, **kw_args)

    _attrs = ["fuelType", "minFuelAllocation", "fuelAllocationStartDate", "maxFuelAllocation", "fuelAllocationEndDate"]
    _attr_types = {"fuelType": str, "minFuelAllocation": float, "fuelAllocationStartDate": str, "maxFuelAllocation": float, "fuelAllocationEndDate": str}
    _defaults = {"fuelType": "lignite", "minFuelAllocation": 0.0, "fuelAllocationStartDate": '', "maxFuelAllocation": 0.0, "fuelAllocationEndDate": ''}
    _enums = {"fuelType": "FuelType"}
    _refs = ["FossilFuel", "ThermalGeneratingUnit"]
    _many_refs = []

    def getFossilFuel(self):
        """A fuel allocation schedule must have a fossil fuel
        """
        return self._FossilFuel

    def setFossilFuel(self, value):
        if self._FossilFuel is not None:
            filtered = [x for x in self.FossilFuel.FuelAllocationSchedules if x != self]
            self._FossilFuel._FuelAllocationSchedules = filtered

        self._FossilFuel = value
        if self._FossilFuel is not None:
            if self not in self._FossilFuel._FuelAllocationSchedules:
                self._FossilFuel._FuelAllocationSchedules.append(self)

    FossilFuel = property(getFossilFuel, setFossilFuel)

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may have one or more fuel allocation schedules
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            filtered = [x for x in self.ThermalGeneratingUnit.FuelAllocationSchedules if x != self]
            self._ThermalGeneratingUnit._FuelAllocationSchedules = filtered

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            if self not in self._ThermalGeneratingUnit._FuelAllocationSchedules:
                self._ThermalGeneratingUnit._FuelAllocationSchedules.append(self)

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)

