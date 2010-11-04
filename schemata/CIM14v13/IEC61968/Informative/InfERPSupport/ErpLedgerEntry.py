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

class ErpLedgerEntry(IdentifiedObject):
    """Details of an individual entry in a ledger, which was posted from a journal on the posted date.
    """

    def __init__(self, accountKind='estimate', amount=0.0, accountID='', transactionDateTime='', postedDateTime='', ErpLedger=None, UserAttributes=None, ErpLedgerEntry=None, Settlements=None, ErpJounalEntry=None, status=None, **kw_args):
        """Initializes a new 'ErpLedgerEntry' instance.

        @param accountKind: Kind of account for this entry. Values are: "estimate", "reversal", "statistical", "normal"
        @param amount: The amount of the debit or credit for this account. 
        @param accountID: Account identifier for this entry. 
        @param transactionDateTime: Date and time journal entry was recorded. 
        @param postedDateTime: Date and time this entry was posted to the ledger. 
        @param ErpLedger:
        @param UserAttributes:
        @param ErpLedgerEntry:
        @param Settlements:
        @param ErpJounalEntry:
        @param status:
        """
        #: Kind of account for this entry.Values are: "estimate", "reversal", "statistical", "normal"
        self.accountKind = accountKind

        #: The amount of the debit or credit for this account.
        self.amount = amount

        #: Account identifier for this entry.
        self.accountID = accountID

        #: Date and time journal entry was recorded.
        self.transactionDateTime = transactionDateTime

        #: Date and time this entry was posted to the ledger.
        self.postedDateTime = postedDateTime

        self._ErpLedger = None
        self.ErpLedger = ErpLedger

        self._UserAttributes = []
        self.UserAttributes = [] if UserAttributes is None else UserAttributes

        self._ErpLedgerEntry = None
        self.ErpLedgerEntry = ErpLedgerEntry

        self._Settlements = []
        self.Settlements = [] if Settlements is None else Settlements

        self._ErpJounalEntry = None
        self.ErpJounalEntry = ErpJounalEntry

        self.status = status

        super(ErpLedgerEntry, self).__init__(**kw_args)

    def getErpLedger(self):
        
        return self._ErpLedger

    def setErpLedger(self, value):
        if self._ErpLedger is not None:
            filtered = [x for x in self.ErpLedger.ErpLedgerEntries if x != self]
            self._ErpLedger._ErpLedgerEntries = filtered

        self._ErpLedger = value
        if self._ErpLedger is not None:
            self._ErpLedger._ErpLedgerEntries.append(self)

    ErpLedger = property(getErpLedger, setErpLedger)

    def getUserAttributes(self):
        
        return self._UserAttributes

    def setUserAttributes(self, value):
        for p in self._UserAttributes:
            filtered = [q for q in p.ErpLedgerEntries if q != self]
            self._UserAttributes._ErpLedgerEntries = filtered
        for r in value:
            if self not in r._ErpLedgerEntries:
                r._ErpLedgerEntries.append(self)
        self._UserAttributes = value

    UserAttributes = property(getUserAttributes, setUserAttributes)

    def addUserAttributes(self, *UserAttributes):
        for obj in UserAttributes:
            if self not in obj._ErpLedgerEntries:
                obj._ErpLedgerEntries.append(self)
            self._UserAttributes.append(obj)

    def removeUserAttributes(self, *UserAttributes):
        for obj in UserAttributes:
            if self in obj._ErpLedgerEntries:
                obj._ErpLedgerEntries.remove(self)
            self._UserAttributes.remove(obj)

    def getErpLedgerEntry(self):
        
        return self._ErpLedgerEntry

    def setErpLedgerEntry(self, value):
        if self._ErpLedgerEntry is not None:
            self._ErpLedgerEntry._ErpLedBudLineItem = None

        self._ErpLedgerEntry = value
        if self._ErpLedgerEntry is not None:
            self._ErpLedgerEntry._ErpLedBudLineItem = self

    ErpLedgerEntry = property(getErpLedgerEntry, setErpLedgerEntry)

    def getSettlements(self):
        
        return self._Settlements

    def setSettlements(self, value):
        for p in self._Settlements:
            filtered = [q for q in p.ErpLedgerEntries if q != self]
            self._Settlements._ErpLedgerEntries = filtered
        for r in value:
            if self not in r._ErpLedgerEntries:
                r._ErpLedgerEntries.append(self)
        self._Settlements = value

    Settlements = property(getSettlements, setSettlements)

    def addSettlements(self, *Settlements):
        for obj in Settlements:
            if self not in obj._ErpLedgerEntries:
                obj._ErpLedgerEntries.append(self)
            self._Settlements.append(obj)

    def removeSettlements(self, *Settlements):
        for obj in Settlements:
            if self in obj._ErpLedgerEntries:
                obj._ErpLedgerEntries.remove(self)
            self._Settlements.remove(obj)

    def getErpJounalEntry(self):
        
        return self._ErpJounalEntry

    def setErpJounalEntry(self, value):
        if self._ErpJounalEntry is not None:
            self._ErpJounalEntry._ErpLedgerEntry = None

        self._ErpJounalEntry = value
        if self._ErpJounalEntry is not None:
            self._ErpJounalEntry._ErpLedgerEntry = self

    ErpJounalEntry = property(getErpJounalEntry, setErpJounalEntry)

    status = None

