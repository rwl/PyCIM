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

from CIM16.IEC61970.Core.IdentifiedObject import IdentifiedObject

class FossilFuel(IdentifiedObject):
    """The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gasThe fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas
    """

    def __init__(self, fuelSulfur=0.0, fuelCost=0.0, fossilFuelType="oil", lowBreakpointP=0.0, fuelDispatchCost=0.0, fuelHandlingCost=0.0, fuelHeatContent=0.0, fuelEffFactor=0.0, fuelMixture=0.0, highBreakpointP=0.0, ThermalGeneratingUnit=None, FuelAllocationSchedules=None, *args, **kw_args):
        """Initialises a new 'FossilFuel' instance.

        @param fuelSulfur: The fuel's fraction of pollution credit per unit of heat content 
        @param fuelCost: The cost in terms of heat value for the given type of fuel 
        @param fossilFuelType: The type of fossil fuel, such as coal, oil, or gas. Values are: "oil", "coal", "lignite", "gas"
        @param lowBreakpointP: The active power output level of the unit at which the given type of fuel is switched off. This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low active power output levels. 
        @param fuelDispatchCost: The cost of fuel used for economic dispatching which includes: fuel cost, transportation cost,  and incremental maintenance cost 
        @param fuelHandlingCost: Handling and processing cost associated with this fuel 
        @param fuelHeatContent: The amount of heat per weight (or volume) of the given type of fuel 
        @param fuelEffFactor: The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed 
        @param fuelMixture: Relative amount of the given type of fuel, when multiple fuels are being consumed. 
        @param highBreakpointP: The active power output level of the unit at which the given type of fuel is switched on. This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high active power output levels. 
        @param ThermalGeneratingUnit: A thermal generating unit may have one or more fossil fuels
        @param FuelAllocationSchedules: A fuel allocation schedule must have a fossil fuel
        """
        #: The fuel's fraction of pollution credit per unit of heat content
        self.fuelSulfur = fuelSulfur

        #: The cost in terms of heat value for the given type of fuel
        self.fuelCost = fuelCost

        #: The type of fossil fuel, such as coal, oil, or gas. Values are: "oil", "coal", "lignite", "gas"
        self.fossilFuelType = fossilFuelType

        #: The active power output level of the unit at which the given type of fuel is switched off. This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low active power output levels.
        self.lowBreakpointP = lowBreakpointP

        #: The cost of fuel used for economic dispatching which includes: fuel cost, transportation cost,  and incremental maintenance cost
        self.fuelDispatchCost = fuelDispatchCost

        #: Handling and processing cost associated with this fuel
        self.fuelHandlingCost = fuelHandlingCost

        #: The amount of heat per weight (or volume) of the given type of fuel
        self.fuelHeatContent = fuelHeatContent

        #: The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed
        self.fuelEffFactor = fuelEffFactor

        #: Relative amount of the given type of fuel, when multiple fuels are being consumed.
        self.fuelMixture = fuelMixture

        #: The active power output level of the unit at which the given type of fuel is switched on. This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high active power output levels.
        self.highBreakpointP = highBreakpointP

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        self._FuelAllocationSchedules = []
        self.FuelAllocationSchedules = [] if FuelAllocationSchedules is None else FuelAllocationSchedules

        super(FossilFuel, self).__init__(*args, **kw_args)

    _attrs = ["fuelSulfur", "fuelCost", "fossilFuelType", "lowBreakpointP", "fuelDispatchCost", "fuelHandlingCost", "fuelHeatContent", "fuelEffFactor", "fuelMixture", "highBreakpointP"]
    _attr_types = {"fuelSulfur": float, "fuelCost": float, "fossilFuelType": str, "lowBreakpointP": float, "fuelDispatchCost": float, "fuelHandlingCost": float, "fuelHeatContent": float, "fuelEffFactor": float, "fuelMixture": float, "highBreakpointP": float}
    _defaults = {"fuelSulfur": 0.0, "fuelCost": 0.0, "fossilFuelType": "oil", "lowBreakpointP": 0.0, "fuelDispatchCost": 0.0, "fuelHandlingCost": 0.0, "fuelHeatContent": 0.0, "fuelEffFactor": 0.0, "fuelMixture": 0.0, "highBreakpointP": 0.0}
    _enums = {"fossilFuelType": "FuelType"}
    _refs = ["ThermalGeneratingUnit", "FuelAllocationSchedules"]
    _many_refs = ["FuelAllocationSchedules"]

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
            if self not in self._ThermalGeneratingUnit._FossilFuels:
                self._ThermalGeneratingUnit._FossilFuels.append(self)

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)

    def getFuelAllocationSchedules(self):
        """A fuel allocation schedule must have a fossil fuel
        """
        return self._FuelAllocationSchedules

    def setFuelAllocationSchedules(self, value):
        for x in self._FuelAllocationSchedules:
            x.FossilFuel = None
        for y in value:
            y._FossilFuel = self
        self._FuelAllocationSchedules = value

    FuelAllocationSchedules = property(getFuelAllocationSchedules, setFuelAllocationSchedules)

    def addFuelAllocationSchedules(self, *FuelAllocationSchedules):
        for obj in FuelAllocationSchedules:
            obj.FossilFuel = self

    def removeFuelAllocationSchedules(self, *FuelAllocationSchedules):
        for obj in FuelAllocationSchedules:
            obj.FossilFuel = None

