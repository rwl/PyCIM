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

class MarketProduct(IdentifiedObject):
    """A product traded by an RTO (e.g., energy, 10 minute spinning reserve).  Ancillary service product examples include: Regulation Up Regulation Dn Spinning Reserve Non-Spinning Reserve Operating Reserve
    """

    def __init__(self, Market=None, RegisteredResources=None, ReserveReqs=None, ProductBids=None, **kw_args):
        """Initializes a new 'MarketProduct' instance.

        @param Market:
        @param RegisteredResources: A registered resource is eligible to bid market products
        @param ReserveReqs: Market product associated with reserve requirement must be a reserve or regulation product.
        @param ProductBids:
        """
        self._Market = None
        self.Market = Market

        self._RegisteredResources = []
        self.RegisteredResources = [] if RegisteredResources is None else RegisteredResources

        self._ReserveReqs = []
        self.ReserveReqs = [] if ReserveReqs is None else ReserveReqs

        self._ProductBids = []
        self.ProductBids = [] if ProductBids is None else ProductBids

        super(MarketProduct, self).__init__(**kw_args)

    def getMarket(self):
        
        return self._Market

    def setMarket(self, value):
        if self._Market is not None:
            filtered = [x for x in self.Market.MarketProducts if x != self]
            self._Market._MarketProducts = filtered

        self._Market = value
        if self._Market is not None:
            self._Market._MarketProducts.append(self)

    Market = property(getMarket, setMarket)

    def getRegisteredResources(self):
        """A registered resource is eligible to bid market products
        """
        return self._RegisteredResources

    def setRegisteredResources(self, value):
        for p in self._RegisteredResources:
            filtered = [q for q in p.MarketProducts if q != self]
            self._RegisteredResources._MarketProducts = filtered
        for r in value:
            if self not in r._MarketProducts:
                r._MarketProducts.append(self)
        self._RegisteredResources = value

    RegisteredResources = property(getRegisteredResources, setRegisteredResources)

    def addRegisteredResources(self, *RegisteredResources):
        for obj in RegisteredResources:
            if self not in obj._MarketProducts:
                obj._MarketProducts.append(self)
            self._RegisteredResources.append(obj)

    def removeRegisteredResources(self, *RegisteredResources):
        for obj in RegisteredResources:
            if self in obj._MarketProducts:
                obj._MarketProducts.remove(self)
            self._RegisteredResources.remove(obj)

    def getReserveReqs(self):
        """Market product associated with reserve requirement must be a reserve or regulation product.
        """
        return self._ReserveReqs

    def setReserveReqs(self, value):
        for x in self._ReserveReqs:
            x._MarketProduct = None
        for y in value:
            y._MarketProduct = self
        self._ReserveReqs = value

    ReserveReqs = property(getReserveReqs, setReserveReqs)

    def addReserveReqs(self, *ReserveReqs):
        for obj in ReserveReqs:
            obj._MarketProduct = self
            self._ReserveReqs.append(obj)

    def removeReserveReqs(self, *ReserveReqs):
        for obj in ReserveReqs:
            obj._MarketProduct = None
            self._ReserveReqs.remove(obj)

    def getProductBids(self):
        
        return self._ProductBids

    def setProductBids(self, value):
        for x in self._ProductBids:
            x._MarketProduct = None
        for y in value:
            y._MarketProduct = self
        self._ProductBids = value

    ProductBids = property(getProductBids, setProductBids)

    def addProductBids(self, *ProductBids):
        for obj in ProductBids:
            obj._MarketProduct = self
            self._ProductBids.append(obj)

    def removeProductBids(self, *ProductBids):
        for obj in ProductBids:
            obj._MarketProduct = None
            self._ProductBids.remove(obj)

