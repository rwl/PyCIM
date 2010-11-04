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

from CIM14v13.IEC61970.Core.PowerSystemResource import PowerSystemResource

class HydroPowerPlant(PowerSystemResource):
    """A hydro power station which can generate or pump. When generating, the generator turbines receive there water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.
    """

    def __init__(self, hydroPlantType='majorStorage', surgeTankCode='', penstockType='', pumpRatedP=0.0, genRatedP=0.0, plantDischargeCapacity=0.0, dischargeTravelDelay=0.0, plantRatedHead=0.0, surgeTankCrestLevel=0.0, GenSourcePumpDischargeReservoir=None, HydroPumps=None, HydroGeneratingUnits=None, Reservoir=None, *args, **kw_args):
        """Initializes a new 'HydroPowerPlant' instance.

        @param hydroPlantType: The type of hydro power plant. Values are: "majorStorage", "runOfRiver", "minorStorage", "pumpedStorage"
        @param surgeTankCode: A code describing the type (or absence) of surge tank that is associated with the hydro power plant 
        @param penstockType: Type and configuration of hydro plant penstock(s) 
        @param pumpRatedP: The hydro plant's pumping rating active power for rated head conditions 
        @param genRatedP: The hydro plant's generating rating active power for rated head conditions 
        @param plantDischargeCapacity: Total plant discharge capacity in cubic meters per second 
        @param dischargeTravelDelay: Water travel delay from tailbay to next downstream hydro power station 
        @param plantRatedHead: The plant's rated gross head 
        @param surgeTankCrestLevel: The level at which the surge tank spills 
        @param GenSourcePumpDischargeReservoir: Generators are supplied water from or pumps discharge water to an upstream reservoir
        @param HydroPumps: The hydro pump may be a member of a pumped storage plant or a pump for distributing water
        @param HydroGeneratingUnits: The hydro generating unit belongs to a hydro power plant
        @param Reservoir: Generators discharge water to or pumps are supplied water from a downstream reservoir
        """
        #: The type of hydro power plant.Values are: "majorStorage", "runOfRiver", "minorStorage", "pumpedStorage"
        self.hydroPlantType = hydroPlantType

        #: A code describing the type (or absence) of surge tank that is associated with the hydro power plant
        self.surgeTankCode = surgeTankCode

        #: Type and configuration of hydro plant penstock(s)
        self.penstockType = penstockType

        #: The hydro plant's pumping rating active power for rated head conditions
        self.pumpRatedP = pumpRatedP

        #: The hydro plant's generating rating active power for rated head conditions
        self.genRatedP = genRatedP

        #: Total plant discharge capacity in cubic meters per second
        self.plantDischargeCapacity = plantDischargeCapacity

        #: Water travel delay from tailbay to next downstream hydro power station
        self.dischargeTravelDelay = dischargeTravelDelay

        #: The plant's rated gross head
        self.plantRatedHead = plantRatedHead

        #: The level at which the surge tank spills
        self.surgeTankCrestLevel = surgeTankCrestLevel

        self._GenSourcePumpDischargeReservoir = None
        self.GenSourcePumpDischargeReservoir = GenSourcePumpDischargeReservoir

        self._HydroPumps = []
        self.HydroPumps = [] if HydroPumps is None else HydroPumps

        self._HydroGeneratingUnits = []
        self.HydroGeneratingUnits = [] if HydroGeneratingUnits is None else HydroGeneratingUnits

        self._Reservoir = None
        self.Reservoir = Reservoir

        super(HydroPowerPlant, self).__init__(*args, **kw_args)

    def getGenSourcePumpDischargeReservoir(self):
        """Generators are supplied water from or pumps discharge water to an upstream reservoir
        """
        return self._GenSourcePumpDischargeReservoir

    def setGenSourcePumpDischargeReservoir(self, value):
        if self._GenSourcePumpDischargeReservoir is not None:
            filtered = [x for x in self.GenSourcePumpDischargeReservoir.UpstreamFromHydroPowerPlants if x != self]
            self._GenSourcePumpDischargeReservoir._UpstreamFromHydroPowerPlants = filtered

        self._GenSourcePumpDischargeReservoir = value
        if self._GenSourcePumpDischargeReservoir is not None:
            self._GenSourcePumpDischargeReservoir._UpstreamFromHydroPowerPlants.append(self)

    GenSourcePumpDischargeReservoir = property(getGenSourcePumpDischargeReservoir, setGenSourcePumpDischargeReservoir)

    def getHydroPumps(self):
        """The hydro pump may be a member of a pumped storage plant or a pump for distributing water
        """
        return self._HydroPumps

    def setHydroPumps(self, value):
        for x in self._HydroPumps:
            x._HydroPowerPlant = None
        for y in value:
            y._HydroPowerPlant = self
        self._HydroPumps = value

    HydroPumps = property(getHydroPumps, setHydroPumps)

    def addHydroPumps(self, *HydroPumps):
        for obj in HydroPumps:
            obj._HydroPowerPlant = self
            self._HydroPumps.append(obj)

    def removeHydroPumps(self, *HydroPumps):
        for obj in HydroPumps:
            obj._HydroPowerPlant = None
            self._HydroPumps.remove(obj)

    def getHydroGeneratingUnits(self):
        """The hydro generating unit belongs to a hydro power plant
        """
        return self._HydroGeneratingUnits

    def setHydroGeneratingUnits(self, value):
        for x in self._HydroGeneratingUnits:
            x._HydroPowerPlant = None
        for y in value:
            y._HydroPowerPlant = self
        self._HydroGeneratingUnits = value

    HydroGeneratingUnits = property(getHydroGeneratingUnits, setHydroGeneratingUnits)

    def addHydroGeneratingUnits(self, *HydroGeneratingUnits):
        for obj in HydroGeneratingUnits:
            obj._HydroPowerPlant = self
            self._HydroGeneratingUnits.append(obj)

    def removeHydroGeneratingUnits(self, *HydroGeneratingUnits):
        for obj in HydroGeneratingUnits:
            obj._HydroPowerPlant = None
            self._HydroGeneratingUnits.remove(obj)

    def getReservoir(self):
        """Generators discharge water to or pumps are supplied water from a downstream reservoir
        """
        return self._Reservoir

    def setReservoir(self, value):
        if self._Reservoir is not None:
            filtered = [x for x in self.Reservoir.HydroPowerPlants if x != self]
            self._Reservoir._HydroPowerPlants = filtered

        self._Reservoir = value
        if self._Reservoir is not None:
            self._Reservoir._HydroPowerPlants.append(self)

    Reservoir = property(getReservoir, setReservoir)

