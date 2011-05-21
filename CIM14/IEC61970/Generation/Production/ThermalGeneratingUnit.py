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

from CIM14.IEC61970.Generation.Production.GeneratingUnit import GeneratingUnit

class ThermalGeneratingUnit(GeneratingUnit):
    """A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.
    """

    def __init__(self, oMCost=0.0, StartupModel=None, EmmissionAccounts=None, CombinedCyclePlant=None, CogenerationPlant=None, EmissionCurves=None, HeatRateCurve=None, ShutdownCurve=None, IncrementalHeatRateCurve=None, FuelAllocationSchedules=None, FossilFuels=None, HeatInputCurve=None, CAESPlant=None, *args, **kw_args):
        """Initialises a new 'ThermalGeneratingUnit' instance.

        @param oMCost: Operating and maintenance cost for the thermal unit 
        @param StartupModel: A thermal generating unit may have a startup model
        @param EmmissionAccounts: A thermal generating unit may have one or more emission allowance accounts
        @param CombinedCyclePlant: A thermal generating unit may be a member of a combined cycle plant
        @param CogenerationPlant: A thermal generating unit may be a member of a cogeneration plant
        @param EmissionCurves: A thermal generating unit may have  one or more emission curves
        @param HeatRateCurve: A thermal generating unit may have a heat rate curve
        @param ShutdownCurve: A thermal generating unit may have a shutdown curve
        @param IncrementalHeatRateCurve: A thermal generating unit may have an incremental heat rate curve
        @param FuelAllocationSchedules: A thermal generating unit may have one or more fuel allocation schedules
        @param FossilFuels: A thermal generating unit may have one or more fossil fuels
        @param HeatInputCurve: A thermal generating unit may have a heat input curve
        @param CAESPlant: A thermal generating unit may be a member of a compressed air energy storage plant
        """
        #: Operating and maintenance cost for the thermal unit
        self.oMCost = oMCost

        self._StartupModel = None
        self.StartupModel = StartupModel

        self._EmmissionAccounts = []
        self.EmmissionAccounts = [] if EmmissionAccounts is None else EmmissionAccounts

        self._CombinedCyclePlant = None
        self.CombinedCyclePlant = CombinedCyclePlant

        self._CogenerationPlant = None
        self.CogenerationPlant = CogenerationPlant

        self._EmissionCurves = []
        self.EmissionCurves = [] if EmissionCurves is None else EmissionCurves

        self._HeatRateCurve = None
        self.HeatRateCurve = HeatRateCurve

        self._ShutdownCurve = None
        self.ShutdownCurve = ShutdownCurve

        self._IncrementalHeatRateCurve = None
        self.IncrementalHeatRateCurve = IncrementalHeatRateCurve

        self._FuelAllocationSchedules = []
        self.FuelAllocationSchedules = [] if FuelAllocationSchedules is None else FuelAllocationSchedules

        self._FossilFuels = []
        self.FossilFuels = [] if FossilFuels is None else FossilFuels

        self._HeatInputCurve = None
        self.HeatInputCurve = HeatInputCurve

        self._CAESPlant = None
        self.CAESPlant = CAESPlant

        super(ThermalGeneratingUnit, self).__init__(*args, **kw_args)

    _attrs = ["oMCost"]
    _attr_types = {"oMCost": float}
    _defaults = {"oMCost": 0.0}
    _enums = {}
    _refs = ["StartupModel", "EmmissionAccounts", "CombinedCyclePlant", "CogenerationPlant", "EmissionCurves", "HeatRateCurve", "ShutdownCurve", "IncrementalHeatRateCurve", "FuelAllocationSchedules", "FossilFuels", "HeatInputCurve", "CAESPlant"]
    _many_refs = ["EmmissionAccounts", "EmissionCurves", "FuelAllocationSchedules", "FossilFuels"]

    def getStartupModel(self):
        """A thermal generating unit may have a startup model
        """
        return self._StartupModel

    def setStartupModel(self, value):
        if self._StartupModel is not None:
            self._StartupModel._ThermalGeneratingUnit = None

        self._StartupModel = value
        if self._StartupModel is not None:
            self._StartupModel.ThermalGeneratingUnit = None
            self._StartupModel._ThermalGeneratingUnit = self

    StartupModel = property(getStartupModel, setStartupModel)

    def getEmmissionAccounts(self):
        """A thermal generating unit may have one or more emission allowance accounts
        """
        return self._EmmissionAccounts

    def setEmmissionAccounts(self, value):
        for x in self._EmmissionAccounts:
            x.ThermalGeneratingUnit = None
        for y in value:
            y._ThermalGeneratingUnit = self
        self._EmmissionAccounts = value

    EmmissionAccounts = property(getEmmissionAccounts, setEmmissionAccounts)

    def addEmmissionAccounts(self, *EmmissionAccounts):
        for obj in EmmissionAccounts:
            obj.ThermalGeneratingUnit = self

    def removeEmmissionAccounts(self, *EmmissionAccounts):
        for obj in EmmissionAccounts:
            obj.ThermalGeneratingUnit = None

    def getCombinedCyclePlant(self):
        """A thermal generating unit may be a member of a combined cycle plant
        """
        return self._CombinedCyclePlant

    def setCombinedCyclePlant(self, value):
        if self._CombinedCyclePlant is not None:
            filtered = [x for x in self.CombinedCyclePlant.ThermalGeneratingUnits if x != self]
            self._CombinedCyclePlant._ThermalGeneratingUnits = filtered

        self._CombinedCyclePlant = value
        if self._CombinedCyclePlant is not None:
            if self not in self._CombinedCyclePlant._ThermalGeneratingUnits:
                self._CombinedCyclePlant._ThermalGeneratingUnits.append(self)

    CombinedCyclePlant = property(getCombinedCyclePlant, setCombinedCyclePlant)

    def getCogenerationPlant(self):
        """A thermal generating unit may be a member of a cogeneration plant
        """
        return self._CogenerationPlant

    def setCogenerationPlant(self, value):
        if self._CogenerationPlant is not None:
            filtered = [x for x in self.CogenerationPlant.ThermalGeneratingUnits if x != self]
            self._CogenerationPlant._ThermalGeneratingUnits = filtered

        self._CogenerationPlant = value
        if self._CogenerationPlant is not None:
            if self not in self._CogenerationPlant._ThermalGeneratingUnits:
                self._CogenerationPlant._ThermalGeneratingUnits.append(self)

    CogenerationPlant = property(getCogenerationPlant, setCogenerationPlant)

    def getEmissionCurves(self):
        """A thermal generating unit may have  one or more emission curves
        """
        return self._EmissionCurves

    def setEmissionCurves(self, value):
        for x in self._EmissionCurves:
            x.ThermalGeneratingUnit = None
        for y in value:
            y._ThermalGeneratingUnit = self
        self._EmissionCurves = value

    EmissionCurves = property(getEmissionCurves, setEmissionCurves)

    def addEmissionCurves(self, *EmissionCurves):
        for obj in EmissionCurves:
            obj.ThermalGeneratingUnit = self

    def removeEmissionCurves(self, *EmissionCurves):
        for obj in EmissionCurves:
            obj.ThermalGeneratingUnit = None

    def getHeatRateCurve(self):
        """A thermal generating unit may have a heat rate curve
        """
        return self._HeatRateCurve

    def setHeatRateCurve(self, value):
        if self._HeatRateCurve is not None:
            self._HeatRateCurve._ThermalGeneratingUnit = None

        self._HeatRateCurve = value
        if self._HeatRateCurve is not None:
            self._HeatRateCurve.ThermalGeneratingUnit = None
            self._HeatRateCurve._ThermalGeneratingUnit = self

    HeatRateCurve = property(getHeatRateCurve, setHeatRateCurve)

    def getShutdownCurve(self):
        """A thermal generating unit may have a shutdown curve
        """
        return self._ShutdownCurve

    def setShutdownCurve(self, value):
        if self._ShutdownCurve is not None:
            self._ShutdownCurve._ThermalGeneratingUnit = None

        self._ShutdownCurve = value
        if self._ShutdownCurve is not None:
            self._ShutdownCurve.ThermalGeneratingUnit = None
            self._ShutdownCurve._ThermalGeneratingUnit = self

    ShutdownCurve = property(getShutdownCurve, setShutdownCurve)

    def getIncrementalHeatRateCurve(self):
        """A thermal generating unit may have an incremental heat rate curve
        """
        return self._IncrementalHeatRateCurve

    def setIncrementalHeatRateCurve(self, value):
        if self._IncrementalHeatRateCurve is not None:
            self._IncrementalHeatRateCurve._ThermalGeneratingUnit = None

        self._IncrementalHeatRateCurve = value
        if self._IncrementalHeatRateCurve is not None:
            self._IncrementalHeatRateCurve.ThermalGeneratingUnit = None
            self._IncrementalHeatRateCurve._ThermalGeneratingUnit = self

    IncrementalHeatRateCurve = property(getIncrementalHeatRateCurve, setIncrementalHeatRateCurve)

    def getFuelAllocationSchedules(self):
        """A thermal generating unit may have one or more fuel allocation schedules
        """
        return self._FuelAllocationSchedules

    def setFuelAllocationSchedules(self, value):
        for x in self._FuelAllocationSchedules:
            x.ThermalGeneratingUnit = None
        for y in value:
            y._ThermalGeneratingUnit = self
        self._FuelAllocationSchedules = value

    FuelAllocationSchedules = property(getFuelAllocationSchedules, setFuelAllocationSchedules)

    def addFuelAllocationSchedules(self, *FuelAllocationSchedules):
        for obj in FuelAllocationSchedules:
            obj.ThermalGeneratingUnit = self

    def removeFuelAllocationSchedules(self, *FuelAllocationSchedules):
        for obj in FuelAllocationSchedules:
            obj.ThermalGeneratingUnit = None

    def getFossilFuels(self):
        """A thermal generating unit may have one or more fossil fuels
        """
        return self._FossilFuels

    def setFossilFuels(self, value):
        for x in self._FossilFuels:
            x.ThermalGeneratingUnit = None
        for y in value:
            y._ThermalGeneratingUnit = self
        self._FossilFuels = value

    FossilFuels = property(getFossilFuels, setFossilFuels)

    def addFossilFuels(self, *FossilFuels):
        for obj in FossilFuels:
            obj.ThermalGeneratingUnit = self

    def removeFossilFuels(self, *FossilFuels):
        for obj in FossilFuels:
            obj.ThermalGeneratingUnit = None

    def getHeatInputCurve(self):
        """A thermal generating unit may have a heat input curve
        """
        return self._HeatInputCurve

    def setHeatInputCurve(self, value):
        if self._HeatInputCurve is not None:
            self._HeatInputCurve._ThermalGeneratingUnit = None

        self._HeatInputCurve = value
        if self._HeatInputCurve is not None:
            self._HeatInputCurve.ThermalGeneratingUnit = None
            self._HeatInputCurve._ThermalGeneratingUnit = self

    HeatInputCurve = property(getHeatInputCurve, setHeatInputCurve)

    def getCAESPlant(self):
        """A thermal generating unit may be a member of a compressed air energy storage plant
        """
        return self._CAESPlant

    def setCAESPlant(self, value):
        if self._CAESPlant is not None:
            self._CAESPlant._ThermalGeneratingUnit = None

        self._CAESPlant = value
        if self._CAESPlant is not None:
            self._CAESPlant.ThermalGeneratingUnit = None
            self._CAESPlant._ThermalGeneratingUnit = self

    CAESPlant = property(getCAESPlant, setCAESPlant)

