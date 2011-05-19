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

from CIM15.IEC61970.Core.Curve import Curve

class FuelAllocationSchedule(Curve):
    """The amount of fuel of a given type which is allocated for consumption over a specified period of timeThe amount of fuel of a given type which is allocated for consumption over a specified period of time
    """

    def __init__(self, minFuelAllocation=0.0, fuelAllocationEndDate='', maxFuelAllocation=0.0, fuelAllocationStartDate='', fuelType="oil", FossilFuel=None, ThermalGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'FuelAllocationSchedule' instance.

        @param minFuelAllocation: The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract 
        @param fuelAllocationEndDate: The end time and date of the fuel allocation schedule 
        @param maxFuelAllocation: The maximum amount fuel that is allocated for consumption for the scheduled time period 
        @param fuelAllocationStartDate: The start time and date of the fuel allocation schedule 
        @param fuelType: The type of fuel, which also indicates the corresponding measurement unit Values are: "oil", "coal", "lignite", "gas"
        @param FossilFuel: A fuel allocation schedule must have a fossil fuel
        @param ThermalGeneratingUnit: A thermal generating unit may have one or more fuel allocation schedules
        """
        #: The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract
        self.minFuelAllocation = minFuelAllocation

        #: The end time and date of the fuel allocation schedule
        self.fuelAllocationEndDate = fuelAllocationEndDate

        #: The maximum amount fuel that is allocated for consumption for the scheduled time period
        self.maxFuelAllocation = maxFuelAllocation

        #: The start time and date of the fuel allocation schedule
        self.fuelAllocationStartDate = fuelAllocationStartDate

        #: The type of fuel, which also indicates the corresponding measurement unit Values are: "oil", "coal", "lignite", "gas"
        self.fuelType = fuelType

        self._FossilFuel = None
        self.FossilFuel = FossilFuel

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(FuelAllocationSchedule, self).__init__(*args, **kw_args)

    _attrs = ["minFuelAllocation", "fuelAllocationEndDate", "maxFuelAllocation", "fuelAllocationStartDate", "fuelType"]
    _attr_types = {"minFuelAllocation": float, "fuelAllocationEndDate": str, "maxFuelAllocation": float, "fuelAllocationStartDate": str, "fuelType": str}
    _defaults = {"minFuelAllocation": 0.0, "fuelAllocationEndDate": '', "maxFuelAllocation": 0.0, "fuelAllocationStartDate": '', "fuelType": "oil"}
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

