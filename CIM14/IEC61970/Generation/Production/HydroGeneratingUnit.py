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

class HydroGeneratingUnit(GeneratingUnit):
    """A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)
    """

    def __init__(self, energyConversionCapability="generator", hydroUnitWaterCost=0.0, HydroPowerPlant=None, PenstockLossCurve=None, HydroGeneratingEfficiencyCurves=None, TailbayLossCurve=None, *args, **kw_args):
        """Initialises a new 'HydroGeneratingUnit' instance.

        @param energyConversionCapability: Energy conversion capability for generating. Values are: "generator", "pumpAndGenerator"
        @param hydroUnitWaterCost: The equivalent cost of water that drives the hydro turbine, expressed as cost per volume. 
        @param HydroPowerPlant: The hydro generating unit belongs to a hydro power plant
        @param PenstockLossCurve: A hydro generating unit has a penstock loss curve
        @param HydroGeneratingEfficiencyCurves: A hydro generating unit has an efficiency curve
        @param TailbayLossCurve: A hydro generating unit has a tailbay loss curve
        """
        #: Energy conversion capability for generating. Values are: "generator", "pumpAndGenerator"
        self.energyConversionCapability = energyConversionCapability

        #: The equivalent cost of water that drives the hydro turbine, expressed as cost per volume.
        self.hydroUnitWaterCost = hydroUnitWaterCost

        self._HydroPowerPlant = None
        self.HydroPowerPlant = HydroPowerPlant

        self._PenstockLossCurve = None
        self.PenstockLossCurve = PenstockLossCurve

        self._HydroGeneratingEfficiencyCurves = []
        self.HydroGeneratingEfficiencyCurves = [] if HydroGeneratingEfficiencyCurves is None else HydroGeneratingEfficiencyCurves

        self._TailbayLossCurve = []
        self.TailbayLossCurve = [] if TailbayLossCurve is None else TailbayLossCurve

        super(HydroGeneratingUnit, self).__init__(*args, **kw_args)

    _attrs = ["energyConversionCapability", "hydroUnitWaterCost"]
    _attr_types = {"energyConversionCapability": str, "hydroUnitWaterCost": float}
    _defaults = {"energyConversionCapability": "generator", "hydroUnitWaterCost": 0.0}
    _enums = {"energyConversionCapability": "HydroEnergyConversionKind"}
    _refs = ["HydroPowerPlant", "PenstockLossCurve", "HydroGeneratingEfficiencyCurves", "TailbayLossCurve"]
    _many_refs = ["HydroGeneratingEfficiencyCurves", "TailbayLossCurve"]

    def getHydroPowerPlant(self):
        """The hydro generating unit belongs to a hydro power plant
        """
        return self._HydroPowerPlant

    def setHydroPowerPlant(self, value):
        if self._HydroPowerPlant is not None:
            filtered = [x for x in self.HydroPowerPlant.HydroGeneratingUnits if x != self]
            self._HydroPowerPlant._HydroGeneratingUnits = filtered

        self._HydroPowerPlant = value
        if self._HydroPowerPlant is not None:
            if self not in self._HydroPowerPlant._HydroGeneratingUnits:
                self._HydroPowerPlant._HydroGeneratingUnits.append(self)

    HydroPowerPlant = property(getHydroPowerPlant, setHydroPowerPlant)

    def getPenstockLossCurve(self):
        """A hydro generating unit has a penstock loss curve
        """
        return self._PenstockLossCurve

    def setPenstockLossCurve(self, value):
        if self._PenstockLossCurve is not None:
            self._PenstockLossCurve._HydroGeneratingUnit = None

        self._PenstockLossCurve = value
        if self._PenstockLossCurve is not None:
            self._PenstockLossCurve.HydroGeneratingUnit = None
            self._PenstockLossCurve._HydroGeneratingUnit = self

    PenstockLossCurve = property(getPenstockLossCurve, setPenstockLossCurve)

    def getHydroGeneratingEfficiencyCurves(self):
        """A hydro generating unit has an efficiency curve
        """
        return self._HydroGeneratingEfficiencyCurves

    def setHydroGeneratingEfficiencyCurves(self, value):
        for x in self._HydroGeneratingEfficiencyCurves:
            x.HydroGeneratingUnit = None
        for y in value:
            y._HydroGeneratingUnit = self
        self._HydroGeneratingEfficiencyCurves = value

    HydroGeneratingEfficiencyCurves = property(getHydroGeneratingEfficiencyCurves, setHydroGeneratingEfficiencyCurves)

    def addHydroGeneratingEfficiencyCurves(self, *HydroGeneratingEfficiencyCurves):
        for obj in HydroGeneratingEfficiencyCurves:
            obj.HydroGeneratingUnit = self

    def removeHydroGeneratingEfficiencyCurves(self, *HydroGeneratingEfficiencyCurves):
        for obj in HydroGeneratingEfficiencyCurves:
            obj.HydroGeneratingUnit = None

    def getTailbayLossCurve(self):
        """A hydro generating unit has a tailbay loss curve
        """
        return self._TailbayLossCurve

    def setTailbayLossCurve(self, value):
        for x in self._TailbayLossCurve:
            x.HydroGeneratingUnit = None
        for y in value:
            y._HydroGeneratingUnit = self
        self._TailbayLossCurve = value

    TailbayLossCurve = property(getTailbayLossCurve, setTailbayLossCurve)

    def addTailbayLossCurve(self, *TailbayLossCurve):
        for obj in TailbayLossCurve:
            obj.HydroGeneratingUnit = self

    def removeTailbayLossCurve(self, *TailbayLossCurve):
        for obj in TailbayLossCurve:
            obj.HydroGeneratingUnit = None

