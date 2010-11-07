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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class FossilFuel(IdentifiedObject):
    """The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas
    """

    def __init__(self, fossilFuelType='lignite', fuelSulfur=0.0, fuelMixture=0.0, fuelCost=0.0, fuelHandlingCost=0.0, fuelEffFactor=0.0, fuelHeatContent=0.0, fuelDispatchCost=0.0, lowBreakpointP=0.0, highBreakpointP=0.0, FuelAllocationSchedules=None, ThermalGeneratingUnit=None, **kw_args):
        """Initializes a new 'FossilFuel' instance.

        @param fossilFuelType: The type of fossil fuel, such as coal, oil, or gas. Values are: "lignite", "coal", "oil", "gas"
        @param fuelSulfur: The fuel's fraction of pollution credit per unit of heat content 
        @param fuelMixture: Relative amount of the given type of fuel, when multiple fuels are being consumed. 
        @param fuelCost: The cost in terms of heat value for the given type of fuel 
        @param fuelHandlingCost: Handling and processing cost associated with this fuel 
        @param fuelEffFactor: The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed 
        @param fuelHeatContent: The amount of heat per weight (or volume) of the given type of fuel 
        @param fuelDispatchCost: The cost of fuel used for economic dispatching which includes: fuel cost, transportation cost,  and incremental maintenance cost 
        @param lowBreakpointP: The active power output level of the unit at which the given type of fuel is switched off. This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low active power output levels. 
        @param highBreakpointP: The active power output level of the unit at which the given type of fuel is switched on. This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high active power output levels. 
        @param FuelAllocationSchedules: A fuel allocation schedule must have a fossil fuel
        @param ThermalGeneratingUnit: A thermal generating unit may have one or more fossil fuels
        """
        #: The type of fossil fuel, such as coal, oil, or gas.Values are: "lignite", "coal", "oil", "gas"
        self.fossilFuelType = fossilFuelType

        #: The fuel's fraction of pollution credit per unit of heat content
        self.fuelSulfur = fuelSulfur

        #: Relative amount of the given type of fuel, when multiple fuels are being consumed.
        self.fuelMixture = fuelMixture

        #: The cost in terms of heat value for the given type of fuel
        self.fuelCost = fuelCost

        #: Handling and processing cost associated with this fuel
        self.fuelHandlingCost = fuelHandlingCost

        #: The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed
        self.fuelEffFactor = fuelEffFactor

        #: The amount of heat per weight (or volume) of the given type of fuel
        self.fuelHeatContent = fuelHeatContent

        #: The cost of fuel used for economic dispatching which includes: fuel cost, transportation cost,  and incremental maintenance cost
        self.fuelDispatchCost = fuelDispatchCost

        #: The active power output level of the unit at which the given type of fuel is switched off. This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low active power output levels.
        self.lowBreakpointP = lowBreakpointP

        #: The active power output level of the unit at which the given type of fuel is switched on. This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high active power output levels.
        self.highBreakpointP = highBreakpointP

        self._FuelAllocationSchedules = []
        self.FuelAllocationSchedules = [] if FuelAllocationSchedules is None else FuelAllocationSchedules

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(FossilFuel, self).__init__(**kw_args)

    def getFuelAllocationSchedules(self):
        """A fuel allocation schedule must have a fossil fuel
        """
        return self._FuelAllocationSchedules

    def setFuelAllocationSchedules(self, value):
        for x in self._FuelAllocationSchedules:
            x._FossilFuel = None
        for y in value:
            y._FossilFuel = self
        self._FuelAllocationSchedules = value

    FuelAllocationSchedules = property(getFuelAllocationSchedules, setFuelAllocationSchedules)

    def addFuelAllocationSchedules(self, *FuelAllocationSchedules):
        for obj in FuelAllocationSchedules:
            obj._FossilFuel = self
            self._FuelAllocationSchedules.append(obj)

    def removeFuelAllocationSchedules(self, *FuelAllocationSchedules):
        for obj in FuelAllocationSchedules:
            obj._FossilFuel = None
            self._FuelAllocationSchedules.remove(obj)

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may have one or more fossil fuels
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            filtered = [x for x in self.ThermalGeneratingUnit.FossilFuels if x != self]
            self._ThermalGeneratingUnit._FossilFuels = filtered

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._FossilFuels.append(self)

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)

