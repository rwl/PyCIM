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

from CIM14v13.IEC61970.Core.Curve import Curve

class FuelAllocationSchedule(Curve):
    """The amount of fuel of a given type which is allocated for consumption over a specified period of time
    """

    def __init__(self, fuelType='gas', minFuelAllocation=0.0, fuelAllocationStartDate='', maxFuelAllocation=0.0, fuelAllocationEndDate='', ThermalGeneratingUnit=None, FossilFuel=None, *args, **kw_args):
        """Initializes a new 'FuelAllocationSchedule' instance.

        @param fuelType: The type of fuel, which also indicates the corresponding measurement unit Values are: "gas", "oil", "coal", "lignite"
        @param minFuelAllocation: The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract 
        @param fuelAllocationStartDate: The start time and date of the fuel allocation schedule 
        @param maxFuelAllocation: The maximum amount fuel that is allocated for consumption for the scheduled time period 
        @param fuelAllocationEndDate: The end time and date of the fuel allocation schedule 
        @param ThermalGeneratingUnit: A thermal generating unit may have one or more fuel allocation schedules
        @param FossilFuel: A fuel allocation schedule must have a fossil fuel
        """
        #: The type of fuel, which also indicates the corresponding measurement unitValues are: "gas", "oil", "coal", "lignite"
        self.fuelType = fuelType

        #: The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract
        self.minFuelAllocation = minFuelAllocation

        #: The start time and date of the fuel allocation schedule
        self.fuelAllocationStartDate = fuelAllocationStartDate

        #: The maximum amount fuel that is allocated for consumption for the scheduled time period
        self.maxFuelAllocation = maxFuelAllocation

        #: The end time and date of the fuel allocation schedule
        self.fuelAllocationEndDate = fuelAllocationEndDate

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        self._FossilFuel = None
        self.FossilFuel = FossilFuel

        super(FuelAllocationSchedule, self).__init__(*args, **kw_args)

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
            self._ThermalGeneratingUnit._FuelAllocationSchedules.append(self)

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)

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
            self._FossilFuel._FuelAllocationSchedules.append(self)

    FossilFuel = property(getFossilFuel, setFossilFuel)

