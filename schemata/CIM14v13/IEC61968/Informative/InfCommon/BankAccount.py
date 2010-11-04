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

class BankAccount(Document):
    """Bank account.
    """

    def __init__(self, accountNumber='', ServiceSupplier=None, Bank=None, BankStatements=None, **kw_args):
        """Initializes a new 'BankAccount' instance.

        @param accountNumber: Account reference number. 
        @param ServiceSupplier: ServiceSupplier that is owner of this BankAccount.
        @param Bank: Bank that provides this BankAccount.
        @param BankStatements: All bank statements generated from this bank account.
        """
        #: Account reference number.
        self.accountNumber = accountNumber

        self._ServiceSupplier = None
        self.ServiceSupplier = ServiceSupplier

        self._Bank = None
        self.Bank = Bank

        self._BankStatements = []
        self.BankStatements = [] if BankStatements is None else BankStatements

        super(BankAccount, self).__init__(**kw_args)

    def getServiceSupplier(self):
        """ServiceSupplier that is owner of this BankAccount.
        """
        return self._ServiceSupplier

    def setServiceSupplier(self, value):
        if self._ServiceSupplier is not None:
            filtered = [x for x in self.ServiceSupplier.BankAccounts if x != self]
            self._ServiceSupplier._BankAccounts = filtered

        self._ServiceSupplier = value
        if self._ServiceSupplier is not None:
            self._ServiceSupplier._BankAccounts.append(self)

    ServiceSupplier = property(getServiceSupplier, setServiceSupplier)

    def getBank(self):
        """Bank that provides this BankAccount.
        """
        return self._Bank

    def setBank(self, value):
        if self._Bank is not None:
            filtered = [x for x in self.Bank.BankAccounts if x != self]
            self._Bank._BankAccounts = filtered

        self._Bank = value
        if self._Bank is not None:
            self._Bank._BankAccounts.append(self)

    Bank = property(getBank, setBank)

    def getBankStatements(self):
        """All bank statements generated from this bank account.
        """
        return self._BankStatements

    def setBankStatements(self, value):
        for x in self._BankStatements:
            x._BankAccount = None
        for y in value:
            y._BankAccount = self
        self._BankStatements = value

    BankStatements = property(getBankStatements, setBankStatements)

    def addBankStatements(self, *BankStatements):
        for obj in BankStatements:
            obj._BankAccount = self
            self._BankStatements.append(obj)

    def removeBankStatements(self, *BankStatements):
        for obj in BankStatements:
            obj._BankAccount = None
            self._BankStatements.remove(obj)

