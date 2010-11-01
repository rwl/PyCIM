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

class StartUpCostCurve(Curve):
    """Startup costs and time as a function of down time.  Relationship between unit startup cost (Y1-axis) and unit startup time (Y2-axis) vs. unit elapsed down time (X-axis).
    """

    def __init__(self, GeneratingBids=None, RegisteredGenerators=None, *args, **kw_args):
        """Initializes a new 'StartUpCostCurve' instance.

        @param GeneratingBids:
        @param RegisteredGenerators:
        """
        self._GeneratingBids = []
        self.GeneratingBids = [] if GeneratingBids is None else GeneratingBids

        self._RegisteredGenerators = []
        self.RegisteredGenerators = [] if RegisteredGenerators is None else RegisteredGenerators

        super(StartUpCostCurve, self).__init__(*args, **kw_args)

    def getGeneratingBids(self):
        
        return self._GeneratingBids

    def setGeneratingBids(self, value):
        for x in self._GeneratingBids:
            x._StartUpCostCurve = None
        for y in value:
            y._StartUpCostCurve = self
        self._GeneratingBids = value

    GeneratingBids = property(getGeneratingBids, setGeneratingBids)

    def addGeneratingBids(self, *GeneratingBids):
        for obj in GeneratingBids:
            obj._StartUpCostCurve = self
            self._GeneratingBids.append(obj)

    def removeGeneratingBids(self, *GeneratingBids):
        for obj in GeneratingBids:
            obj._StartUpCostCurve = None
            self._GeneratingBids.remove(obj)

    def getRegisteredGenerators(self):
        
        return self._RegisteredGenerators

    def setRegisteredGenerators(self, value):
        for p in self._RegisteredGenerators:
            filtered = [q for q in p.StartUpCostCurves if q != self]
            self._RegisteredGenerators._StartUpCostCurves = filtered
        for r in value:
            if self not in r._StartUpCostCurves:
                r._StartUpCostCurves.append(self)
        self._RegisteredGenerators = value

    RegisteredGenerators = property(getRegisteredGenerators, setRegisteredGenerators)

    def addRegisteredGenerators(self, *RegisteredGenerators):
        for obj in RegisteredGenerators:
            if self not in obj._StartUpCostCurves:
                obj._StartUpCostCurves.append(self)
            self._RegisteredGenerators.append(obj)

    def removeRegisteredGenerators(self, *RegisteredGenerators):
        for obj in RegisteredGenerators:
            if self in obj._StartUpCostCurves:
                obj._StartUpCostCurves.remove(self)
            self._RegisteredGenerators.remove(obj)

