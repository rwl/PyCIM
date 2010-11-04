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

from CIM14v13.IEC61968.Informative.MarketOperations.ResourceGroupReq import ResourceGroupReq

class ReserveReq(ResourceGroupReq):
    """Requirements for minimum amount of reserve and/or regulation to be supplied by a set of qualified resources.
    """

    def __init__(self, MarketProduct=None, ReserveReqCurve=None, SensitivityPriceCurve=None, **kw_args):
        """Initializes a new 'ReserveReq' instance.

        @param MarketProduct: Market product associated with reserve requirement must be a reserve or regulation product.
        @param ReserveReqCurve:
        @param SensitivityPriceCurve:
        """
        self._MarketProduct = None
        self.MarketProduct = MarketProduct

        self._ReserveReqCurve = None
        self.ReserveReqCurve = ReserveReqCurve

        self._SensitivityPriceCurve = None
        self.SensitivityPriceCurve = SensitivityPriceCurve

        super(ReserveReq, self).__init__(**kw_args)

    def getMarketProduct(self):
        """Market product associated with reserve requirement must be a reserve or regulation product.
        """
        return self._MarketProduct

    def setMarketProduct(self, value):
        if self._MarketProduct is not None:
            filtered = [x for x in self.MarketProduct.ReserveReqs if x != self]
            self._MarketProduct._ReserveReqs = filtered

        self._MarketProduct = value
        if self._MarketProduct is not None:
            self._MarketProduct._ReserveReqs.append(self)

    MarketProduct = property(getMarketProduct, setMarketProduct)

    def getReserveReqCurve(self):
        
        return self._ReserveReqCurve

    def setReserveReqCurve(self, value):
        if self._ReserveReqCurve is not None:
            self._ReserveReqCurve._ReserveReq = None

        self._ReserveReqCurve = value
        if self._ReserveReqCurve is not None:
            self._ReserveReqCurve._ReserveReq = self

    ReserveReqCurve = property(getReserveReqCurve, setReserveReqCurve)

    def getSensitivityPriceCurve(self):
        
        return self._SensitivityPriceCurve

    def setSensitivityPriceCurve(self, value):
        if self._SensitivityPriceCurve is not None:
            self._SensitivityPriceCurve._ReserveReq = None

        self._SensitivityPriceCurve = value
        if self._SensitivityPriceCurve is not None:
            self._SensitivityPriceCurve._ReserveReq = self

    SensitivityPriceCurve = property(getSensitivityPriceCurve, setSensitivityPriceCurve)

