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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Market(IdentifiedObject):
    """Market (e.g., DAM, HAM)  zzMarket operation control parameters.
    """

    def __init__(self, rampIntervalNonSpinRes=0.0, localTimeZone='', rampIntervalEnergy=0.0, type='', timeIntervalLength=0.0, rampIntervalSpinRes=0.0, dst=False, rampIntervalReg=0.0, end='', start='', Bids=None, MarketProducts=None, RegisteredResources=None, Settlements=None, MarketFactors=None, RTO=None, **kw_args):
        """Initializes a new 'Market' instance.

        @param rampIntervalNonSpinRes: Ramping time interval for non-spinning reserve. 
        @param localTimeZone: Local time zone. 
        @param rampIntervalEnergy: Ramping time interval for energy. 
        @param type: The type of a market. 
        @param timeIntervalLength: Trading time interval length. 
        @param rampIntervalSpinRes: Ramping time interval for spinning reserve. 
        @param dst: True if daylight savings time (DST) is in effect. 
        @param rampIntervalReg: Ramping time interval for regulation. 
        @param end: Market end time. 
        @param start: Market start time. 
        @param Bids:
        @param MarketProducts:
        @param RegisteredResources:
        @param Settlements:
        @param MarketFactors:
        @param RTO:
        """
        #: Ramping time interval for non-spinning reserve.
        self.rampIntervalNonSpinRes = rampIntervalNonSpinRes

        #: Local time zone.
        self.localTimeZone = localTimeZone

        #: Ramping time interval for energy.
        self.rampIntervalEnergy = rampIntervalEnergy

        #: The type of a market.
        self.type = type

        #: Trading time interval length.
        self.timeIntervalLength = timeIntervalLength

        #: Ramping time interval for spinning reserve.
        self.rampIntervalSpinRes = rampIntervalSpinRes

        #: True if daylight savings time (DST) is in effect.
        self.dst = dst

        #: Ramping time interval for regulation.
        self.rampIntervalReg = rampIntervalReg

        #: Market end time.
        self.end = end

        #: Market start time.
        self.start = start

        self._Bids = []
        self.Bids = [] if Bids is None else Bids

        self._MarketProducts = []
        self.MarketProducts = [] if MarketProducts is None else MarketProducts

        self._RegisteredResources = []
        self.RegisteredResources = [] if RegisteredResources is None else RegisteredResources

        self._Settlements = []
        self.Settlements = [] if Settlements is None else Settlements

        self._MarketFactors = []
        self.MarketFactors = [] if MarketFactors is None else MarketFactors

        self._RTO = None
        self.RTO = RTO

        super(Market, self).__init__(**kw_args)

    def getBids(self):
        
        return self._Bids

    def setBids(self, value):
        for x in self._Bids:
            x._Market = None
        for y in value:
            y._Market = self
        self._Bids = value

    Bids = property(getBids, setBids)

    def addBids(self, *Bids):
        for obj in Bids:
            obj._Market = self
            self._Bids.append(obj)

    def removeBids(self, *Bids):
        for obj in Bids:
            obj._Market = None
            self._Bids.remove(obj)

    def getMarketProducts(self):
        
        return self._MarketProducts

    def setMarketProducts(self, value):
        for x in self._MarketProducts:
            x._Market = None
        for y in value:
            y._Market = self
        self._MarketProducts = value

    MarketProducts = property(getMarketProducts, setMarketProducts)

    def addMarketProducts(self, *MarketProducts):
        for obj in MarketProducts:
            obj._Market = self
            self._MarketProducts.append(obj)

    def removeMarketProducts(self, *MarketProducts):
        for obj in MarketProducts:
            obj._Market = None
            self._MarketProducts.remove(obj)

    def getRegisteredResources(self):
        
        return self._RegisteredResources

    def setRegisteredResources(self, value):
        for p in self._RegisteredResources:
            filtered = [q for q in p.Markets if q != self]
            self._RegisteredResources._Markets = filtered
        for r in value:
            if self not in r._Markets:
                r._Markets.append(self)
        self._RegisteredResources = value

    RegisteredResources = property(getRegisteredResources, setRegisteredResources)

    def addRegisteredResources(self, *RegisteredResources):
        for obj in RegisteredResources:
            if self not in obj._Markets:
                obj._Markets.append(self)
            self._RegisteredResources.append(obj)

    def removeRegisteredResources(self, *RegisteredResources):
        for obj in RegisteredResources:
            if self in obj._Markets:
                obj._Markets.remove(self)
            self._RegisteredResources.remove(obj)

    def getSettlements(self):
        
        return self._Settlements

    def setSettlements(self, value):
        for x in self._Settlements:
            x._Market = None
        for y in value:
            y._Market = self
        self._Settlements = value

    Settlements = property(getSettlements, setSettlements)

    def addSettlements(self, *Settlements):
        for obj in Settlements:
            obj._Market = self
            self._Settlements.append(obj)

    def removeSettlements(self, *Settlements):
        for obj in Settlements:
            obj._Market = None
            self._Settlements.remove(obj)

    def getMarketFactors(self):
        
        return self._MarketFactors

    def setMarketFactors(self, value):
        for x in self._MarketFactors:
            x._Market = None
        for y in value:
            y._Market = self
        self._MarketFactors = value

    MarketFactors = property(getMarketFactors, setMarketFactors)

    def addMarketFactors(self, *MarketFactors):
        for obj in MarketFactors:
            obj._Market = self
            self._MarketFactors.append(obj)

    def removeMarketFactors(self, *MarketFactors):
        for obj in MarketFactors:
            obj._Market = None
            self._MarketFactors.remove(obj)

    def getRTO(self):
        
        return self._RTO

    def setRTO(self, value):
        if self._RTO is not None:
            filtered = [x for x in self.RTO.Markets if x != self]
            self._RTO._Markets = filtered

        self._RTO = value
        if self._RTO is not None:
            self._RTO._Markets.append(self)

    RTO = property(getRTO, setRTO)

