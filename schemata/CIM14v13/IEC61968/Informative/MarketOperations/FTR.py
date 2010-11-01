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

from CIM14v13.IEC61968.Common.Agreement import Agreement

class FTR(Agreement):
    """Financial Transmission Rights (FTR) regarding transmission capacity at a flowgate.
    """

    def __init__(self, action='', klass='', baseEnergy=0.0, optimized='', ftrType='', Pnodes=None, EnergyPriceCurve=None, Flowgate=None, *args, **kw_args):
        """Initializes a new 'FTR' instance.

        @param action: Buy, Sell
        @param class: Peak, Off-peak, 24-hour
        @param baseEnergy: Quantity, typically MWs - Seller owns all rights being offered, MWs over time on same Point of Receipt, Point of Delivery, or Resource.
        @param optimized: Fixed (covers re-configuration, grandfathering) or Optimized (up for sale/purchase
        @param ftrType: Type of rights being offered (product) allowed to be auctioned (option, obligation).
        @param Pnodes:
        @param EnergyPriceCurve:
        @param Flowgate:
        """
        #: Buy, Sell
        self.action = action

        #: Peak, Off-peak, 24-hour
        self.klass = klass

        #: Quantity, typically MWs - Seller owns all rights being offered, MWs over time on same Point of Receipt, Point of Delivery, or Resource.
        self.baseEnergy = baseEnergy

        #: Fixed (covers re-configuration, grandfathering) or Optimized (up for sale/purchase
        self.optimized = optimized

        #: Type of rights being offered (product) allowed to be auctioned (option, obligation).
        self.ftrType = ftrType

        self._Pnodes = []
        self.Pnodes = [] if Pnodes is None else Pnodes

        self._EnergyPriceCurve = None
        self.EnergyPriceCurve = EnergyPriceCurve

        self._Flowgate = None
        self.Flowgate = Flowgate

        super(FTR, self).__init__(*args, **kw_args)

    def getPnodes(self):

        return self._Pnodes

    def setPnodes(self, value):
        for p in self._Pnodes:
            filtered = [q for q in p.FTRs if q != self]
            self._Pnodes._FTRs = filtered
        for r in value:
            if self not in r._FTRs:
                r._FTRs.append(self)
        self._Pnodes = value

    Pnodes = property(getPnodes, setPnodes)

    def addPnodes(self, *Pnodes):
        for obj in Pnodes:
            if self not in obj._FTRs:
                obj._FTRs.append(self)
            self._Pnodes.append(obj)

    def removePnodes(self, *Pnodes):
        for obj in Pnodes:
            if self in obj._FTRs:
                obj._FTRs.remove(self)
            self._Pnodes.remove(obj)

    def getEnergyPriceCurve(self):

        return self._EnergyPriceCurve

    def setEnergyPriceCurve(self, value):
        if self._EnergyPriceCurve is not None:
            filtered = [x for x in self.EnergyPriceCurve.FTRs if x != self]
            self._EnergyPriceCurve._FTRs = filtered

        self._EnergyPriceCurve = value
        if self._EnergyPriceCurve is not None:
            self._EnergyPriceCurve._FTRs.append(self)

    EnergyPriceCurve = property(getEnergyPriceCurve, setEnergyPriceCurve)

    def getFlowgate(self):

        return self._Flowgate

    def setFlowgate(self, value):
        if self._Flowgate is not None:
            filtered = [x for x in self.Flowgate.FTRs if x != self]
            self._Flowgate._FTRs = filtered

        self._Flowgate = value
        if self._Flowgate is not None:
            self._Flowgate._FTRs.append(self)

    Flowgate = property(getFlowgate, setFlowgate)

