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

from CIM15.IEC61970.Core.PowerSystemResource import PowerSystemResource

class Reservoir(PowerSystemResource):
    """A water storage facility within a hydro system, including: ponds, lakes, lagoons, and rivers. The storage is usually behind some type of dam.A water storage facility within a hydro system, including: ponds, lakes, lagoons, and rivers. The storage is usually behind some type of dam.
    """

    def __init__(self, spillwayCapacity=0.0, energyStorageRating=0.0, grossCapacity=0.0, riverOutletWorks='', spillwayCrestLevel=0.0, normalMinOperateLevel=0.0, spillwayCrestLength=0.0, spillTravelDelay=0.0, activeStorageCapacity=0.0, spillWayGateType="", fullSupplyLevel=0.0, LevelVsVolumeCurves=None, TargetLevelSchedule=None, HydroPowerPlants=None, UpstreamFromHydroPowerPlants=None, InflowForecasts=None, SpillsFromReservoir=None, SpillsIntoReservoirs=None, *args, **kw_args):
        """Initialises a new 'Reservoir' instance.

        @param spillwayCapacity: The flow capacity of the spillway in cubic meters per second 
        @param energyStorageRating: The reservoir's energy storage rating in energy for given head conditions 
        @param grossCapacity: Total capacity of reservoir 
        @param riverOutletWorks: River outlet works for riparian right releases or other purposes 
        @param spillwayCrestLevel: Spillway crest level above which water will spill 
        @param normalMinOperateLevel: Normal minimum operating level below which the penstocks will draw air 
        @param spillwayCrestLength: The length of the spillway crest 
        @param spillTravelDelay: The spillway water travel delay to the next downstream reservoir 
        @param activeStorageCapacity: Storage volume between the full supply level and the normal minimum operating level 
        @param spillWayGateType: Type of spillway gate, including parameters 
        @param fullSupplyLevel: Full supply level, above which water will spill. This can be the spillway crest level or the top of closed gates. 
        @param LevelVsVolumeCurves: A reservoir may have a level versus volume relationship.
        @param TargetLevelSchedule: A reservoir may have a water level target schedule.
        @param HydroPowerPlants: Generators discharge water to or pumps are supplied water from a downstream reservoir
        @param UpstreamFromHydroPowerPlants: Generators are supplied water from or pumps discharge water to an upstream reservoir
        @param InflowForecasts: A reservoir may have a 'natural' inflow forecast.
        @param SpillsFromReservoir: A reservoir may spill into a downstream reservoir
        @param SpillsIntoReservoirs: A reservoir may spill into a downstream reservoir
        """
        #: The flow capacity of the spillway in cubic meters per second
        self.spillwayCapacity = spillwayCapacity

        #: The reservoir's energy storage rating in energy for given head conditions
        self.energyStorageRating = energyStorageRating

        #: Total capacity of reservoir
        self.grossCapacity = grossCapacity

        #: River outlet works for riparian right releases or other purposes
        self.riverOutletWorks = riverOutletWorks

        #: Spillway crest level above which water will spill
        self.spillwayCrestLevel = spillwayCrestLevel

        #: Normal minimum operating level below which the penstocks will draw air
        self.normalMinOperateLevel = normalMinOperateLevel

        #: The length of the spillway crest
        self.spillwayCrestLength = spillwayCrestLength

        #: The spillway water travel delay to the next downstream reservoir
        self.spillTravelDelay = spillTravelDelay

        #: Storage volume between the full supply level and the normal minimum operating level
        self.activeStorageCapacity = activeStorageCapacity

        #: Type of spillway gate, including parameters
        self.spillWayGateType = spillWayGateType

        #: Full supply level, above which water will spill. This can be the spillway crest level or the top of closed gates.
        self.fullSupplyLevel = fullSupplyLevel

        self._LevelVsVolumeCurves = []
        self.LevelVsVolumeCurves = [] if LevelVsVolumeCurves is None else LevelVsVolumeCurves

        self._TargetLevelSchedule = None
        self.TargetLevelSchedule = TargetLevelSchedule

        self._HydroPowerPlants = []
        self.HydroPowerPlants = [] if HydroPowerPlants is None else HydroPowerPlants

        self._UpstreamFromHydroPowerPlants = []
        self.UpstreamFromHydroPowerPlants = [] if UpstreamFromHydroPowerPlants is None else UpstreamFromHydroPowerPlants

        self._InflowForecasts = []
        self.InflowForecasts = [] if InflowForecasts is None else InflowForecasts

        self._SpillsFromReservoir = None
        self.SpillsFromReservoir = SpillsFromReservoir

        self._SpillsIntoReservoirs = []
        self.SpillsIntoReservoirs = [] if SpillsIntoReservoirs is None else SpillsIntoReservoirs

        super(Reservoir, self).__init__(*args, **kw_args)

    _attrs = ["spillwayCapacity", "energyStorageRating", "grossCapacity", "riverOutletWorks", "spillwayCrestLevel", "normalMinOperateLevel", "spillwayCrestLength", "spillTravelDelay", "activeStorageCapacity", "spillWayGateType", "fullSupplyLevel"]
    _attr_types = {"spillwayCapacity": float, "energyStorageRating": float, "grossCapacity": float, "riverOutletWorks": str, "spillwayCrestLevel": float, "normalMinOperateLevel": float, "spillwayCrestLength": float, "spillTravelDelay": float, "activeStorageCapacity": float, "spillWayGateType": str, "fullSupplyLevel": float}
    _defaults = {"spillwayCapacity": 0.0, "energyStorageRating": 0.0, "grossCapacity": 0.0, "riverOutletWorks": '', "spillwayCrestLevel": 0.0, "normalMinOperateLevel": 0.0, "spillwayCrestLength": 0.0, "spillTravelDelay": 0.0, "activeStorageCapacity": 0.0, "spillWayGateType": "", "fullSupplyLevel": 0.0}
    _enums = {"spillWayGateType": "SpillwayGateType"}
    _refs = ["LevelVsVolumeCurves", "TargetLevelSchedule", "HydroPowerPlants", "UpstreamFromHydroPowerPlants", "InflowForecasts", "SpillsFromReservoir", "SpillsIntoReservoirs"]
    _many_refs = ["LevelVsVolumeCurves", "HydroPowerPlants", "UpstreamFromHydroPowerPlants", "InflowForecasts", "SpillsIntoReservoirs"]

    def getLevelVsVolumeCurves(self):
        """A reservoir may have a level versus volume relationship.
        """
        return self._LevelVsVolumeCurves

    def setLevelVsVolumeCurves(self, value):
        for x in self._LevelVsVolumeCurves:
            x.Reservoir = None
        for y in value:
            y._Reservoir = self
        self._LevelVsVolumeCurves = value

    LevelVsVolumeCurves = property(getLevelVsVolumeCurves, setLevelVsVolumeCurves)

    def addLevelVsVolumeCurves(self, *LevelVsVolumeCurves):
        for obj in LevelVsVolumeCurves:
            obj.Reservoir = self

    def removeLevelVsVolumeCurves(self, *LevelVsVolumeCurves):
        for obj in LevelVsVolumeCurves:
            obj.Reservoir = None

    def getTargetLevelSchedule(self):
        """A reservoir may have a water level target schedule.
        """
        return self._TargetLevelSchedule

    def setTargetLevelSchedule(self, value):
        if self._TargetLevelSchedule is not None:
            self._TargetLevelSchedule._Reservoir = None

        self._TargetLevelSchedule = value
        if self._TargetLevelSchedule is not None:
            self._TargetLevelSchedule.Reservoir = None
            self._TargetLevelSchedule._Reservoir = self

    TargetLevelSchedule = property(getTargetLevelSchedule, setTargetLevelSchedule)

    def getHydroPowerPlants(self):
        """Generators discharge water to or pumps are supplied water from a downstream reservoir
        """
        return self._HydroPowerPlants

    def setHydroPowerPlants(self, value):
        for x in self._HydroPowerPlants:
            x.Reservoir = None
        for y in value:
            y._Reservoir = self
        self._HydroPowerPlants = value

    HydroPowerPlants = property(getHydroPowerPlants, setHydroPowerPlants)

    def addHydroPowerPlants(self, *HydroPowerPlants):
        for obj in HydroPowerPlants:
            obj.Reservoir = self

    def removeHydroPowerPlants(self, *HydroPowerPlants):
        for obj in HydroPowerPlants:
            obj.Reservoir = None

    def getUpstreamFromHydroPowerPlants(self):
        """Generators are supplied water from or pumps discharge water to an upstream reservoir
        """
        return self._UpstreamFromHydroPowerPlants

    def setUpstreamFromHydroPowerPlants(self, value):
        for x in self._UpstreamFromHydroPowerPlants:
            x.GenSourcePumpDischargeReservoir = None
        for y in value:
            y._GenSourcePumpDischargeReservoir = self
        self._UpstreamFromHydroPowerPlants = value

    UpstreamFromHydroPowerPlants = property(getUpstreamFromHydroPowerPlants, setUpstreamFromHydroPowerPlants)

    def addUpstreamFromHydroPowerPlants(self, *UpstreamFromHydroPowerPlants):
        for obj in UpstreamFromHydroPowerPlants:
            obj.GenSourcePumpDischargeReservoir = self

    def removeUpstreamFromHydroPowerPlants(self, *UpstreamFromHydroPowerPlants):
        for obj in UpstreamFromHydroPowerPlants:
            obj.GenSourcePumpDischargeReservoir = None

    def getInflowForecasts(self):
        """A reservoir may have a 'natural' inflow forecast.
        """
        return self._InflowForecasts

    def setInflowForecasts(self, value):
        for x in self._InflowForecasts:
            x.Reservoir = None
        for y in value:
            y._Reservoir = self
        self._InflowForecasts = value

    InflowForecasts = property(getInflowForecasts, setInflowForecasts)

    def addInflowForecasts(self, *InflowForecasts):
        for obj in InflowForecasts:
            obj.Reservoir = self

    def removeInflowForecasts(self, *InflowForecasts):
        for obj in InflowForecasts:
            obj.Reservoir = None

    def getSpillsFromReservoir(self):
        """A reservoir may spill into a downstream reservoir
        """
        return self._SpillsFromReservoir

    def setSpillsFromReservoir(self, value):
        if self._SpillsFromReservoir is not None:
            filtered = [x for x in self.SpillsFromReservoir.SpillsIntoReservoirs if x != self]
            self._SpillsFromReservoir._SpillsIntoReservoirs = filtered

        self._SpillsFromReservoir = value
        if self._SpillsFromReservoir is not None:
            if self not in self._SpillsFromReservoir._SpillsIntoReservoirs:
                self._SpillsFromReservoir._SpillsIntoReservoirs.append(self)

    SpillsFromReservoir = property(getSpillsFromReservoir, setSpillsFromReservoir)

    def getSpillsIntoReservoirs(self):
        """A reservoir may spill into a downstream reservoir
        """
        return self._SpillsIntoReservoirs

    def setSpillsIntoReservoirs(self, value):
        for x in self._SpillsIntoReservoirs:
            x.SpillsFromReservoir = None
        for y in value:
            y._SpillsFromReservoir = self
        self._SpillsIntoReservoirs = value

    SpillsIntoReservoirs = property(getSpillsIntoReservoirs, setSpillsIntoReservoirs)

    def addSpillsIntoReservoirs(self, *SpillsIntoReservoirs):
        for obj in SpillsIntoReservoirs:
            obj.SpillsFromReservoir = self

    def removeSpillsIntoReservoirs(self, *SpillsIntoReservoirs):
        for obj in SpillsIntoReservoirs:
            obj.SpillsFromReservoir = None

