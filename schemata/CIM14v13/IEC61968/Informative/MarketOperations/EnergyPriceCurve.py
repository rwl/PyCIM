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

class EnergyPriceCurve(Curve):
    """Relationship between a price in $/hour (Y-axis) and a MW value (X-axis).
    """

    def __init__(self, EnergyTransactions=None, FTRs=None, **kw_args):
        """Initializes a new 'EnergyPriceCurve' instance.

        @param EnergyTransactions:
        @param FTRs:
        """
        self._EnergyTransactions = []
        self.EnergyTransactions = [] if EnergyTransactions is None else EnergyTransactions

        self._FTRs = []
        self.FTRs = [] if FTRs is None else FTRs

        super(EnergyPriceCurve, self).__init__(**kw_args)

    def getEnergyTransactions(self):
        
        return self._EnergyTransactions

    def setEnergyTransactions(self, value):
        for p in self._EnergyTransactions:
            filtered = [q for q in p.EnergyPriceCurves if q != self]
            self._EnergyTransactions._EnergyPriceCurves = filtered
        for r in value:
            if self not in r._EnergyPriceCurves:
                r._EnergyPriceCurves.append(self)
        self._EnergyTransactions = value

    EnergyTransactions = property(getEnergyTransactions, setEnergyTransactions)

    def addEnergyTransactions(self, *EnergyTransactions):
        for obj in EnergyTransactions:
            if self not in obj._EnergyPriceCurves:
                obj._EnergyPriceCurves.append(self)
            self._EnergyTransactions.append(obj)

    def removeEnergyTransactions(self, *EnergyTransactions):
        for obj in EnergyTransactions:
            if self in obj._EnergyPriceCurves:
                obj._EnergyPriceCurves.remove(self)
            self._EnergyTransactions.remove(obj)

    def getFTRs(self):
        
        return self._FTRs

    def setFTRs(self, value):
        for x in self._FTRs:
            x._EnergyPriceCurve = None
        for y in value:
            y._EnergyPriceCurve = self
        self._FTRs = value

    FTRs = property(getFTRs, setFTRs)

    def addFTRs(self, *FTRs):
        for obj in FTRs:
            obj._EnergyPriceCurve = self
            self._FTRs.append(obj)

    def removeFTRs(self, *FTRs):
        for obj in FTRs:
            obj._EnergyPriceCurve = None
            self._FTRs.remove(obj)

