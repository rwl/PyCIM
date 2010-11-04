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

from CIM14v13.IEC61968.Informative.MarketOperations.ResourceBid import ResourceBid

class LoadBid(ResourceBid):

    def __init__(self, dropRampRate=None, minTimeBetLoadRed=0.0, minLoadReductionCost=0.0, minLoadReductionInterval=0.0, minLoad=0.0, pickUpRampRate=None, reqNoticeTime=0.0, minLoadReduction=0.0, shutdownCost=0.0, LoadReductionPriceCurve=None, RegisteredLoad=None, *args, **kw_args):
        """Initializes a new 'LoadBid' instance.

        @param dropRampRate: Maximum rate that load can be reduced (MW/minute) 
        @param minTimeBetLoadRed: Shortest time that load must be left at normal levels before a new load reduction. 
        @param minLoadReductionCost: Cost in $ at the minimum reduced load 
        @param minLoadReductionInterval: Shortest period load reduction must be maintained before load can be restored to normal levels. 
        @param minLoad: Minimum MW load below which it may not be reduced. 
        @param pickUpRampRate: Maximum rate load may be restored (MW/minute) 
        @param reqNoticeTime: Time period that is required from an order to reduce a load to the time that it takes to get to the minimum load reduction. 
        @param minLoadReduction: Minimum MW for a load reduction (e.g., MW rating of a discrete pump. 
        @param shutdownCost: The fixed cost associated with committing a load reduction. 
        @param LoadReductionPriceCurve:
        @param RegisteredLoad:
        """
        #: Maximum rate that load can be reduced (MW/minute)
        self.dropRampRate = dropRampRate

        #: Shortest time that load must be left at normal levels before a new load reduction.
        self.minTimeBetLoadRed = minTimeBetLoadRed

        #: Cost in $ at the minimum reduced load
        self.minLoadReductionCost = minLoadReductionCost

        #: Shortest period load reduction must be maintained before load can be restored to normal levels.
        self.minLoadReductionInterval = minLoadReductionInterval

        #: Minimum MW load below which it may not be reduced.
        self.minLoad = minLoad

        #: Maximum rate load may be restored (MW/minute)
        self.pickUpRampRate = pickUpRampRate

        #: Time period that is required from an order to reduce a load to the time that it takes to get to the minimum load reduction.
        self.reqNoticeTime = reqNoticeTime

        #: Minimum MW for a load reduction (e.g., MW rating of a discrete pump.
        self.minLoadReduction = minLoadReduction

        #: The fixed cost associated with committing a load reduction.
        self.shutdownCost = shutdownCost

        self._LoadReductionPriceCurve = None
        self.LoadReductionPriceCurve = LoadReductionPriceCurve

        self._RegisteredLoad = None
        self.RegisteredLoad = RegisteredLoad

        super(LoadBid, self).__init__(*args, **kw_args)

    def getLoadReductionPriceCurve(self):
        
        return self._LoadReductionPriceCurve

    def setLoadReductionPriceCurve(self, value):
        if self._LoadReductionPriceCurve is not None:
            filtered = [x for x in self.LoadReductionPriceCurve.LoadBids if x != self]
            self._LoadReductionPriceCurve._LoadBids = filtered

        self._LoadReductionPriceCurve = value
        if self._LoadReductionPriceCurve is not None:
            self._LoadReductionPriceCurve._LoadBids.append(self)

    LoadReductionPriceCurve = property(getLoadReductionPriceCurve, setLoadReductionPriceCurve)

    def getRegisteredLoad(self):
        
        return self._RegisteredLoad

    def setRegisteredLoad(self, value):
        if self._RegisteredLoad is not None:
            filtered = [x for x in self.RegisteredLoad.LoadBids if x != self]
            self._RegisteredLoad._LoadBids = filtered

        self._RegisteredLoad = value
        if self._RegisteredLoad is not None:
            self._RegisteredLoad._LoadBids.append(self)

    RegisteredLoad = property(getRegisteredLoad, setRegisteredLoad)

