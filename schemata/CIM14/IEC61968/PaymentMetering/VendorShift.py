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

from CIM14.IEC61968.PaymentMetering.Shift import Shift

class VendorShift(Shift):
    """The operating shift for a vendor during which he may transact against the merchant's account. It aggregates transactions and receipts during the shift and periodically debits a merchant account. The totals in VendorShift should always = sum of totals aggregated in all cashier shifts that were open under the particular vendor shift.
    """

    def __init__(self, merchantDebitAmount=0.0, posted=False, MerchantAccount=None, Transactions=None, Receipts=None, Vendor=None, **kw_args):
        """Initializes a new 'VendorShift' instance.

        @param merchantDebitAmount: The amount that is to be debited from the merchant account for this vendor shift. This amount reflects the sum(PaymentTransaction.transactionAmount). 
        @param posted: = true if merchantDebitAmount has been debited from MerchantAccount; typically happens at the end of VendorShift when it closes. 
        @param MerchantAccount: Merchant account this vendor shift periodically debits (based on aggregated transactions).
        @param Transactions:
        @param Receipts:
        @param Vendor: Vendor that opens and owns this vendor shift.
        """
        #: The amount that is to be debited from the merchant account for this vendor shift. This amount reflects the sum(PaymentTransaction.transactionAmount).
        self.merchantDebitAmount = merchantDebitAmount

        #: = true if merchantDebitAmount has been debited from MerchantAccount; typically happens at the end of VendorShift when it closes.
        self.posted = posted

        self._MerchantAccount = None
        self.MerchantAccount = MerchantAccount

        self._Transactions = []
        self.Transactions = [] if Transactions is None else Transactions

        self._Receipts = []
        self.Receipts = [] if Receipts is None else Receipts

        self._Vendor = None
        self.Vendor = Vendor

        super(VendorShift, self).__init__(**kw_args)

    def getMerchantAccount(self):
        """Merchant account this vendor shift periodically debits (based on aggregated transactions).
        """
        return self._MerchantAccount

    def setMerchantAccount(self, value):
        if self._MerchantAccount is not None:
            filtered = [x for x in self.MerchantAccount.VendorShifts if x != self]
            self._MerchantAccount._VendorShifts = filtered

        self._MerchantAccount = value
        if self._MerchantAccount is not None:
            self._MerchantAccount._VendorShifts.append(self)

    MerchantAccount = property(getMerchantAccount, setMerchantAccount)

    def getTransactions(self):
        
        return self._Transactions

    def setTransactions(self, value):
        for x in self._Transactions:
            x._VendorShift = None
        for y in value:
            y._VendorShift = self
        self._Transactions = value

    Transactions = property(getTransactions, setTransactions)

    def addTransactions(self, *Transactions):
        for obj in Transactions:
            obj._VendorShift = self
            self._Transactions.append(obj)

    def removeTransactions(self, *Transactions):
        for obj in Transactions:
            obj._VendorShift = None
            self._Transactions.remove(obj)

    def getReceipts(self):
        
        return self._Receipts

    def setReceipts(self, value):
        for x in self._Receipts:
            x._VendorShift = None
        for y in value:
            y._VendorShift = self
        self._Receipts = value

    Receipts = property(getReceipts, setReceipts)

    def addReceipts(self, *Receipts):
        for obj in Receipts:
            obj._VendorShift = self
            self._Receipts.append(obj)

    def removeReceipts(self, *Receipts):
        for obj in Receipts:
            obj._VendorShift = None
            self._Receipts.remove(obj)

    def getVendor(self):
        """Vendor that opens and owns this vendor shift.
        """
        return self._Vendor

    def setVendor(self, value):
        if self._Vendor is not None:
            filtered = [x for x in self.Vendor.VendorShifts if x != self]
            self._Vendor._VendorShifts = filtered

        self._Vendor = value
        if self._Vendor is not None:
            self._Vendor._VendorShifts.append(self)

    Vendor = property(getVendor, setVendor)

