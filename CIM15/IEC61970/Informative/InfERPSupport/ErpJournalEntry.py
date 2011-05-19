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

class ErpJournalEntry(IdentifiedObject):
    """Details of an individual entry in a journal, which is to be posted to a ledger on the posting date.Details of an individual entry in a journal, which is to be posted to a ledger on the posting date.
    """

    def __init__(self, transactionDateTime='', sourceID='', postingDateTime='', amount=0.0, accountID='', status=None, ErpPayableLineItems=None, ErpInvoiceLineItem=None, ErpRecLineItems=None, ErpLedgerEntry=None, CostTypes=None, ErpJournal=None, *args, **kw_args):
        """Initialises a new 'ErpJournalEntry' instance.

        @param transactionDateTime: Date and time journal entry was recorded. 
        @param sourceID: The identifer of the source for this entry. 
        @param postingDateTime: Date and time this entry is to be posted to the ledger. 
        @param amount: The amount of the debit or credit for this account. 
        @param accountID: Account identifier for this entry. 
        @param status:
        @param ErpPayableLineItems:
        @param ErpInvoiceLineItem:
        @param ErpRecLineItems:
        @param ErpLedgerEntry:
        @param CostTypes:
        @param ErpJournal:
        """
        #: Date and time journal entry was recorded.
        self.transactionDateTime = transactionDateTime

        #: The identifer of the source for this entry.
        self.sourceID = sourceID

        #: Date and time this entry is to be posted to the ledger.
        self.postingDateTime = postingDateTime

        #: The amount of the debit or credit for this account.
        self.amount = amount

        #: Account identifier for this entry.
        self.accountID = accountID

        self.status = status

        self._ErpPayableLineItems = []
        self.ErpPayableLineItems = [] if ErpPayableLineItems is None else ErpPayableLineItems

        self._ErpInvoiceLineItem = None
        self.ErpInvoiceLineItem = ErpInvoiceLineItem

        self._ErpRecLineItems = []
        self.ErpRecLineItems = [] if ErpRecLineItems is None else ErpRecLineItems

        self._ErpLedgerEntry = None
        self.ErpLedgerEntry = ErpLedgerEntry

        self._CostTypes = []
        self.CostTypes = [] if CostTypes is None else CostTypes

        self._ErpJournal = None
        self.ErpJournal = ErpJournal

        super(ErpJournalEntry, self).__init__(*args, **kw_args)

    _attrs = ["transactionDateTime", "sourceID", "postingDateTime", "amount", "accountID"]
    _attr_types = {"transactionDateTime": str, "sourceID": str, "postingDateTime": str, "amount": float, "accountID": str}
    _defaults = {"transactionDateTime": '', "sourceID": '', "postingDateTime": '', "amount": 0.0, "accountID": ''}
    _enums = {}
    _refs = ["status", "ErpPayableLineItems", "ErpInvoiceLineItem", "ErpRecLineItems", "ErpLedgerEntry", "CostTypes", "ErpJournal"]
    _many_refs = ["ErpPayableLineItems", "ErpRecLineItems", "CostTypes"]

    status = None

    def getErpPayableLineItems(self):
        
        return self._ErpPayableLineItems

    def setErpPayableLineItems(self, value):
        for p in self._ErpPayableLineItems:
            filtered = [q for q in p.ErpJournalEntries if q != self]
            self._ErpPayableLineItems._ErpJournalEntries = filtered
        for r in value:
            if self not in r._ErpJournalEntries:
                r._ErpJournalEntries.append(self)
        self._ErpPayableLineItems = value

    ErpPayableLineItems = property(getErpPayableLineItems, setErpPayableLineItems)

    def addErpPayableLineItems(self, *ErpPayableLineItems):
        for obj in ErpPayableLineItems:
            if self not in obj._ErpJournalEntries:
                obj._ErpJournalEntries.append(self)
            self._ErpPayableLineItems.append(obj)

    def removeErpPayableLineItems(self, *ErpPayableLineItems):
        for obj in ErpPayableLineItems:
            if self in obj._ErpJournalEntries:
                obj._ErpJournalEntries.remove(self)
            self._ErpPayableLineItems.remove(obj)

    def getErpInvoiceLineItem(self):
        
        return self._ErpInvoiceLineItem

    def setErpInvoiceLineItem(self, value):
        if self._ErpInvoiceLineItem is not None:
            filtered = [x for x in self.ErpInvoiceLineItem.ErpJournalEntries if x != self]
            self._ErpInvoiceLineItem._ErpJournalEntries = filtered

        self._ErpInvoiceLineItem = value
        if self._ErpInvoiceLineItem is not None:
            if self not in self._ErpInvoiceLineItem._ErpJournalEntries:
                self._ErpInvoiceLineItem._ErpJournalEntries.append(self)

    ErpInvoiceLineItem = property(getErpInvoiceLineItem, setErpInvoiceLineItem)

    def getErpRecLineItems(self):
        
        return self._ErpRecLineItems

    def setErpRecLineItems(self, value):
        for p in self._ErpRecLineItems:
            filtered = [q for q in p.ErpJournalEntries if q != self]
            self._ErpRecLineItems._ErpJournalEntries = filtered
        for r in value:
            if self not in r._ErpJournalEntries:
                r._ErpJournalEntries.append(self)
        self._ErpRecLineItems = value

    ErpRecLineItems = property(getErpRecLineItems, setErpRecLineItems)

    def addErpRecLineItems(self, *ErpRecLineItems):
        for obj in ErpRecLineItems:
            if self not in obj._ErpJournalEntries:
                obj._ErpJournalEntries.append(self)
            self._ErpRecLineItems.append(obj)

    def removeErpRecLineItems(self, *ErpRecLineItems):
        for obj in ErpRecLineItems:
            if self in obj._ErpJournalEntries:
                obj._ErpJournalEntries.remove(self)
            self._ErpRecLineItems.remove(obj)

    def getErpLedgerEntry(self):
        
        return self._ErpLedgerEntry

    def setErpLedgerEntry(self, value):
        if self._ErpLedgerEntry is not None:
            self._ErpLedgerEntry._ErpJounalEntry = None

        self._ErpLedgerEntry = value
        if self._ErpLedgerEntry is not None:
            self._ErpLedgerEntry.ErpJounalEntry = None
            self._ErpLedgerEntry._ErpJounalEntry = self

    ErpLedgerEntry = property(getErpLedgerEntry, setErpLedgerEntry)

    def getCostTypes(self):
        
        return self._CostTypes

    def setCostTypes(self, value):
        for p in self._CostTypes:
            filtered = [q for q in p.ErpJournalEntries if q != self]
            self._CostTypes._ErpJournalEntries = filtered
        for r in value:
            if self not in r._ErpJournalEntries:
                r._ErpJournalEntries.append(self)
        self._CostTypes = value

    CostTypes = property(getCostTypes, setCostTypes)

    def addCostTypes(self, *CostTypes):
        for obj in CostTypes:
            if self not in obj._ErpJournalEntries:
                obj._ErpJournalEntries.append(self)
            self._CostTypes.append(obj)

    def removeCostTypes(self, *CostTypes):
        for obj in CostTypes:
            if self in obj._ErpJournalEntries:
                obj._ErpJournalEntries.remove(self)
            self._CostTypes.remove(obj)

    def getErpJournal(self):
        
        return self._ErpJournal

    def setErpJournal(self, value):
        if self._ErpJournal is not None:
            filtered = [x for x in self.ErpJournal.ErpJournalEntries if x != self]
            self._ErpJournal._ErpJournalEntries = filtered

        self._ErpJournal = value
        if self._ErpJournal is not None:
            if self not in self._ErpJournal._ErpJournalEntries:
                self._ErpJournal._ErpJournalEntries.append(self)

    ErpJournal = property(getErpJournal, setErpJournal)

