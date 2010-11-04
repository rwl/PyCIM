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

from CIM14v13.IEC61968.Informative.MarketOperations.RegisteredResource import RegisteredResource

class RegisteredGenerator(RegisteredResource):

    def __init__(self, lowerRampRate=None, maximumAllowableSpinningReserve=0.0, lowerControlRate=None, raiseControlRate=None, highControlLimit=0.0, maximumOperatingMW=0.0, raiseRampRate=None, spinReserveRamp=None, lowControlLImit=0.0, minimumOperatingMW=0.0, UnitInitialConditions=None, RampRateCurves=None, GeneratingBids=None, StartUpCostCurves=None, GeneratingUnit=None, *args, **kw_args):
        """Initializes a new 'RegisteredGenerator' instance.

        @param lowerRampRate: 
        @param maximumAllowableSpinningReserve: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. 
        @param lowerControlRate: Regulation down response rate in MW per minute 
        @param raiseControlRate: Regulation up response rate in MW per minute 
        @param highControlLimit: High limit for secondary (AGC) control 
        @param maximumOperatingMW: This is the maximum operating MW limit the dispatcher can enter for this unit 
        @param raiseRampRate: 
        @param spinReserveRamp: 
        @param lowControlLImit: Low limit for secondary (AGC) control 
        @param minimumOperatingMW: This is the minimum operating MW limit the dispatcher can enter for this unit. 
        @param UnitInitialConditions:
        @param RampRateCurves:
        @param GeneratingBids:
        @param StartUpCostCurves:
        @param GeneratingUnit:
        """

        self.lowerRampRate = lowerRampRate

        #: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
        self.maximumAllowableSpinningReserve = maximumAllowableSpinningReserve

        #: Regulation down response rate in MW per minute
        self.lowerControlRate = lowerControlRate

        #: Regulation up response rate in MW per minute
        self.raiseControlRate = raiseControlRate

        #: High limit for secondary (AGC) control
        self.highControlLimit = highControlLimit

        #: This is the maximum operating MW limit the dispatcher can enter for this unit
        self.maximumOperatingMW = maximumOperatingMW


        self.raiseRampRate = raiseRampRate


        self.spinReserveRamp = spinReserveRamp

        #: Low limit for secondary (AGC) control
        self.lowControlLImit = lowControlLImit

        #: This is the minimum operating MW limit the dispatcher can enter for this unit.
        self.minimumOperatingMW = minimumOperatingMW

        self._UnitInitialConditions = []
        self.UnitInitialConditions = [] if UnitInitialConditions is None else UnitInitialConditions

        self._RampRateCurves = []
        self.RampRateCurves = [] if RampRateCurves is None else RampRateCurves

        self._GeneratingBids = []
        self.GeneratingBids = [] if GeneratingBids is None else GeneratingBids

        self._StartUpCostCurves = []
        self.StartUpCostCurves = [] if StartUpCostCurves is None else StartUpCostCurves

        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        super(RegisteredGenerator, self).__init__(*args, **kw_args)

    def getUnitInitialConditions(self):
        
        return self._UnitInitialConditions

    def setUnitInitialConditions(self, value):
        for x in self._UnitInitialConditions:
            x._GeneratingUnit = None
        for y in value:
            y._GeneratingUnit = self
        self._UnitInitialConditions = value

    UnitInitialConditions = property(getUnitInitialConditions, setUnitInitialConditions)

    def addUnitInitialConditions(self, *UnitInitialConditions):
        for obj in UnitInitialConditions:
            obj._GeneratingUnit = self
            self._UnitInitialConditions.append(obj)

    def removeUnitInitialConditions(self, *UnitInitialConditions):
        for obj in UnitInitialConditions:
            obj._GeneratingUnit = None
            self._UnitInitialConditions.remove(obj)

    def getRampRateCurves(self):
        
        return self._RampRateCurves

    def setRampRateCurves(self, value):
        for p in self._RampRateCurves:
            filtered = [q for q in p.GeneratingUnit if q != self]
            self._RampRateCurves._GeneratingUnit = filtered
        for r in value:
            if self not in r._GeneratingUnit:
                r._GeneratingUnit.append(self)
        self._RampRateCurves = value

    RampRateCurves = property(getRampRateCurves, setRampRateCurves)

    def addRampRateCurves(self, *RampRateCurves):
        for obj in RampRateCurves:
            if self not in obj._GeneratingUnit:
                obj._GeneratingUnit.append(self)
            self._RampRateCurves.append(obj)

    def removeRampRateCurves(self, *RampRateCurves):
        for obj in RampRateCurves:
            if self in obj._GeneratingUnit:
                obj._GeneratingUnit.remove(self)
            self._RampRateCurves.remove(obj)

    def getGeneratingBids(self):
        
        return self._GeneratingBids

    def setGeneratingBids(self, value):
        for x in self._GeneratingBids:
            x._RegisteredGenerator = None
        for y in value:
            y._RegisteredGenerator = self
        self._GeneratingBids = value

    GeneratingBids = property(getGeneratingBids, setGeneratingBids)

    def addGeneratingBids(self, *GeneratingBids):
        for obj in GeneratingBids:
            obj._RegisteredGenerator = self
            self._GeneratingBids.append(obj)

    def removeGeneratingBids(self, *GeneratingBids):
        for obj in GeneratingBids:
            obj._RegisteredGenerator = None
            self._GeneratingBids.remove(obj)

    def getStartUpCostCurves(self):
        
        return self._StartUpCostCurves

    def setStartUpCostCurves(self, value):
        for p in self._StartUpCostCurves:
            filtered = [q for q in p.RegisteredGenerators if q != self]
            self._StartUpCostCurves._RegisteredGenerators = filtered
        for r in value:
            if self not in r._RegisteredGenerators:
                r._RegisteredGenerators.append(self)
        self._StartUpCostCurves = value

    StartUpCostCurves = property(getStartUpCostCurves, setStartUpCostCurves)

    def addStartUpCostCurves(self, *StartUpCostCurves):
        for obj in StartUpCostCurves:
            if self not in obj._RegisteredGenerators:
                obj._RegisteredGenerators.append(self)
            self._StartUpCostCurves.append(obj)

    def removeStartUpCostCurves(self, *StartUpCostCurves):
        for obj in StartUpCostCurves:
            if self in obj._RegisteredGenerators:
                obj._RegisteredGenerators.remove(self)
            self._StartUpCostCurves.remove(obj)

    def getGeneratingUnit(self):
        
        return self._GeneratingUnit

    def setGeneratingUnit(self, value):
        if self._GeneratingUnit is not None:
            self._GeneratingUnit._RegisteredGenerator = None

        self._GeneratingUnit = value
        if self._GeneratingUnit is not None:
            self._GeneratingUnit._RegisteredGenerator = self

    GeneratingUnit = property(getGeneratingUnit, setGeneratingUnit)

