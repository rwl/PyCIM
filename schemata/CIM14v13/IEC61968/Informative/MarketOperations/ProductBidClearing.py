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

from CIM14v13.IEC61968.Informative.MarketOperations.MarketFactors import MarketFactors

class ProductBidClearing(MarketFactors):
    """Product Bid clearing results posted for a given settlement period.
    """

    def __init__(self, clearedMW=0.0, ProductBids=None, *args, **kw_args):
        """Initializes a new 'ProductBidClearing' instance.

        @param clearedMW: Cleared MWs. 
        @param ProductBids:
        """
        #: Cleared MWs. 
        self.clearedMW = clearedMW

        self._ProductBids = []
        self.ProductBids = [] if ProductBids is None else ProductBids

        super(ProductBidClearing, self).__init__(*args, **kw_args)

    def getProductBids(self):
        
        return self._ProductBids

    def setProductBids(self, value):
        for x in self._ProductBids:
            x._ProductBidClearing = None
        for y in value:
            y._ProductBidClearing = self
        self._ProductBids = value

    ProductBids = property(getProductBids, setProductBids)

    def addProductBids(self, *ProductBids):
        for obj in ProductBids:
            obj._ProductBidClearing = self
            self._ProductBids.append(obj)

    def removeProductBids(self, *ProductBids):
        for obj in ProductBids:
            obj._ProductBidClearing = None
            self._ProductBids.remove(obj)

