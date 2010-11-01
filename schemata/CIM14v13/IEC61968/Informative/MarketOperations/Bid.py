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

from CIM14v13.IEC61968.Common.Document import Document

class Bid(Document):
    """Represents both bids to purchase and offers to sell energy or ancillary services in an RTO-sponsored market.
    """

    def __init__(self, stopTime='', startTime='', marketType='', Market=None, ProductBids=None, BidClearing=None, *args, **kw_args):
        """Initializes a new 'Bid' instance.

        @param stopTime: Stop time and date for which bid is applicable. 
        @param startTime: Start time and date for which bid applies. 
        @param marketType: 
        @param Market:
        @param ProductBids: A bid comprises one or more product bids of market products
        @param BidClearing:
        """
        #: Stop time and date for which bid is applicable. 
        self.stopTime = stopTime

        #: Start time and date for which bid applies. 
        self.startTime = startTime

 
        self.marketType = marketType

        self._Market = None
        self.Market = Market

        self._ProductBids = []
        self.ProductBids = [] if ProductBids is None else ProductBids

        self._BidClearing = None
        self.BidClearing = BidClearing

        super(Bid, self).__init__(*args, **kw_args)

    def getMarket(self):
        
        return self._Market

    def setMarket(self, value):
        if self._Market is not None:
            filtered = [x for x in self.Market.Bids if x != self]
            self._Market._Bids = filtered

        self._Market = value
        if self._Market is not None:
            self._Market._Bids.append(self)

    Market = property(getMarket, setMarket)

    def getProductBids(self):
        """A bid comprises one or more product bids of market products
        """
        return self._ProductBids

    def setProductBids(self, value):
        for x in self._ProductBids:
            x._Bid = None
        for y in value:
            y._Bid = self
        self._ProductBids = value

    ProductBids = property(getProductBids, setProductBids)

    def addProductBids(self, *ProductBids):
        for obj in ProductBids:
            obj._Bid = self
            self._ProductBids.append(obj)

    def removeProductBids(self, *ProductBids):
        for obj in ProductBids:
            obj._Bid = None
            self._ProductBids.remove(obj)

    def getBidClearing(self):
        
        return self._BidClearing

    def setBidClearing(self, value):
        if self._BidClearing is not None:
            self._BidClearing._Bid = None

        self._BidClearing = value
        if self._BidClearing is not None:
            self._BidClearing._Bid = self

    BidClearing = property(getBidClearing, setBidClearing)

