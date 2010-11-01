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

from CIM14v13.IEC61968.Common.Organisation import Organisation

class Bank(Organisation):
    """Organisation that is a commercial bank, agency, or other institution that offers a similar service.
    """

    def __init__(self, iban='', branchCode='', bic='', BankAccounts=None, *args, **kw_args):
        """Initializes a new 'Bank' instance.

        @param iban: International bank account number defined in ISO 13616; for countries where IBAN is not in operation, the existing BIC or SWIFT codes may be used instead (see ISO 9362). 
        @param branchCode: Codified reference to the particular branch of the bank where BankAccount is held. 
        @param bic: Bank identifier code as defined in ISO 9362; for use in countries wher IBAN is not yet in operation. 
        @param BankAccounts: All BankAccounts this Bank provides.
        """
        #: International bank account number defined in ISO 13616; for countries where IBAN is not in operation, the existing BIC or SWIFT codes may be used instead (see ISO 9362). 
        self.iban = iban

        #: Codified reference to the particular branch of the bank where BankAccount is held. 
        self.branchCode = branchCode

        #: Bank identifier code as defined in ISO 9362; for use in countries wher IBAN is not yet in operation. 
        self.bic = bic

        self._BankAccounts = []
        self.BankAccounts = [] if BankAccounts is None else BankAccounts

        super(Bank, self).__init__(*args, **kw_args)

    def getBankAccounts(self):
        """All BankAccounts this Bank provides.
        """
        return self._BankAccounts

    def setBankAccounts(self, value):
        for x in self._BankAccounts:
            x._Bank = None
        for y in value:
            y._Bank = self
        self._BankAccounts = value

    BankAccounts = property(getBankAccounts, setBankAccounts)

    def addBankAccounts(self, *BankAccounts):
        for obj in BankAccounts:
            obj._Bank = self
            self._BankAccounts.append(obj)

    def removeBankAccounts(self, *BankAccounts):
        for obj in BankAccounts:
            obj._Bank = None
            self._BankAccounts.remove(obj)

