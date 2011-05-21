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

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class HydroPowerPlant(PowerSystemResource):
    """A hydro power station which can generate or pump. When generating, the generator turbines receive there water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.
    """

    def __init__(self, hydroPlantType="runOfRiver", penstockType="", surgeTankCode="", plantRatedHead=0.0, plantDischargeCapacity=0.0, surgeTankCrestLevel=0.0, dischargeTravelDelay=0.0, pumpRatedP=0.0, genRatedP=0.0, HydroGeneratingUnits=None, HydroPumps=None, Reservoir=None, GenSourcePumpDischargeReservoir=None, *args, **kw_args):
        """Initialises a new 'HydroPowerPlant' instance.

        @param hydroPlantType: The type of hydro power plant. Values are: "runOfRiver", "minorStorage", "majorStorage", "pumpedStorage"
        @param penstockType: Type and configuration of hydro plant penstock(s) 
        @param surgeTankCode: A code describing the type (or absence) of surge tank that is associated with the hydro power plant 
        @param plantRatedHead: The plant's rated gross head 
        @param plantDischargeCapacity: Total plant discharge capacity in cubic meters per second 
        @param surgeTankCrestLevel: The level at which the surge tank spills 
        @param dischargeTravelDelay: Water travel delay from tailbay to next downstream hydro power station 
        @param pumpRatedP: The hydro plant's pumping rating active power for rated head conditions 
        @param genRatedP: The hydro plant's generating rating active power for rated head conditions 
        @param HydroGeneratingUnits: The hydro generating unit belongs to a hydro power plant
        @param HydroPumps: The hydro pump may be a member of a pumped storage plant or a pump for distributing water
        @param Reservoir: Generators discharge water to or pumps are supplied water from a downstream reservoir
        @param GenSourcePumpDischargeReservoir: Generators are supplied water from or pumps discharge water to an upstream reservoir
        """
        #: The type of hydro power plant. Values are: "runOfRiver", "minorStorage", "majorStorage", "pumpedStorage"
        self.hydroPlantType = hydroPlantType

        #: Type and configuration of hydro plant penstock(s)
        self.penstockType = penstockType

        #: A code describing the type (or absence) of surge tank that is associated with the hydro power plant
        self.surgeTankCode = surgeTankCode

        #: The plant's rated gross head
        self.plantRatedHead = plantRatedHead

        #: Total plant discharge capacity in cubic meters per second
        self.plantDischargeCapacity = plantDischargeCapacity

        #: The level at which the surge tank spills
        self.surgeTankCrestLevel = surgeTankCrestLevel

        #: Water travel delay from tailbay to next downstream hydro power station
        self.dischargeTravelDelay = dischargeTravelDelay

        #: The hydro plant's pumping rating active power for rated head conditions
        self.pumpRatedP = pumpRatedP

        #: The hydro plant's generating rating active power for rated head conditions
        self.genRatedP = genRatedP

        self._HydroGeneratingUnits = []
        self.HydroGeneratingUnits = [] if HydroGeneratingUnits is None else HydroGeneratingUnits

        self._HydroPumps = []
        self.HydroPumps = [] if HydroPumps is None else HydroPumps

        self._Reservoir = None
        self.Reservoir = Reservoir

        self._GenSourcePumpDischargeReservoir = None
        self.GenSourcePumpDischargeReservoir = GenSourcePumpDischargeReservoir

        super(HydroPowerPlant, self).__init__(*args, **kw_args)

    _attrs = ["hydroPlantType", "penstockType", "surgeTankCode", "plantRatedHead", "plantDischargeCapacity", "surgeTankCrestLevel", "dischargeTravelDelay", "pumpRatedP", "genRatedP"]
    _attr_types = {"hydroPlantType": str, "penstockType": str, "surgeTankCode": str, "plantRatedHead": float, "plantDischargeCapacity": float, "surgeTankCrestLevel": float, "dischargeTravelDelay": float, "pumpRatedP": float, "genRatedP": float}
    _defaults = {"hydroPlantType": "runOfRiver", "penstockType": "", "surgeTankCode": "", "plantRatedHead": 0.0, "plantDischargeCapacity": 0.0, "surgeTankCrestLevel": 0.0, "dischargeTravelDelay": 0.0, "pumpRatedP": 0.0, "genRatedP": 0.0}
    _enums = {"hydroPlantType": "HydroPlantType", "penstockType": "PenstockType", "surgeTankCode": "SurgeTankCode"}
    _refs = ["HydroGeneratingUnits", "HydroPumps", "Reservoir", "GenSourcePumpDischargeReservoir"]
    _many_refs = ["HydroGeneratingUnits", "HydroPumps"]

    def getHydroGeneratingUnits(self):
        """The hydro generating unit belongs to a hydro power plant
        """
        return self._HydroGeneratingUnits

    def setHydroGeneratingUnits(self, value):
        for x in self._HydroGeneratingUnits:
            x.HydroPowerPlant = None
        for y in value:
            y._HydroPowerPlant = self
        self._HydroGeneratingUnits = value

    HydroGeneratingUnits = property(getHydroGeneratingUnits, setHydroGeneratingUnits)

    def addHydroGeneratingUnits(self, *HydroGeneratingUnits):
        for obj in HydroGeneratingUnits:
            obj.HydroPowerPlant = self

    def removeHydroGeneratingUnits(self, *HydroGeneratingUnits):
        for obj in HydroGeneratingUnits:
            obj.HydroPowerPlant = None

    def getHydroPumps(self):
        """The hydro pump may be a member of a pumped storage plant or a pump for distributing water
        """
        return self._HydroPumps

    def setHydroPumps(self, value):
        for x in self._HydroPumps:
            x.HydroPowerPlant = None
        for y in value:
            y._HydroPowerPlant = self
        self._HydroPumps = value

    HydroPumps = property(getHydroPumps, setHydroPumps)

    def addHydroPumps(self, *HydroPumps):
        for obj in HydroPumps:
            obj.HydroPowerPlant = self

    def removeHydroPumps(self, *HydroPumps):
        for obj in HydroPumps:
            obj.HydroPowerPlant = None

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
            if self not in self._Reservoir._HydroPowerPlants:
                self._Reservoir._HydroPowerPlants.append(self)

    Reservoir = property(getReservoir, setReservoir)

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
            if self not in self._GenSourcePumpDischargeReservoir._UpstreamFromHydroPowerPlants:
                self._GenSourcePumpDischargeReservoir._UpstreamFromHydroPowerPlants.append(self)

    GenSourcePumpDischargeReservoir = property(getGenSourcePumpDischargeReservoir, setGenSourcePumpDischargeReservoir)

