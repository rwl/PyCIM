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

from CIM14.IEC61968.Common.Document import Document

class AuxiliaryAccount(Document):
    """Variable and dynamic part of AuxiliaryAgreement, generally representing the current state of the account related to the outstanding balance defined in AuxiliaryAgreement.
    """

    def __init__(self, balance=0.0, principleAmount=0.0, Charges=None, AuxiliaryAgreement=None, PaymentTransactions=None, lastDebit=None, lastCredit=None, due=None, *args, **kw_args):
        """Initialises a new 'AuxiliaryAccount' instance.

        @param balance: The total amount currently remaining on this account that is required to be paid in order to settle the account to zero. This excludes any due amounts not yet paid. 
        @param principleAmount: The initial principle amount, with which this account was instantiated. 
        @param Charges: All charges levied on this account.
        @param AuxiliaryAgreement: Auxiliary agreement regulating this account.
        @param PaymentTransactions: All payments against this account.
        @param lastDebit: Details of the last debit transaction performed on this account.
        @param lastCredit: Details of the last credit transaction performed on this account.
        @param due: Current amounts now due for payment on this account.
        """
        #: The total amount currently remaining on this account that is required to be paid in order to settle the account to zero. This excludes any due amounts not yet paid.
        self.balance = balance

        #: The initial principle amount, with which this account was instantiated.
        self.principleAmount = principleAmount

        self._Charges = []
        self.Charges = [] if Charges is None else Charges

        self._AuxiliaryAgreement = None
        self.AuxiliaryAgreement = AuxiliaryAgreement

        self._PaymentTransactions = []
        self.PaymentTransactions = [] if PaymentTransactions is None else PaymentTransactions

        self.lastDebit = lastDebit

        self.lastCredit = lastCredit

        self.due = due

        super(AuxiliaryAccount, self).__init__(*args, **kw_args)

    _attrs = ["balance", "principleAmount"]
    _attr_types = {"balance": float, "principleAmount": float}
    _defaults = {"balance": 0.0, "principleAmount": 0.0}
    _enums = {}
    _refs = ["Charges", "AuxiliaryAgreement", "PaymentTransactions", "lastDebit", "lastCredit", "due"]
    _many_refs = ["Charges", "PaymentTransactions"]

    def getCharges(self):
        """All charges levied on this account.
        """
        return self._Charges

    def setCharges(self, value):
        for p in self._Charges:
            filtered = [q for q in p.AuxiliaryAccounts if q != self]
            self._Charges._AuxiliaryAccounts = filtered
        for r in value:
            if self not in r._AuxiliaryAccounts:
                r._AuxiliaryAccounts.append(self)
        self._Charges = value

    Charges = property(getCharges, setCharges)

    def addCharges(self, *Charges):
        for obj in Charges:
            if self not in obj._AuxiliaryAccounts:
                obj._AuxiliaryAccounts.append(self)
            self._Charges.append(obj)

    def removeCharges(self, *Charges):
        for obj in Charges:
            if self in obj._AuxiliaryAccounts:
                obj._AuxiliaryAccounts.remove(self)
            self._Charges.remove(obj)

    def getAuxiliaryAgreement(self):
        """Auxiliary agreement regulating this account.
        """
        return self._AuxiliaryAgreement

    def setAuxiliaryAgreement(self, value):
        if self._AuxiliaryAgreement is not None:
            filtered = [x for x in self.AuxiliaryAgreement.AuxiliaryAccounts if x != self]
            self._AuxiliaryAgreement._AuxiliaryAccounts = filtered

        self._AuxiliaryAgreement = value
        if self._AuxiliaryAgreement is not None:
            if self not in self._AuxiliaryAgreement._AuxiliaryAccounts:
                self._AuxiliaryAgreement._AuxiliaryAccounts.append(self)

    AuxiliaryAgreement = property(getAuxiliaryAgreement, setAuxiliaryAgreement)

    def getPaymentTransactions(self):
        """All payments against this account.
        """
        return self._PaymentTransactions

    def setPaymentTransactions(self, value):
        for x in self._PaymentTransactions:
            x.AuxiliaryAccount = None
        for y in value:
            y._AuxiliaryAccount = self
        self._PaymentTransactions = value

    PaymentTransactions = property(getPaymentTransactions, setPaymentTransactions)

    def addPaymentTransactions(self, *PaymentTransactions):
        for obj in PaymentTransactions:
            obj.AuxiliaryAccount = self

    def removePaymentTransactions(self, *PaymentTransactions):
        for obj in PaymentTransactions:
            obj.AuxiliaryAccount = None

    # Details of the last debit transaction performed on this account.
    lastDebit = None

    # Details of the last credit transaction performed on this account.
    lastCredit = None

    # Current amounts now due for payment on this account.
    due = None

