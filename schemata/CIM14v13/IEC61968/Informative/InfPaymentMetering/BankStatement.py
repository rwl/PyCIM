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

class BankStatement(Document):
    """A type of Document that records bank deposits made by Vendor of revenue collected at PointOfSale.
    """

    def __init__(self, depositAmount=0.0, posted=False, depositDateTime='', merchantCreditAmount=0.0, Vendor=None, MerchantAccount=None, BankAccount=None, *args, **kw_args):
        """Initializes a new 'BankStatement' instance.

        @param depositAmount: The amount that is deposited into the bank via BankAccount. 
        @param posted: True if mechantCreditAmount has been cerdited to MerchantAccount; typically happens when bank statement details are captured into payment system. 
        @param depositDateTime: The date and time the deposit is made. 
        @param merchantCreditAmount: The amount on this statement that is to be credited to MerchantAccount. 
        @param Vendor: The Vendor that made this BankStatement (by making deposit).
        @param MerchantAccount:
        @param BankAccount: BankAccount that generated this bank statement.
        """
        #: The amount that is deposited into the bank via BankAccount.
        self.depositAmount = depositAmount

        #: True if mechantCreditAmount has been cerdited to MerchantAccount; typically happens when bank statement details are captured into payment system.
        self.posted = posted

        #: The date and time the deposit is made.
        self.depositDateTime = depositDateTime

        #: The amount on this statement that is to be credited to MerchantAccount.
        self.merchantCreditAmount = merchantCreditAmount

        self._Vendor = None
        self.Vendor = Vendor

        self._MerchantAccount = None
        self.MerchantAccount = MerchantAccount

        self._BankAccount = None
        self.BankAccount = BankAccount

        super(BankStatement, self).__init__(*args, **kw_args)

    def getVendor(self):
        """The Vendor that made this BankStatement (by making deposit).
        """
        return self._Vendor

    def setVendor(self, value):
        if self._Vendor is not None:
            filtered = [x for x in self.Vendor.BankStatements if x != self]
            self._Vendor._BankStatements = filtered

        self._Vendor = value
        if self._Vendor is not None:
            self._Vendor._BankStatements.append(self)

    Vendor = property(getVendor, setVendor)

    def getMerchantAccount(self):
        
        return self._MerchantAccount

    def setMerchantAccount(self, value):
        if self._MerchantAccount is not None:
            filtered = [x for x in self.MerchantAccount.BankStatements if x != self]
            self._MerchantAccount._BankStatements = filtered

        self._MerchantAccount = value
        if self._MerchantAccount is not None:
            self._MerchantAccount._BankStatements.append(self)

    MerchantAccount = property(getMerchantAccount, setMerchantAccount)

    def getBankAccount(self):
        """BankAccount that generated this bank statement.
        """
        return self._BankAccount

    def setBankAccount(self, value):
        if self._BankAccount is not None:
            filtered = [x for x in self.BankAccount.BankStatements if x != self]
            self._BankAccount._BankStatements = filtered

        self._BankAccount = value
        if self._BankAccount is not None:
            self._BankAccount._BankStatements.append(self)

    BankAccount = property(getBankAccount, setBankAccount)

