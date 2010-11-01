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

class MerchantAccount(Document):
    """The operating account controlled by MerchantAgreement, against which Vendor may vend tokens or receipt payments. Transactions via VendorShift debit the account and bank deposits via BankStatement credit the account.
    """

    def __init__(self, provisionalBalance=0.0, currentBalance=0.0, Vendors=None, Transactors=None, BankStatements=None, MerchantAgreement=None, VendorShifts=None, *args, **kw_args):
        """Initializes a new 'MerchantAccount' instance.

        @param provisionalBalance: The balance of this account after taking into account any pending debits from VendorShift.merchantDebitAmount and pending credits from BankStatement.merchantCreditAmount or credits (see also BankStatement attributes and VendorShift attributes). 
        @param currentBalance: The current operating balance of this account. 
        @param Vendors: All vendors selling tokens or receipt payments against this merchant account.
        @param Transactors: All transactors this merchant account is registered with.
        @param BankStatements:
        @param MerchantAgreement: Merchant agreement that instantiated this merchant account.
        @param VendorShifts: All vendor shifts that operate on this merchant account.
        """
        #: The balance of this account after taking into account any pending debits from VendorShift.merchantDebitAmount and pending credits from BankStatement.merchantCreditAmount or credits (see also BankStatement attributes and VendorShift attributes). 
        self.provisionalBalance = provisionalBalance

        #: The current operating balance of this account. 
        self.currentBalance = currentBalance

        self._Vendors = []
        self.Vendors = [] if Vendors is None else Vendors

        self._Transactors = []
        self.Transactors = [] if Transactors is None else Transactors

        self._BankStatements = []
        self.BankStatements = [] if BankStatements is None else BankStatements

        self._MerchantAgreement = None
        self.MerchantAgreement = MerchantAgreement

        self._VendorShifts = []
        self.VendorShifts = [] if VendorShifts is None else VendorShifts

        super(MerchantAccount, self).__init__(*args, **kw_args)

    def getVendors(self):
        """All vendors selling tokens or receipt payments against this merchant account.
        """
        return self._Vendors

    def setVendors(self, value):
        for x in self._Vendors:
            x._MerchantAccount = None
        for y in value:
            y._MerchantAccount = self
        self._Vendors = value

    Vendors = property(getVendors, setVendors)

    def addVendors(self, *Vendors):
        for obj in Vendors:
            obj._MerchantAccount = self
            self._Vendors.append(obj)

    def removeVendors(self, *Vendors):
        for obj in Vendors:
            obj._MerchantAccount = None
            self._Vendors.remove(obj)

    def getTransactors(self):
        """All transactors this merchant account is registered with.
        """
        return self._Transactors

    def setTransactors(self, value):
        for p in self._Transactors:
            filtered = [q for q in p.MerchantAccounts if q != self]
            self._Transactors._MerchantAccounts = filtered
        for r in value:
            if self not in r._MerchantAccounts:
                r._MerchantAccounts.append(self)
        self._Transactors = value

    Transactors = property(getTransactors, setTransactors)

    def addTransactors(self, *Transactors):
        for obj in Transactors:
            if self not in obj._MerchantAccounts:
                obj._MerchantAccounts.append(self)
            self._Transactors.append(obj)

    def removeTransactors(self, *Transactors):
        for obj in Transactors:
            if self in obj._MerchantAccounts:
                obj._MerchantAccounts.remove(self)
            self._Transactors.remove(obj)

    def getBankStatements(self):
        
        return self._BankStatements

    def setBankStatements(self, value):
        for x in self._BankStatements:
            x._MerchantAccount = None
        for y in value:
            y._MerchantAccount = self
        self._BankStatements = value

    BankStatements = property(getBankStatements, setBankStatements)

    def addBankStatements(self, *BankStatements):
        for obj in BankStatements:
            obj._MerchantAccount = self
            self._BankStatements.append(obj)

    def removeBankStatements(self, *BankStatements):
        for obj in BankStatements:
            obj._MerchantAccount = None
            self._BankStatements.remove(obj)

    def getMerchantAgreement(self):
        """Merchant agreement that instantiated this merchant account.
        """
        return self._MerchantAgreement

    def setMerchantAgreement(self, value):
        if self._MerchantAgreement is not None:
            filtered = [x for x in self.MerchantAgreement.MerchantAccounts if x != self]
            self._MerchantAgreement._MerchantAccounts = filtered

        self._MerchantAgreement = value
        if self._MerchantAgreement is not None:
            self._MerchantAgreement._MerchantAccounts.append(self)

    MerchantAgreement = property(getMerchantAgreement, setMerchantAgreement)

    def getVendorShifts(self):
        """All vendor shifts that operate on this merchant account.
        """
        return self._VendorShifts

    def setVendorShifts(self, value):
        for x in self._VendorShifts:
            x._MerchantAccount = None
        for y in value:
            y._MerchantAccount = self
        self._VendorShifts = value

    VendorShifts = property(getVendorShifts, setVendorShifts)

    def addVendorShifts(self, *VendorShifts):
        for obj in VendorShifts:
            obj._MerchantAccount = self
            self._VendorShifts.append(obj)

    def removeVendorShifts(self, *VendorShifts):
        for obj in VendorShifts:
            obj._MerchantAccount = None
            self._VendorShifts.remove(obj)

