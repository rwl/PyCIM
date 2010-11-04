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

class Settlement(Document):
    """Specifies a settlement run.
    """

    def __init__(self, tradeDate='', Market=None, ErpLedgerEntries=None, ErpInvoiceLineItems=None, *args, **kw_args):
        """Initializes a new 'Settlement' instance.

        @param tradeDate: The trade date on which the settlement is run. 
        @param Market:
        @param ErpLedgerEntries:
        @param ErpInvoiceLineItems:
        """
        #: The trade date on which the settlement is run.
        self.tradeDate = tradeDate

        self._Market = None
        self.Market = Market

        self._ErpLedgerEntries = []
        self.ErpLedgerEntries = [] if ErpLedgerEntries is None else ErpLedgerEntries

        self._ErpInvoiceLineItems = []
        self.ErpInvoiceLineItems = [] if ErpInvoiceLineItems is None else ErpInvoiceLineItems

        super(Settlement, self).__init__(*args, **kw_args)

    def getMarket(self):
        
        return self._Market

    def setMarket(self, value):
        if self._Market is not None:
            filtered = [x for x in self.Market.Settlements if x != self]
            self._Market._Settlements = filtered

        self._Market = value
        if self._Market is not None:
            self._Market._Settlements.append(self)

    Market = property(getMarket, setMarket)

    def getErpLedgerEntries(self):
        
        return self._ErpLedgerEntries

    def setErpLedgerEntries(self, value):
        for p in self._ErpLedgerEntries:
            filtered = [q for q in p.Settlements if q != self]
            self._ErpLedgerEntries._Settlements = filtered
        for r in value:
            if self not in r._Settlements:
                r._Settlements.append(self)
        self._ErpLedgerEntries = value

    ErpLedgerEntries = property(getErpLedgerEntries, setErpLedgerEntries)

    def addErpLedgerEntries(self, *ErpLedgerEntries):
        for obj in ErpLedgerEntries:
            if self not in obj._Settlements:
                obj._Settlements.append(self)
            self._ErpLedgerEntries.append(obj)

    def removeErpLedgerEntries(self, *ErpLedgerEntries):
        for obj in ErpLedgerEntries:
            if self in obj._Settlements:
                obj._Settlements.remove(self)
            self._ErpLedgerEntries.remove(obj)

    def getErpInvoiceLineItems(self):
        
        return self._ErpInvoiceLineItems

    def setErpInvoiceLineItems(self, value):
        for p in self._ErpInvoiceLineItems:
            filtered = [q for q in p.Settlements if q != self]
            self._ErpInvoiceLineItems._Settlements = filtered
        for r in value:
            if self not in r._Settlements:
                r._Settlements.append(self)
        self._ErpInvoiceLineItems = value

    ErpInvoiceLineItems = property(getErpInvoiceLineItems, setErpInvoiceLineItems)

    def addErpInvoiceLineItems(self, *ErpInvoiceLineItems):
        for obj in ErpInvoiceLineItems:
            if self not in obj._Settlements:
                obj._Settlements.append(self)
            self._ErpInvoiceLineItems.append(obj)

    def removeErpInvoiceLineItems(self, *ErpInvoiceLineItems):
        for obj in ErpInvoiceLineItems:
            if self in obj._Settlements:
                obj._Settlements.remove(self)
            self._ErpInvoiceLineItems.remove(obj)

