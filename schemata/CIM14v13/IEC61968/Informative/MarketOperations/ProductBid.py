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

class ProductBid(IdentifiedObject):
    """Component of a bid that pertains to one market product.
    """

    def __init__(self, Bid=None, MarketProduct=None, BidPriceCurve=None, ProductBidClearing=None, *args, **kw_args):
        """Initializes a new 'ProductBid' instance.

        @param Bid: A bid comprises one or more product bids of market products
        @param MarketProduct:
        @param BidPriceCurve:
        @param ProductBidClearing:
        """
        self._Bid = None
        self.Bid = Bid

        self._MarketProduct = None
        self.MarketProduct = MarketProduct

        self._BidPriceCurve = None
        self.BidPriceCurve = BidPriceCurve

        self._ProductBidClearing = None
        self.ProductBidClearing = ProductBidClearing

        super(ProductBid, self).__init__(*args, **kw_args)

    def getBid(self):
        """A bid comprises one or more product bids of market products
        """
        return self._Bid

    def setBid(self, value):
        if self._Bid is not None:
            filtered = [x for x in self.Bid.ProductBids if x != self]
            self._Bid._ProductBids = filtered

        self._Bid = value
        if self._Bid is not None:
            self._Bid._ProductBids.append(self)

    Bid = property(getBid, setBid)

    def getMarketProduct(self):
        
        return self._MarketProduct

    def setMarketProduct(self, value):
        if self._MarketProduct is not None:
            filtered = [x for x in self.MarketProduct.ProductBids if x != self]
            self._MarketProduct._ProductBids = filtered

        self._MarketProduct = value
        if self._MarketProduct is not None:
            self._MarketProduct._ProductBids.append(self)

    MarketProduct = property(getMarketProduct, setMarketProduct)

    def getBidPriceCurve(self):
        
        return self._BidPriceCurve

    def setBidPriceCurve(self, value):
        if self._BidPriceCurve is not None:
            filtered = [x for x in self.BidPriceCurve.ProductBids if x != self]
            self._BidPriceCurve._ProductBids = filtered

        self._BidPriceCurve = value
        if self._BidPriceCurve is not None:
            self._BidPriceCurve._ProductBids.append(self)

    BidPriceCurve = property(getBidPriceCurve, setBidPriceCurve)

    def getProductBidClearing(self):
        
        return self._ProductBidClearing

    def setProductBidClearing(self, value):
        if self._ProductBidClearing is not None:
            filtered = [x for x in self.ProductBidClearing.ProductBids if x != self]
            self._ProductBidClearing._ProductBids = filtered

        self._ProductBidClearing = value
        if self._ProductBidClearing is not None:
            self._ProductBidClearing._ProductBids.append(self)

    ProductBidClearing = property(getProductBidClearing, setProductBidClearing)

