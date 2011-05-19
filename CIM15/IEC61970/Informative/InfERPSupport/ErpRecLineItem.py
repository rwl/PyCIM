# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ErpRecLineItem(IdentifiedObject):
    """Individual entry of an ErpReceivable, it is a particular transaction representing an invoice, credit memo or debit memo to a customer.Individual entry of an ErpReceivable, it is a particular transaction representing an invoice, credit memo or debit memo to a customer.
    """

    def __init__(self, ErpReceivable=None, status=None, ErpInvoiceLineItem=None, ErpPayments=None, ErpJournalEntries=None, *args, **kw_args):
        """Initialises a new 'ErpRecLineItem' instance.

        @param ErpReceivable:
        @param status:
        @param ErpInvoiceLineItem:
        @param ErpPayments:
        @param ErpJournalEntries:
        """
        self._ErpReceivable = None
        self.ErpReceivable = ErpReceivable

        self.status = status

        self._ErpInvoiceLineItem = None
        self.ErpInvoiceLineItem = ErpInvoiceLineItem

        self._ErpPayments = []
        self.ErpPayments = [] if ErpPayments is None else ErpPayments

        self._ErpJournalEntries = []
        self.ErpJournalEntries = [] if ErpJournalEntries is None else ErpJournalEntries

        super(ErpRecLineItem, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpReceivable", "status", "ErpInvoiceLineItem", "ErpPayments", "ErpJournalEntries"]
    _many_refs = ["ErpPayments", "ErpJournalEntries"]

    def getErpReceivable(self):
        
        return self._ErpReceivable

    def setErpReceivable(self, value):
        if self._ErpReceivable is not None:
            filtered = [x for x in self.ErpReceivable.ErpRecLineItems if x != self]
            self._ErpReceivable._ErpRecLineItems = filtered

        self._ErpReceivable = value
        if self._ErpReceivable is not None:
            if self not in self._ErpReceivable._ErpRecLineItems:
                self._ErpReceivable._ErpRecLineItems.append(self)

    ErpReceivable = property(getErpReceivable, setErpReceivable)

    status = None

    def getErpInvoiceLineItem(self):
        
        return self._ErpInvoiceLineItem

    def setErpInvoiceLineItem(self, value):
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem._ErpRecLineItem = None

        self._ErpInvoiceLineItem = value
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem.ErpRecLineItem = None
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

