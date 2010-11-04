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

class ErpJournalEntry(IdentifiedObject):
    """Details of an individual entry in a journal, which is to be posted to a ledger on the posting date.
    """

    def __init__(self, transactionDateTime='', accountID='', postingDateTime='', amount=0.0, sourceID='', ErpPayableLineItems=None, ErpInvoiceLineItem=None, status=None, ErpJournal=None, CostTypes=None, ErpLedgerEntry=None, ErpRecLineItems=None, *args, **kw_args):
        """Initializes a new 'ErpJournalEntry' instance.

        @param transactionDateTime: Date and time journal entry was recorded. 
        @param accountID: Account identifier for this entry. 
        @param postingDateTime: Date and time this entry is to be posted to the ledger. 
        @param amount: The amount of the debit or credit for this account. 
        @param sourceID: The identifer of the source for this entry. 
        @param ErpPayableLineItems:
        @param ErpInvoiceLineItem:
        @param status:
        @param ErpJournal:
        @param CostTypes:
        @param ErpLedgerEntry:
        @param ErpRecLineItems:
        """
        #: Date and time journal entry was recorded.
        self.transactionDateTime = transactionDateTime

        #: Account identifier for this entry.
        self.accountID = accountID

        #: Date and time this entry is to be posted to the ledger.
        self.postingDateTime = postingDateTime

        #: The amount of the debit or credit for this account.
        self.amount = amount

        #: The identifer of the source for this entry.
        self.sourceID = sourceID

        self._ErpPayableLineItems = []
        self.ErpPayableLineItems = [] if ErpPayableLineItems is None else ErpPayableLineItems

        self._ErpInvoiceLineItem = None
        self.ErpInvoiceLineItem = ErpInvoiceLineItem

        self.status = status

        self._ErpJournal = None
        self.ErpJournal = ErpJournal

        self._CostTypes = []
        self.CostTypes = [] if CostTypes is None else CostTypes

        self._ErpLedgerEntry = None
        self.ErpLedgerEntry = ErpLedgerEntry

        self._ErpRecLineItems = []
        self.ErpRecLineItems = [] if ErpRecLineItems is None else ErpRecLineItems

        super(ErpJournalEntry, self).__init__(*args, **kw_args)

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
            self._ErpInvoiceLineItem._ErpJournalEntries.append(self)

    ErpInvoiceLineItem = property(getErpInvoiceLineItem, setErpInvoiceLineItem)

    status = None

    def getErpJournal(self):
        
        return self._ErpJournal

    def setErpJournal(self, value):
        if self._ErpJournal is not None:
            filtered = [x for x in self.ErpJournal.ErpJournalEntries if x != self]
            self._ErpJournal._ErpJournalEntries = filtered

        self._ErpJournal = value
        if self._ErpJournal is not None:
            self._ErpJournal._ErpJournalEntries.append(self)

    ErpJournal = property(getErpJournal, setErpJournal)

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

    def getErpLedgerEntry(self):
        
        return self._ErpLedgerEntry

    def setErpLedgerEntry(self, value):
        if self._ErpLedgerEntry is not None:
            self._ErpLedgerEntry._ErpJounalEntry = None

        self._ErpLedgerEntry = value
        if self._ErpLedgerEntry is not None:
            self._ErpLedgerEntry._ErpJounalEntry = self

    ErpLedgerEntry = property(getErpLedgerEntry, setErpLedgerEntry)

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

