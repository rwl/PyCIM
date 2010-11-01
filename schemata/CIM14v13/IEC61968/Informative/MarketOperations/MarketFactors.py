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

class MarketFactors(Document):
    """Aggregation of market information relative for a specific time interval.
    """

    def __init__(self, intervalStartTime='', ErpInvoices=None, Market=None, *args, **kw_args):
        """Initializes a new 'MarketFactors' instance.

        @param intervalStartTime: The start of the time interval for which requirement is defined. 
        @param ErpInvoices:
        @param Market:
        """
        #: The start of the time interval for which requirement is defined. 
        self.intervalStartTime = intervalStartTime

        self._ErpInvoices = []
        self.ErpInvoices = [] if ErpInvoices is None else ErpInvoices

        self._Market = None
        self.Market = Market

        super(MarketFactors, self).__init__(*args, **kw_args)

    def getErpInvoices(self):
        
        return self._ErpInvoices

    def setErpInvoices(self, value):
        for p in self._ErpInvoices:
            filtered = [q for q in p.MarketFactors if q != self]
            self._ErpInvoices._MarketFactors = filtered
        for r in value:
            if self not in r._MarketFactors:
                r._MarketFactors.append(self)
        self._ErpInvoices = value

    ErpInvoices = property(getErpInvoices, setErpInvoices)

    def addErpInvoices(self, *ErpInvoices):
        for obj in ErpInvoices:
            if self not in obj._MarketFactors:
                obj._MarketFactors.append(self)
            self._ErpInvoices.append(obj)

    def removeErpInvoices(self, *ErpInvoices):
        for obj in ErpInvoices:
            if self in obj._MarketFactors:
                obj._MarketFactors.remove(self)
            self._ErpInvoices.remove(obj)

    def getMarket(self):
        
        return self._Market

    def setMarket(self, value):
        if self._Market is not None:
            filtered = [x for x in self.Market.MarketFactors if x != self]
            self._Market._MarketFactors = filtered

        self._Market = value
        if self._Market is not None:
            self._Market._MarketFactors.append(self)

    Market = property(getMarket, setMarket)

