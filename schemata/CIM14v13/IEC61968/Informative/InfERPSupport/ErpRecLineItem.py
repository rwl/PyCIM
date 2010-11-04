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

class ErpRecLineItem(IdentifiedObject):
    """Individual entry of an ErpReceivable, it is a particular transaction representing an invoice, credit memo or debit memo to a customer.
    """

    def __init__(self, ErpInvoiceLineItem=None, ErpPayments=None, ErpJournalEntries=None, ErpReceivable=None, status=None, **kw_args):
        """Initializes a new 'ErpRecLineItem' instance.

        @param ErpInvoiceLineItem:
        @param ErpPayments:
        @param ErpJournalEntries:
        @param ErpReceivable:
        @param status:
        """
        self._ErpInvoiceLineItem = None
        self.ErpInvoiceLineItem = ErpInvoiceLineItem

        self._ErpPayments = []
        self.ErpPayments = [] if ErpPayments is None else ErpPayments

        self._ErpJournalEntries = []
        self.ErpJournalEntries = [] if ErpJournalEntries is None else ErpJournalEntries

        self._ErpReceivable = None
        self.ErpReceivable = ErpReceivable

        self.status = status

        super(ErpRecLineItem, self).__init__(**kw_args)

    def getErpInvoiceLineItem(self):
        
        return self._ErpInvoiceLineItem

    def setErpInvoiceLineItem(self, value):
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem._ErpRecLineItem = None

        self._ErpInvoiceLineItem = value
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem._ErpRecLineItem = self

    ErpInvoiceLineItem = property(getErpInvoiceLineItem, setErpInvoiceLineItem)

    def getErpPayments(self):
        
        return self._ErpPayments

    def setErpPayments(self, value):
        for p in self._ErpPayments:
            filtered = [q for q in p.ErpRecLineItems if q != self]
            self._ErpPayments._ErpRecLineItems = filtered
        for r in value:
            if self not in r._ErpRecLineItems:
                r._ErpRecLineItems.append(self)
        self._ErpPayments = value

    ErpPayments = property(getErpPayments, setErpPayments)

    def addErpPayments(self, *ErpPayments):
        for obj in ErpPayments:
            if self not in obj._ErpRecLineItems:
                obj._ErpRecLineItems.append(self)
            self._ErpPayments.append(obj)

    def removeErpPayments(self, *ErpPayments):
        for obj in ErpPayments:
            if self in obj._ErpRecLineItems:
                obj._ErpRecLineItems.remove(self)
            self._ErpPayments.remove(obj)

    def getErpJournalEntries(self):
        
        return self._ErpJournalEntries

    def setErpJournalEntries(self, value):
        for p in self._ErpJournalEntries:
            filtered = [q for q in p.ErpRecLineItems if q != self]
            self._ErpJournalEntries._ErpRecLineItems = filtered
        for r in value:
            if self not in r._ErpRecLineItems:
                r._ErpRecLineItems.append(self)
        self._ErpJournalEntries = value

    ErpJournalEntries = property(getErpJournalEntries, setErpJournalEntries)

    def addErpJournalEntries(self, *ErpJournalEntries):
        for obj in ErpJournalEntries:
            if self not in obj._ErpRecLineItems:
                obj._ErpRecLineItems.append(self)
            self._ErpJournalEntries.append(obj)

    def removeErpJournalEntries(self, *ErpJournalEntries):
        for obj in ErpJournalEntries:
            if self in obj._ErpRecLineItems:
                obj._ErpRecLineItems.remove(self)
            self._ErpJournalEntries.remove(obj)

    def getErpReceivable(self):
        
        return self._ErpReceivable

    def setErpReceivable(self, value):
        if self._ErpReceivable is not None:
            filtered = [x for x in self.ErpReceivable.ErpRecLineItems if x != self]
            self._ErpReceivable._ErpRecLineItems = filtered

        self._ErpReceivable = value
        if self._ErpReceivable is not None:
            self._ErpReceivable._ErpRecLineItems.append(self)

    ErpReceivable = property(getErpReceivable, setErpReceivable)

    status = None

