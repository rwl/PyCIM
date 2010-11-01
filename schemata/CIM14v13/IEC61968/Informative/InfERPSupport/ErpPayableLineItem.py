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

class ErpPayableLineItem(IdentifiedObject):
    """Of an ErpPayable, a line item references an ErpInvoiceLineitem or other source such as credit memos.
    """

    def __init__(self, ErpJournalEntries=None, status=None, ErpPayments=None, ErpInvoiceLineItem=None, ErpPayable=None, *args, **kw_args):
        """Initializes a new 'ErpPayableLineItem' instance.

        @param ErpJournalEntries:
        @param status:
        @param ErpPayments:
        @param ErpInvoiceLineItem:
        @param ErpPayable:
        """
        self._ErpJournalEntries = []
        self.ErpJournalEntries = [] if ErpJournalEntries is None else ErpJournalEntries

        self.status = status

        self._ErpPayments = []
        self.ErpPayments = [] if ErpPayments is None else ErpPayments

        self._ErpInvoiceLineItem = None
        self.ErpInvoiceLineItem = ErpInvoiceLineItem

        self._ErpPayable = None
        self.ErpPayable = ErpPayable

        super(ErpPayableLineItem, self).__init__(*args, **kw_args)

    def getErpJournalEntries(self):
        
        return self._ErpJournalEntries

    def setErpJournalEntries(self, value):
        for p in self._ErpJournalEntries:
            filtered = [q for q in p.ErpPayableLineItems if q != self]
            self._ErpJournalEntries._ErpPayableLineItems = filtered
        for r in value:
            if self not in r._ErpPayableLineItems:
                r._ErpPayableLineItems.append(self)
        self._ErpJournalEntries = value

    ErpJournalEntries = property(getErpJournalEntries, setErpJournalEntries)

    def addErpJournalEntries(self, *ErpJournalEntries):
        for obj in ErpJournalEntries:
            if self not in obj._ErpPayableLineItems:
                obj._ErpPayableLineItems.append(self)
            self._ErpJournalEntries.append(obj)

    def removeErpJournalEntries(self, *ErpJournalEntries):
        for obj in ErpJournalEntries:
            if self in obj._ErpPayableLineItems:
                obj._ErpPayableLineItems.remove(self)
            self._ErpJournalEntries.remove(obj)

    status = None

    def getErpPayments(self):
        
        return self._ErpPayments

    def setErpPayments(self, value):
        for p in self._ErpPayments:
            filtered = [q for q in p.ErpPayableLineItems if q != self]
            self._ErpPayments._ErpPayableLineItems = filtered
        for r in value:
            if self not in r._ErpPayableLineItems:
                r._ErpPayableLineItems.append(self)
        self._ErpPayments = value

    ErpPayments = property(getErpPayments, setErpPayments)

    def addErpPayments(self, *ErpPayments):
        for obj in ErpPayments:
            if self not in obj._ErpPayableLineItems:
                obj._ErpPayableLineItems.append(self)
            self._ErpPayments.append(obj)

    def removeErpPayments(self, *ErpPayments):
        for obj in ErpPayments:
            if self in obj._ErpPayableLineItems:
                obj._ErpPayableLineItems.remove(self)
            self._ErpPayments.remove(obj)

    def getErpInvoiceLineItem(self):
        
        return self._ErpInvoiceLineItem

    def setErpInvoiceLineItem(self, value):
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem._ErpPayableLineItem = None

        self._ErpInvoiceLineItem = value
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem._ErpPayableLineItem = self

    ErpInvoiceLineItem = property(getErpInvoiceLineItem, setErpInvoiceLineItem)

    def getErpPayable(self):
        
        return self._ErpPayable

    def setErpPayable(self, value):
        if self._ErpPayable is not None:
            filtered = [x for x in self.ErpPayable.ErpPayableLineItems if x != self]
            self._ErpPayable._ErpPayableLineItems = filtered

        self._ErpPayable = value
        if self._ErpPayable is not None:
            self._ErpPayable._ErpPayableLineItems.append(self)

    ErpPayable = property(getErpPayable, setErpPayable)

