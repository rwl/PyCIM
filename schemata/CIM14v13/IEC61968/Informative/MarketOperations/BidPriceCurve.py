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

class BidPriceCurve(Curve):
    """Relationship between unit operating price in $/hour (Y-axis) and unit output in MW (X-axis).
    """

    def __init__(self, ProductBids=None, **kw_args):
        """Initializes a new 'BidPriceCurve' instance.

        @param ProductBids:
        """
        self._ProductBids = []
        self.ProductBids = [] if ProductBids is None else ProductBids

        super(BidPriceCurve, self).__init__(**kw_args)

    def getProductBids(self):
        
        return self._ProductBids

    def setProductBids(self, value):
        for x in self._ProductBids:
            x._BidPriceCurve = None
        for y in value:
            y._BidPriceCurve = self
        self._ProductBids = value

    ProductBids = property(getProductBids, setProductBids)

    def addProductBids(self, *ProductBids):
        for obj in ProductBids:
            obj._BidPriceCurve = self
            self._ProductBids.append(obj)

    def removeProductBids(self, *ProductBids):
        for obj in ProductBids:
            obj._BidPriceCurve = None
            self._ProductBids.remove(obj)

