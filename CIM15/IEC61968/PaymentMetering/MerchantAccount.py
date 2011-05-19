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

from CIM15.IEC61968.Common.Document import Document

class MerchantAccount(Document):
    """The operating account controlled by merchant agreement, against which vendor may vend tokens or receipt payments. Transactions via vendor shift debit the account and bank deposits via bank statement credit the account.The operating account controlled by merchant agreement, against which vendor may vend tokens or receipt payments. Transactions via vendor shift debit the account and bank deposits via bank statement credit the account.
    """

    def __init__(self, currentBalance=0.0, provisionalBalance=0.0, MerchantAgreement=None, Transactors=None, VendorShifts=None, *args, **kw_args):
        """Initialises a new 'MerchantAccount' instance.

        @param currentBalance: The current operating balance of this account. 
        @param provisionalBalance: The balance of this account after taking into account any pending debits from VendorShift.merchantDebitAmount and pending credits from BankStatement.merchantCreditAmount or credits (see also BankStatement attributes and VendorShift attributes). 
        @param MerchantAgreement: Merchant agreement that instantiated this merchant account.
        @param Transactors: All transactors this merchant account is registered with.
        @param VendorShifts: All vendor shifts that operate on this merchant account.
        """
        #: The current operating balance of this account.
        self.currentBalance = currentBalance

        #: The balance of this account after taking into account any pending debits from VendorShift.merchantDebitAmount and pending credits from BankStatement.merchantCreditAmount or credits (see also BankStatement attributes and VendorShift attributes).
        self.provisionalBalance = provisionalBalance

        self._MerchantAgreement = None
        self.MerchantAgreement = MerchantAgreement

        self._Transactors = []
        self.Transactors = [] if Transactors is None else Transactors

        self._VendorShifts = []
        self.VendorShifts = [] if VendorShifts is None else VendorShifts

        super(MerchantAccount, self).__init__(*args, **kw_args)

    _attrs = ["currentBalance", "provisionalBalance"]
    _attr_types = {"currentBalance": float, "provisionalBalance": float}
    _defaults = {"currentBalance": 0.0, "provisionalBalance": 0.0}
    _enums = {}
    _refs = ["MerchantAgreement", "Transactors", "VendorShifts"]
    _many_refs = ["Transactors", "VendorShifts"]

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
            if self not in self._MerchantAgreement._MerchantAccounts:
                self._MerchantAgreement._MerchantAccounts.append(self)

    MerchantAgreement = property(getMerchantAgreement, setMerchantAgreement)

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

    def getVendorShifts(self):
        """All vendor shifts that operate on this merchant account.
        """
        return self._VendorShifts

    def setVendorShifts(self, value):
        for x in self._VendorShifts:
            x.MerchantAccount = None
        for y in value:
            y._MerchantAccount = self
        self._VendorShifts = value

    VendorShifts = property(getVendorShifts, setVendorShifts)

    def addVendorShifts(self, *VendorShifts):
        for obj in VendorShifts:
            obj.MerchantAccount = self

    def removeVendorShifts(self, *VendorShifts):
        for obj in VendorShifts:
            obj.MerchantAccount = None

