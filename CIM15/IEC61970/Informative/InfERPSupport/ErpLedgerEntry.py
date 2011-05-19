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

class ErpLedgerEntry(IdentifiedObject):
    """Details of an individual entry in a ledger, which was posted from a journal on the posted date.Details of an individual entry in a ledger, which was posted from a journal on the posted date.
    """

    def __init__(self, transactionDateTime='', accountKind="normal", amount=0.0, postedDateTime='', accountID='', ErpLedger=None, status=None, ErpLedgerEntry=None, UserAttributes=None, ErpJounalEntry=None, *args, **kw_args):
        """Initialises a new 'ErpLedgerEntry' instance.

        @param transactionDateTime: Date and time journal entry was recorded. 
        @param accountKind: Kind of account for this entry. Values are: "normal", "estimate", "statistical", "reversal"
        @param amount: The amount of the debit or credit for this account. 
        @param postedDateTime: Date and time this entry was posted to the ledger. 
        @param accountID: Account identifier for this entry. 
        @param ErpLedger:
        @param status:
        @param ErpLedgerEntry:
        @param UserAttributes:
        @param ErpJounalEntry:
        """
        #: Date and time journal entry was recorded.
        self.transactionDateTime = transactionDateTime

        #: Kind of account for this entry. Values are: "normal", "estimate", "statistical", "reversal"
        self.accountKind = accountKind

        #: The amount of the debit or credit for this account.
        self.amount = amount

        #: Date and time this entry was posted to the ledger.
        self.postedDateTime = postedDateTime

        #: Account identifier for this entry.
        self.accountID = accountID

        self._ErpLedger = None
        self.ErpLedger = ErpLedger

        self.status = status

        self._ErpLedgerEntry = None
        self.ErpLedgerEntry = ErpLedgerEntry

        self._UserAttributes = []
        self.UserAttributes = [] if UserAttributes is None else UserAttributes

        self._ErpJounalEntry = None
        self.ErpJounalEntry = ErpJounalEntry

        super(ErpLedgerEntry, self).__init__(*args, **kw_args)

    _attrs = ["transactionDateTime", "accountKind", "amount", "postedDateTime", "accountID"]
    _attr_types = {"transactionDateTime": str, "accountKind": str, "amount": float, "postedDateTime": str, "accountID": str}
    _defaults = {"transactionDateTime": '', "accountKind": "normal", "amount": 0.0, "postedDateTime": '', "accountID": ''}
    _enums = {"accountKind": "ErpAccountKind"}
    _refs = ["ErpLedger", "status", "ErpLedgerEntry", "UserAttributes", "ErpJounalEntry"]
    _many_refs = ["UserAttributes"]

    def getErpLedger(self):
        
        return self._ErpLedger

    def setErpLedger(self, value):
        if self._ErpLedger is not None:
            filtered = [x for x in self.ErpLedger.ErpLedgerEntries if x != self]
            self._ErpLedger._ErpLedgerEntries = filtered

        self._ErpLedger = value
        if self._ErpLedger is not None:
            if self not in self._ErpLedger._ErpLedgerEntries:
                self._ErpLedger._ErpLedgerEntries.append(self)

    ErpLedger = property(getErpLedger, setErpLedger)

    status = None

    def getErpLedgerEntry(self):
        
        return self._ErpLedgerEntry

    def setErpLedgerEntry(self, value):
        if self._ErpLedgerEntry is not None:
            self._ErpLedgerEntry._ErpLedBudLineItem = None

        self._ErpLedgerEntry = value
        if self._ErpLedgerEntry is not None:
            self._ErpLedgerEntry.ErpLedBudLineItem = None
            self._ErpLedgerEntry._ErpLedBudLineItem = self

    ErpLedgerEntry = property(getErpLedgerEntry, setErpLedgerEntry)

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

    def getErpJounalEntry(self):
        
        return self._ErpJounalEntry

    def setErpJounalEntry(self, value):
        if self._ErpJounalEntry is not None:
            self._ErpJounalEntry._ErpLedgerEntry = None

        self._ErpJounalEntry = value
        if self._ErpJounalEntry is not None:
            self._ErpJounalEntry.ErpLedgerEntry = None
            self._ErpJounalEntry._ErpLedgerEntry = self

    ErpJounalEntry = property(getErpJounalEntry, setErpJounalEntry)

