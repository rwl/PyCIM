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

class AuxiliaryAccount(Document):
    """Variable and dynamic part of AuxiliaryAgreement, generally representing the current state of the account related to the outstanding balance defined in AuxiliaryAgreement.
    """

    def __init__(self, balance=0.0, principleAmount=0.0, lastDebit=None, Charges=None, lastCredit=None, AuxiliaryAgreement=None, PaymentTransactions=None, due=None, *args, **kw_args):
        """Initializes a new 'AuxiliaryAccount' instance.

        @param balance: The total amount currently remaining on this account that is required to be paid in order to settle the account to zero. This excludes any due amounts not yet paid. 
        @param principleAmount: The initial principle amount, with which this account was instantiated. 
        @param lastDebit: Details of the last debit transaction performed on this account.
        @param Charges: All charges levied on this account.
        @param lastCredit: Details of the last credit transaction performed on this account.
        @param AuxiliaryAgreement: Auxiliary agreement regulating this account.
        @param PaymentTransactions: All payments against this account.
        @param due: Current amounts now due for payment on this account.
        """
        #: The total amount currently remaining on this account that is required to be paid in order to settle the account to zero. This excludes any due amounts not yet paid.
        self.balance = balance

        #: The initial principle amount, with which this account was instantiated.
        self.principleAmount = principleAmount

        self.lastDebit = lastDebit

        self._Charges = []
        self.Charges = [] if Charges is None else Charges

        self.lastCredit = lastCredit

        self._AuxiliaryAgreement = None
        self.AuxiliaryAgreement = AuxiliaryAgreement

        self._PaymentTransactions = []
        self.PaymentTransactions = [] if PaymentTransactions is None else PaymentTransactions

        self.due = due

        super(AuxiliaryAccount, self).__init__(*args, **kw_args)

    # Details of the last debit transaction performed on this account.
    lastDebit = None

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

    # Details of the last credit transaction performed on this account.
    lastCredit = None

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
            self._AuxiliaryAgreement._AuxiliaryAccounts.append(self)

    AuxiliaryAgreement = property(getAuxiliaryAgreement, setAuxiliaryAgreement)

    def getPaymentTransactions(self):
        """All payments against this account.
        """
        return self._PaymentTransactions

    def setPaymentTransactions(self, value):
        for x in self._PaymentTransactions:
            x._AuxiliaryAccount = None
        for y in value:
            y._AuxiliaryAccount = self
        self._PaymentTransactions = value

    PaymentTransactions = property(getPaymentTransactions, setPaymentTransactions)

    def addPaymentTransactions(self, *PaymentTransactions):
        for obj in PaymentTransactions:
            obj._AuxiliaryAccount = self
            self._PaymentTransactions.append(obj)

    def removePaymentTransactions(self, *PaymentTransactions):
        for obj in PaymentTransactions:
            obj._AuxiliaryAccount = None
            self._PaymentTransactions.remove(obj)

    # Current amounts now due for payment on this account.
    due = None

